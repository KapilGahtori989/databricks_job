import dlt

@dlt.table(
    name = "bronze_orders",
    comment = "Raw orders ingested using AutoLoader"
)
def bronze_orders():
    return (
        spark.readStream.format("cloudFiles")
        .option("cloudFiles.format", "json")
        .option("multiline","true")
        .load("/Volumes/learning_spark_sql/ecommerse_data/orders_raw")
    )



