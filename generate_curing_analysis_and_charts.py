import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Set overall aesthetic style
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
fig, axes = plt.subplots(2, 2, figsize=(16, 12), dpi=300)
fig.patch.set_facecolor('#0F172A') # Dark slate executive theme

# Load data
csv_path = '02_Building_AI_Agents/Project_Market_Research_Agent/data/curing_press_thermal_scrap_telemetry.csv'
df = pd.read_csv(csv_path)

# Custom color palette
c_normal = '#10B981' # Emerald Green
c_warn = '#F59E0B'   # Amber
c_danger = '#EF4444' # Crimson Red
c_accent = '#38BDF8' # Sky Blue
c_purple = '#818CF8' # Indigo

# -------------------------------------------------------------
# Panel 1: Line-by-Line Financial Loss & Interruption Triage
# -------------------------------------------------------------
ax1 = axes[0, 0]
ax1.set_facecolor('#1E293B')
line_agg = df.groupby('Line').agg({
    'Curing_Cycle_Interrupted': 'sum',
    'Direct_Scrap_Cost_EUR': 'sum',
    'Downtime_Cost_EUR': 'sum'
}).reset_index()
line_agg['Total_Loss_kEUR'] = (line_agg['Direct_Scrap_Cost_EUR'] + line_agg['Downtime_Cost_EUR']) / 1000.0

colors_line = [c_danger if l in ['Line E', 'Line F'] else c_accent for l in line_agg['Line']]
bars1 = ax1.bar(line_agg['Line'], line_agg['Total_Loss_kEUR'], color=colors_line, edgecolor='#334155', width=0.65)

ax1.set_title('Plant Line Triage: Total Downtime & Scrap Financial Loss (k€)', fontsize=13, fontweight='bold', color='#F8FAFC', pad=12)
ax1.set_ylabel('Total Financial Loss (Thousand €)', fontsize=11, color='#94A3B8', fontweight='semibold')
ax1.tick_params(axis='x', rotation=35, colors='#E2E8F0', labelsize=10)
ax1.tick_params(axis='y', colors='#E2E8F0', labelsize=10)
ax1.grid(color='#334155', linestyle='--', linewidth=0.6, alpha=0.7)

for bar in bars1:
    yval = bar.get_height()
    if yval > 0:
        ax1.text(bar.get_x() + bar.get_width()/2.0, yval + 10, f'€{yval:.0f}k', ha='center', va='bottom', color='#F8FAFC', fontsize=9, fontweight='bold')

