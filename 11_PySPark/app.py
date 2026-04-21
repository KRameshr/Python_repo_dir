from pyspark import SparkContext
sc = SparkContext("local","FistName")
sc.stop()
print(sc)