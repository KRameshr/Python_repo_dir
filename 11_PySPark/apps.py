# from pyspark.conf import SparkConf
# from pyspark.context import SparkContext
# conf = SparkConf().setAppName("PySpark Demo App").setMaster("local[2]")

# print(conf.get("spark.master"))
# print(conf.get("spark.app.name"))

import os
from pyspark import SparkContext, SparkConf

# 1. Setup the Configuration and Context
conf = SparkConf().setAppName("Vogue-Data-Extraction").setMaster("local[2]")
sc = SparkContext(conf=conf)

# 2. Define the path (Use 'r' for raw string to avoid path errors)
path = os.path.join(r"C:\Users\ramesh\OneDrive\Desktop\Python\10_Web_Scraping\Wikipedia_web_Scraping", "asia_area_analysis.csv")

# 3. Add the file to Spark
sc.addFile(path)

print("File successfully added to Spark nodes!")