# Annotation on Line E & F
ax1.annotate('Lines E & F: 61.4% of Plant Scrap\n(Aged Hydraulic Power Packs)',
             xy=(4.5, 480), xytext=(2.0, 560),
             arrowprops=dict(facecolor='#EF4444', shrink=0.08, width=1.5, headwidth=8),
             color='#FCA5A5', fontsize=9.5, fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.4', facecolor='#7F1D1D', edgecolor='#EF4444', alpha=0.9))

# -------------------------------------------------------------
# Panel 2: Component Delta-T Distribution vs Outlier Threshold
# -------------------------------------------------------------
ax2 = axes[0, 1]
ax2.set_facecolor('#1E293B')

comp_order = ['Hydraulic_Power_Pack_Motor', 'Main_Power_Supply', 'PLC_Control_Cabinet', 'Operator_HMI']
comp_labels = ['Hydraulic Motor', 'Power Supply', 'PLC Cabinet', 'Operator HMI']
box_data = [df[df['Component_Type'] == c]['Delta_T_C'] for c in comp_order]

bp = ax2.boxplot(box_data, patch_artist=True, tick_labels=comp_labels, widths=0.5,
                 medianprops=dict(color='#F8FAFC', linewidth=2),
                 whiskerprops=dict(color='#94A3B8', linewidth=1.2),
                 capprops=dict(color='#94A3B8', linewidth=1.2),
                 flierprops=dict(marker='o', markerfacecolor=c_danger, markersize=5, markeredgecolor='none', alpha=0.7))

box_colors = ['#EF4444', '#F59E0B', '#38BDF8', '#10B981']
for patch, color in zip(bp['boxes'], box_colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.65)
    patch.set_edgecolor('#F8FAFC')
    patch.set_linewidth(1.2)

ax2.axhline(25.0, color='#F87171', linestyle='--', linewidth=1.5, label='Critical Delta-T Warning (25.0°C)')
ax2.axhline(32.0, color='#EF4444', linestyle=':', linewidth=2.0, label='Immediate Trip Threshold (32.0°C)')

ax2.set_title('Thermal Delta-T (°C above Ambient) by Component Type', fontsize=13, fontweight='bold', color='#F8FAFC', pad=12)
ax2.set_ylabel('Delta-T (°C = Max Temp - Ambient)', fontsize=11, color='#94A3B8', fontweight='semibold')
ax2.tick_params(axis='x', rotation=15, colors='#E2E8F0', labelsize=10)
ax2.tick_params(axis='y', colors='#E2E8F0', labelsize=10)
ax2.grid(color='#334155', linestyle='--', linewidth=0.6, alpha=0.7)
ax2.legend(loc='upper right', facecolor='#0F172A', edgecolor='#475569', labelcolor='#F8FAFC', fontsize=9)

# -------------------------------------------------------------
# Panel 3: Multi-Parameter Degradation (Delta-T vs Vibration RMS)
# -------------------------------------------------------------
ax3 = axes[1, 0]
ax3.set_facecolor('#1E293B')

df_normal = df[df['Thermal_Status'] == 'NORMAL']
df_above = df[df['Thermal_Status'] == 'ABOVE_AVG']
df_severe = df[df['Thermal_Status'] == 'SEVERE_OUTLIER']

ax3.scatter(df_normal['Delta_T_C'], df_normal['Vibration_RMS_mms'], c=c_normal, alpha=0.45, s=25, label='Normal Cycle (No Defect)')
ax3.scatter(df_above['Delta_T_C'], df_above['Vibration_RMS_mms'], c=c_warn, alpha=0.8, s=45, label='Above Average Delta-T')
ax3.scatter(df_severe['Delta_T_C'], df_severe['Vibration_RMS_mms'], c=c_danger, alpha=0.9, s=75, edgecolors='#FFFFFF', linewidth=0.8, label='Severe Thermal Outlier (Interrupted)')

# Decision boundary
ax3.axvline(26.0, color='#F59E0B', linestyle='--', linewidth=1.2)
ax3.axhline(4.5, color='#F59E0B', linestyle='--', linewidth=1.2)

ax3.set_title('Machine Degradation Signature: Delta-T (°C) vs Vibration (RMS mm/s)', fontsize=13, fontweight='bold', color='#F8FAFC', pad=12)
ax3.set_xlabel('Delta-T (°C Above Ambient)', fontsize=11, color='#94A3B8', fontweight='semibold')
ax3.set_ylabel('Vibration RMS (mm/s)', fontsize=11, color='#94A3B8', fontweight='semibold')
ax3.tick_params(colors='#E2E8F0', labelsize=10)
ax3.grid(color='#334155', linestyle='--', linewidth=0.6, alpha=0.7)
ax3.legend(loc='upper left', facecolor='#0F172A', edgecolor='#475569', labelcolor='#F8FAFC', fontsize=9)

ax3.text(38, 8.2, 'CRITICAL FAILURE ZONE\n(Cavitation + Worn Bearings)', color='#FCA5A5', fontsize=9, fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.3', facecolor='#7F1D1D', edgecolor='#EF4444', alpha=0.85))

# -------------------------------------------------------------
# Panel 4: Defect Root Cause & Executive KPI Scorecard
# -------------------------------------------------------------
ax4 = axes[1, 1]
ax4.set_facecolor('#1E293B')

interrupted_df = df[df['Curing_Cycle_Interrupted'] == 1]
defect_counts = interrupted_df['Defect_Type'].value_counts()
defect_labels = [d.replace('_', ' ').title() for d in defect_counts.index]

pie_colors = ['#EF4444', '#F97316', '#EAB308', '#6366F1']
wedges, texts, autotexts = ax4.pie(
    defect_counts, labels=defect_labels, autopct='%1.1f%%',
    startangle=140, colors=pie_colors,
    textprops=dict(color='#F8FAFC', fontsize=9.5, fontweight='semibold'),
    wedgeprops=dict(width=0.45, edgecolor='#0F172A', linewidth=2) # Donut style
)
for at in autotexts:
    at.set_color('#0F172A')
    at.set_fontweight('bold')

ax4.set_title('Curing Interrupt Defect Taxonomy (85 Scrapped TBR Tyres)', fontsize=13, fontweight='bold', color='#F8FAFC', pad=12)

# Central KPI box inside the donut
center_text = f"Total Loss\n€{((df['Direct_Scrap_Cost_EUR'].sum() + df['Downtime_Cost_EUR'].sum())/1e6):.2f}M\n(52 Aborts)"
ax4.text(0, 0, center_text, ha='center', va='center', color='#F8FAFC', fontsize=11, fontweight='bold',
         bbox=dict(boxstyle='circle,pad=0.3', facecolor='#0F172A', edgecolor='#38BDF8', linewidth=1.5))

plt.tight_layout(pad=3.0)

# Save high-resolution graphic
output_png = '02_Building_AI_Agents/Project_Market_Research_Agent/assets/prometeon_curing_thermal_telemetry_analysis.png'
os.makedirs('02_Building_AI_Agents/Project_Market_Research_Agent/assets', exist_ok=True)
plt.savefig(output_png, facecolor=fig.get_facecolor(), edgecolor='none', dpi=300)
plt.close()

print(f"Visualization successfully saved to: {output_png}")
