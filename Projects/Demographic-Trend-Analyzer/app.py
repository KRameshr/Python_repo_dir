import os
import pandas as pd
import matplotlib.pyplot as plt


# 1. CONFIGURATION & DIRECTORY SETUP
# Ensure the folder path matches your local structure
FOLDER_PATH = 'names' 
DATA_LIST = []


# 2. DATA INGESTION & AGGREGATION
if not os.path.exists(FOLDER_PATH):
    print(f"Critical Error: The folder '{FOLDER_PATH}' was not found.")
    print("Please verify the directory exists in your project root.")
else:
    print(f"Folder '{FOLDER_PATH}' identified. Beginning batch processing...")

    # Iterate through all 'yobXXXX.txt' files in the names folder
    for file_name in os.listdir(FOLDER_PATH):
        if file_name.endswith('.txt') and 'yob' in file_name:
            file_path = os.path.join(FOLDER_PATH, file_name)
            
            # Load specific year data
            df = pd.read_csv(file_path, header=None, names=['Name', 'Gender', 'Count'])
            
            # Extract year from filename (yob1880.txt -> 1880)
            df['Year'] = int(file_name[3:7])
            DATA_LIST.append(df)

    # Concatenate all yearly DataFrames into one central dataset
    master_df = pd.concat(DATA_LIST, ignore_index=True)
    print(f"Data Pipeline Complete! Total Records Processed: {len(master_df):,}")

  
    # 3. TREND VISUALIZATION (Task 2)

    print("\n--- Generating Demographic Trend Charts ---")
    
    # Pivot data to compare Birth Counts by Year and Gender
    gender_trends = master_df.pivot_table(values='Count', index='Year', columns='Gender', aggfunc='sum')
    
    plt.figure(figsize=(10, 6))
    gender_trends.plot(kind='line', ax=plt.gca(), title='Annual Birth Counts: Male vs Female (Historical)')
    plt.ylabel('Birth Count')
    plt.xlabel('Year of Birth')
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Export for Portfolio
    plt.savefig('baby_name_trends.png', dpi=300, bbox_inches='tight')
    print("Visual asset exported successfully as 'baby_name_trends.png'")
    plt.show()
    
   
# 4. POPULARITY ANALYSIS (Task 3)
    
    print("\n--- Analyzing Top Tier Naming Trends ---")
    
    # Isolate the top 100 entries by volume
    top_entries = master_df.sort_values(by='Count', ascending=False).head(100)
    
    # Group by name to find the most dominant names in the Top 100 tier
    top_names = top_entries.groupby('Name')['Count'].sum().sort_values(ascending=False)
    
    print("Ranked Leaderboard (Top 10 Most Frequent Names):")
    print("-" * 45)
    print(top_names.head(10))