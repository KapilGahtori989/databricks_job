import dlt

@dlt.table(
    name = "bronze_products",
    comment = "Raw products ingested using AutoLoader"
)
def bronze_orders():
    return (
        spark.readStream.format("cloudFiles")
        .option("cloudFiles.format", "json")
        .option("multiline","true")
        .load("/Volumes/learning_spark_sql/ecommerse_data/products_raw")
    )



