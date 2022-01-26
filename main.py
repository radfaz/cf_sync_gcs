from google.cloud import storage
import os

def stage_file(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    file = event
    target_bucket = os.environ.get("BUCKET_NAME")
    print(f"Processing file: {file['name']}.")
    storage_client = storage.Client()
    source_bucket = storage_client.bucket(file['bucket'])
    source_blob = source_bucket.blob(file['name'])
    destination_bucket = storage_client.bucket(target_bucket)

    blob_copy = source_bucket.copy_blob(
        source_blob, destination_bucket
    )