import pandas as pd
import numpy as np
# Now Python will find the real SciPy library instead of your file!
from scipy.cluster.vq import kmeans, vq, whiten

# 1. Create Data
data_dict = {
    'mpg': [21.0, 21.0, 22.8, 21.4, 18.7],
    'hp': [110, 110, 93, 110, 175],
    'wt': [2.62, 2.87, 2.32, 3.21, 3.44]
}
df = pd.DataFrame(data_dict)

# 2. Clustering Logic
whitened_data = whiten(df)
centroids, _ = kmeans(whitened_data, 2)
idx, _ = vq(whitened_data, centroids)

print("Cluster Assignments:", idx)