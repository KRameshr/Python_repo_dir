import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from scipy.cluster.vq import kmeans, vq, whiten
import os

# --- 1. DATA GENERATION & STORAGE ---
def prepare_data():
    data_dict = {
        'mpg': [21.0, 21.0, 22.8, 21.4, 18.7, 18.1, 14.3, 24.4, 22.8, 19.2, 17.8, 16.4, 17.3, 15.2],
        'cyl': [6, 6, 4, 6, 8, 6, 8, 4, 4, 6, 6, 8, 8, 8],
        'disp': [160.0, 160.0, 108.0, 258.0, 360.0, 225.0, 360.0, 146.7, 140.8, 167.6, 167.6, 275.8, 275.8, 275.8],
        'hp': [110, 110, 93, 110, 175, 105, 245, 62, 95, 123, 123, 180, 180, 180],
        'drat': [3.90, 3.90, 3.85, 3.08, 3.15, 2.76, 3.21, 3.69, 3.92, 3.92, 3.92, 3.07, 3.07, 3.07],
        'wt': [2.620, 2.875, 2.320, 3.215, 3.440, 3.460, 3.570, 3.190, 3.150, 3.440, 3.440, 4.070, 3.730, 3.780],
        'qsec': [16.46, 17.02, 18.61, 19.44, 17.02, 20.22, 15.84, 20.00, 22.90, 18.30, 18.90, 17.40, 17.60, 18.00],
        'vs': [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0],
        'am': [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'gear': [4, 4, 4, 3, 3, 3, 3, 4, 4, 4, 4, 3, 3, 3],
        'carb': [4, 4, 1, 1, 2, 1, 4, 2, 2, 4, 4, 3, 3, 3]
    }
    df = pd.DataFrame(data_dict)
    df.to_excel('somecars1.xlsx', index=False)
    print("Step 1: Data successfully exported to 'somecars1.xlsx'")
    return df

# --- 2. ANALYTICAL PIPELINE ---
def run_analysis():
    # Load data
    if not os.path.exists('somecars1.xlsx'):
        df = prepare_data()
    else:
        df = pd.read_excel('somecars1.xlsx')

    # Normalize/Whiten the data
    # (Removes unit bias between large numbers like 'disp' and small ones like 'wt')
    whitened_data = whiten(df)

    # Apply K-Means Clustering (k=3)
    # centroids = mean of clusters; distortion = sum of squared differences
    centroids, distortion = kmeans(whitened_data, 3)

    # Assign each observation to a cluster
    df['cluster_group'], _ = vq(whitened_data, centroids)

    return df, centroids

# --- 3. VISUALIZATION ---
def plot_clusters(df):
    plt.figure(figsize=(10, 6))
    
    # Define aesthetic mapping
    # Note: Cluster numbers (0,1,2) might shift based on random initialization
    cluster_info = {
        0: {'color': 'red', 'label': 'Segment A'},
        1: {'color': 'blue', 'label': 'Segment B'},
        2: {'color': 'green', 'label': 'Segment C'}
    }

    for group in range(3):
        subset = df[df['cluster_group'] == group]
        plt.scatter(subset['hp'], subset['mpg'], 
                    c=cluster_info[group]['color'], 
                    label=cluster_info[group]['label'], 
                    s=150, edgecolors='white', alpha=0.8)

    plt.title('SciPy Cluster Analysis: Horsepower vs Efficiency', fontsize=14)
    plt.xlabel('Horsepower (hp)')
    plt.ylabel('Miles Per Gallon (mpg)')
    plt.legend(title="Car Category")
    plt.grid(True, linestyle='--', alpha=0.5)
    
    plt.savefig('cluster_results.png')
    print("Step 2: Visualization saved as 'cluster_results.png'")
    plt.show()

# --- EXECUTION ---
if __name__ == "__main__":
    processed_df, final_centroids = run_analysis()
    
    print("\n--- Cluster Summary ---")
    print(processed_df.groupby('cluster_group')[['mpg', 'hp', 'wt']].mean())
    
    plot_clusters(processed_df)
    
    # Final Export
    processed_df.to_excel('final_car_clusters.xlsx', index=False)
    print("\nProject Complete. Final results available in 'final_car_clusters.xlsx'")