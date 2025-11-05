from pyspark.sql import SparkSession
from pyspark.sql.functions import col, upper, avg

# Step 1: Create Spark Session
spark = SparkSession.builder \
    .appName("Basic PySpark Example") \
    .getOrCreate()

# Step 2: Read CSV file
df = spark.read.option("header", True).csv("employees.csv")

# Step 3: Data Transformation
# Convert name column to uppercase and filter records with salary > 50000
transformed_df = df.withColumn("EMP_NAME", upper(col("name"))) \
                   .filter(col("salary") > 50000)

# Step 4: Group by department and calculate average salary
avg_salary_df = transformed_df.groupBy("department").agg(avg("salary").alias("avg_salary"))

# Step 5: Write output to a new CSV file
avg_salary_df.write.mode("overwrite").option("header", True).csv("output/avg_salary")

# Step 6: Stop Spark session
spark.stop()
