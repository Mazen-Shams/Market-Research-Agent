import numpy as np
import pandas as pd
import os

np.random.seed(42)

n_records = 1500
lines = ['Line A', 'Line B', 'Line C', 'Line D', 'Line E', 'Line F', 'Line G', 'Line H', 'Line I', 'Line J']
components = ['Hydraulic_Power_Pack_Motor', 'Main_Power_Supply', 'PLC_Control_Cabinet', 'Operator_HMI']

# Assign presses to lines (total 87 presses)
presses = []
for line_idx, line in enumerate(lines):
    count = 9 if line_idx < 7 else 8
    clean_line = line.replace(' ', '')
    for p in range(1, count + 1):
        press_num = len(presses) + 1
        presses.append((f'P{press_num:02d}_{clean_line}', line))

records = []
start_date = pd.Timestamp('2026-01-01')

for i in range(n_records):
    press_id, line = presses[np.random.choice(len(presses))]
    comp = np.random.choice(components, p=[0.40, 0.25, 0.25, 0.10])
    ts = start_date + pd.Timedelta(minutes=int(np.random.uniform(0, 120 * 24 * 60)))
    
    # Ambient temp in Alexandria plant (seasonal range 22 to 36 C)
    ambient = np.random.normal(28.5, 3.5)
    
    # Failure probability higher in Line E and F (aged assets) and Hydraulic Motor
    is_aged_line = line in ['Line E', 'Line F']
    base_prob = 0.085 if is_aged_line else 0.022
    if comp == 'Hydraulic_Power_Pack_Motor':
        base_prob *= 1.8
    elif comp == 'Main_Power_Supply':
        base_prob *= 1.3
    elif comp == 'Operator_HMI':
        base_prob *= 0.1
        
    is_anomaly = np.random.rand() < base_prob
    
    if is_anomaly:
        # Severe thermal anomaly
        delta_t = np.random.uniform(26.0, 52.0)
        max_temp = ambient + delta_t
        center_temp = max_temp - np.random.uniform(3.0, 8.0)
        vibration = np.random.uniform(4.5, 9.8) if comp == 'Hydraulic_Power_Pack_Motor' else np.random.uniform(1.2, 2.8)
        pressure = np.random.uniform(130.0, 175.0) # Pressure drop
        status = 'SEVERE_OUTLIER' if delta_t > 32.0 else 'ABOVE_AVG'
        interrupted = 1 if np.random.rand() < 0.74 else 0
    else:
        # Normal baseline
        delta_t = np.random.uniform(4.0, 18.0)
        max_temp = ambient + delta_t
        center_temp = max_temp - np.random.uniform(1.0, 4.0)
        vibration = np.random.uniform(1.0, 3.2) if comp == 'Hydraulic_Power_Pack_Motor' else np.random.uniform(0.5, 1.5)
        pressure = np.random.uniform(190.0, 215.0)
        status = 'NORMAL'
        interrupted = 0

    if interrupted:
        defect_type = np.random.choice(
            ['BLISTER_POROSITY', 'UNDER_CURED_BEAD', 'TREAD_SEPARATION', 'IRREVERSIBLE_SCORCH'],
            p=[0.45, 0.25, 0.20, 0.10]
        )
        scrapped_tyres = np.random.choice([1, 2], p=[0.38, 0.62]) # Twin-cavity curing presses scrap 1 or 2 tyres
        scrap_cost = scrapped_tyres * 385.0 # Average EUR 385 per commercial truck radial tyre
        downtime_min = int(np.random.uniform(45, 160))
        downtime_cost = downtime_min * (22500.0 / 60.0) # EUR 375/min
    else:
        defect_type = 'NONE'
        scrapped_tyres = 0
        scrap_cost = 0.0
        downtime_min = 0
        downtime_cost = 0.0

    records.append({
        'Inspection_ID': f'INS-{i+1:05d}',
        'Timestamp': ts.strftime('%Y-%m-%d %H:%M:%S'),
        'Press_ID': press_id,
        'Line': line,
        'Component_Type': comp,
        'Ambient_Temp_C': round(float(ambient), 1),
        'Center_Temp_C': round(float(center_temp), 1),
        'Max_Temp_C': round(float(max_temp), 1),
        'Delta_T_C': round(float(delta_t), 1),
        'Vibration_RMS_mms': round(float(vibration), 2),
        'Hydraulic_Pressure_Bar': round(float(pressure), 1),
        'Thermal_Status': status,
        'Curing_Cycle_Interrupted': int(interrupted),
        'Defect_Type': defect_type,
        'Scrapped_Tyres': int(scrapped_tyres),
        'Direct_Scrap_Cost_EUR': round(float(scrap_cost), 2),
        'Unplanned_Downtime_Minutes': int(downtime_min),
        'Downtime_Cost_EUR': round(float(downtime_cost), 2)
    })

df = pd.DataFrame(records)
os.makedirs('02_Building_AI_Agents/Project_Market_Research_Agent/data', exist_ok=True)
csv_path = '02_Building_AI_Agents/Project_Market_Research_Agent/data/curing_press_thermal_scrap_telemetry.csv'
df.to_csv(csv_path, index=False)
print(f'Generated {len(df)} records in {csv_path}')
print(f'Total interruptions: {df["Curing_Cycle_Interrupted"].sum()}')
print(f'Total scrap tyres: {df["Scrapped_Tyres"].sum()}')
print(f'Total direct scrap cost: EUR {df["Direct_Scrap_Cost_EUR"].sum():,.2f}')
print(f'Total downtime cost: EUR {df["Downtime_Cost_EUR"].sum():,.2f}')
print(f'Combined total financial impact: EUR {(df["Direct_Scrap_Cost_EUR"].sum() + df["Downtime_Cost_EUR"].sum()):,.2f}')
