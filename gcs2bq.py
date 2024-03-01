from google.cloud import bigquery
from google.cloud.exceptions import NotFound

# Example usage
project_id = 'tw-rd-de-bill-404606'
gcs_bucket_name = 'techorange'   #source
bq_dataset_id = 'techorange'        #destination

source_product = 'product.json'   #source file name
table_id_product = 'products'     #destination table name

source_user_event = 'userEvent.json'   #source file name
table_id_user_event = 'userEvents'     #destination table name
def recreate_table(client, project_id, dataset_id, table_id, schema=None):
    """
    Deletes the table if it exists and creates a new one.
    
    Args:
    client (bigquery.Client): BigQuery client.
    project_id (str): BigQuery project ID.
    dataset_id (str): BigQuery dataset ID.
    table_id (str): BigQuery table ID.
    schema (list, optional): Schema of the table to be created. Defaults to None.
    """
    dataset_ref = client.dataset(dataset_id, project=project_id)
    table_ref = dataset_ref.table(table_id)
    
    try:
        client.delete_table(table_ref)  # Attempt to delete the table.
        print(f"Table {dataset_id}.{table_id} deleted.")
    except NotFound:
        print(f"Table {dataset_id}.{table_id} not found, creating a new one.")
    
    # Create a new table
    table = bigquery.Table(table_ref, schema=schema)
    client.create_table(table)
    print(f"Table {dataset_id}.{table_id} created.")

def load_json_from_gcs_to_bigquery(bucket_name, source_blob_name, project_id, dataset_id, table_id):
    """
    Loads a JSON file from Google Cloud Storage into a BigQuery table,
    replacing the table if it exists.
    
    Args:
    bucket_name (str): Name of the GCS bucket where the JSON file is stored.
    source_blob_name (str): Name of the JSON file in the GCS bucket.
    dataset_id (str): BigQuery dataset ID where the table is located.
    table_id (str): BigQuery table ID where the data will be loaded.
    """
    client = bigquery.Client()
    
    # Recreate the table
    recreate_table(client, project_id, dataset_id, table_id)
    
    # Now proceed with loading data into the new table
    table_ref = client.dataset(dataset_id).table(table_id)
    job_config = bigquery.LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
    job_config.autodetect = True  # Automatically infer the schema
    
    uri = f"gs://{bucket_name}/{source_blob_name}"
    
    load_job = client.load_table_from_uri(
        uri,
        table_ref,
        job_config=job_config
    )  # Make an API request.
    
    load_job.result()  # Waits for the job to complete.
    
    print(f"Loaded {load_job.output_rows} rows into {dataset_id}:{table_id}.")

load_json_from_gcs_to_bigquery(gcs_bucket_name, source_product, project_id, bq_dataset_id, table_id_product)
# load_json_from_gcs_to_bigquery(gcs_bucket_name, source_product, project_id, bq_dataset_id, table_id_product)
