import pandas as pd
import matplotlib.pyplot as plt

file_path = r"C:\Users\kilgo\OneDrive\desktop\STAT4188FINALPROJECT/mergedData.csv" 
merged_data = pd.read_csv(file_path)

print("Columns in the dataset:", merged_data.columns)

merged_data.columns = merged_data.columns.str.strip()

temperature_column = 'Temperature(F)'  
study_duration_column = 'Study Duration (hours)'


if temperature_column in merged_data.columns and study_duration_column in merged_data.columns:
    plt.figure(figsize=(8, 6))
    plt.scatter(merged_data[temperature_column], merged_data[study_duration_column], alpha=0.7, color='blue')
    plt.title('Temperature vs. Study Duration', fontsize=14)
    plt.xlabel('Temperature (°F)', fontsize=12)
    plt.ylabel('Study Duration (hours)', fontsize=12)
    plt.grid(alpha=0.3)
    plt.show()
else:
    print(f"Error: Columns '{temperature_column}' or '{study_duration_column}' not found in the dataset.")

correlation = merged_data[['Temperature(F)', 'Study Duration (hours)']].corr()
print(correlation)
