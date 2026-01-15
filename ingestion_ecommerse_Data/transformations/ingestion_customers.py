import dlt

@dlt.table(
    name = "bronze_customers",
    comment = "Raw customers ingested using AutoLoader"
)
def bronze_orders():
    return (
        spark.readStream.format("cloudFiles")
        .option("cloudFiles.format", "json")
        .option("multiline","true")
        .load("/Volumes/learning_spark_sql/ecommerse_data/customers_raw")
    )



