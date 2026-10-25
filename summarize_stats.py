import pandas as pd

df = pd.read_csv('02_Building_AI_Agents/Project_Market_Research_Agent/data/curing_press_thermal_scrap_telemetry.csv')
print('=== EXECUTIVE DATA SUMMARY ===')
print(f'Total Inspections: {len(df)}')
print(f'Total Presses Monitored: {df["Press_ID"].nunique()}')
print(f'Total Lines: {df["Line"].nunique()}')
print(f'Cycle Interruption Rate: {df["Curing_Cycle_Interrupted"].mean()*100:.2f}% ({df["Curing_Cycle_Interrupted"].sum()} aborts)')
print(f'Total Scrapped TBR Tyres: {df["Scrapped_Tyres"].sum()}')
print(f'Direct Tyre Scrap Cost: EUR {df["Direct_Scrap_Cost_EUR"].sum():,.2f}')
print(f'Unplanned Downtime: {df["Unplanned_Downtime_Minutes"].sum()} minutes ({df["Unplanned_Downtime_Minutes"].sum()/60:.1f} hours)')
print(f'Downtime Financial Loss: EUR {df["Downtime_Cost_EUR"].sum():,.2f}')
print(f'Total Combined Operational Loss: EUR {(df["Direct_Scrap_Cost_EUR"].sum() + df["Downtime_Cost_EUR"].sum()):,.2f}')

print('\n=== LINE BREAKDOWN ===')
line_sum = df.groupby('Line').agg({
    'Curing_Cycle_Interrupted': 'sum',
    'Scrapped_Tyres': 'sum',
    'Direct_Scrap_Cost_EUR': 'sum',
    'Unplanned_Downtime_Minutes': 'sum',
    'Downtime_Cost_EUR': 'sum'
}).reset_index()
line_sum['Total_Loss_EUR'] = line_sum['Direct_Scrap_Cost_EUR'] + line_sum['Downtime_Cost_EUR']
line_sum['Loss_Share_%'] = (line_sum['Total_Loss_EUR'] / line_sum['Total_Loss_EUR'].sum()) * 100
print(line_sum.to_string(index=False))

print('\n=== COMPONENT OUTLIER TRIAGE ===')
comp_sum = df.groupby('Component_Type').agg({
    'Delta_T_C': ['mean', 'max'],
    'Curing_Cycle_Interrupted': 'sum',
    'Scrapped_Tyres': 'sum'
})
print(comp_sum)

print('\n=== THERMAL THRESHOLDS VS ABORTS ===')
norm_aborts = df[df['Delta_T_C'] < 25]['Curing_Cycle_Interrupted'].sum()
warn_aborts = df[(df['Delta_T_C'] >= 25) & (df['Delta_T_C'] < 32)]['Curing_Cycle_Interrupted'].sum()
sev_aborts = df[df['Delta_T_C'] >= 32]['Curing_Cycle_Interrupted'].sum()
print(f'Normal (Delta-T < 25C) Aborts: {norm_aborts}')
print(f'Warning (25C <= Delta-T < 32C) Aborts: {warn_aborts}')
print(f'Severe (Delta-T >= 32C) Aborts: {sev_aborts}')
