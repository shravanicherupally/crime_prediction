import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Number of samples
n_samples = 3000

# Possible values for each feature
crime_categories = ['Theft', 'Murder', 'Assault', 'Fraud']
severity_levels = ['Minor', 'Moderate', 'Severe']
weapon_use = [0, 1]  # 0 = No, 1 = Yes
repeat_offender = [0, 1]  # 0 = No, 1 = Yes

# IPC Sections & Punishments mapping (simplified example)
ipc_punishment_map = {
    'Theft': 'IPC 379 - Up to 3 years',
    'Murder': 'IPC 302 - Life Imprisonment',
    'Assault': 'IPC 324 - Up to 3 years',
    'Fraud': 'IPC 420 - Up to 7 years'
}

# Generate balanced dataset
samples_per_category = n_samples // len(crime_categories)

data = []

for crime in crime_categories:
    for _ in range(samples_per_category):
        severity = np.random.choice(severity_levels)
        weapon = np.random.choice(weapon_use)
        repeat = np.random.choice(repeat_offender)
        target = ipc_punishment_map[crime]

        data.append([crime, severity, weapon, repeat, target])

# Shuffle the dataset
np.random.shuffle(data)

# Create DataFrame
df = pd.DataFrame(data, columns=[
    'Crime_Category',
    'Crime_Severity_Level',
    'Use_of_Weapon',
    'Repeat_Offender',
    'IPC_Section_and_Punishment'
])

# Save to CSV
df.to_csv('dataset.csv', index=False)

print("✅ Dataset created with shape:", df.shape)
print(df.head())
