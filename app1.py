df=spark.read.csv("data.csv", header=True, inferSchema=True)

df2 = df.select("column1", "column2")
df2.write.parquet("data.parquet")