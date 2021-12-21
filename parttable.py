from google.cloud import bigquery
client = bigquery.Client()
project = client.project
dataset_ref = bigquery.DatasetReference(project, 'DB_FRESHERS_02')

table_ref = dataset_ref.table("my_partitioned_table1000")
schema = [
    bigquery.SchemaField("name", "STRING"),
    bigquery.SchemaField("join_date", "DATE"),
    
]
table = bigquery.Table(table_ref, schema=schema)
table.time_partitioning = bigquery.TimePartitioning(
    type_=bigquery.TimePartitioningType.DAY,
    field="join_date",  # name of column to use for partitioning
    expiration_ms=7776000000,
)  # 90 days

table = client.create_table(table)

print(
    "Created table {}, partitioned on column {}".format(
        table.table_id, table.time_partitioning.field
    )
)