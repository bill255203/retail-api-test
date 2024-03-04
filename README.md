# **TechOrange Retail README**

## **Overview**

This project is designed to assist TechOrange by transforming and uploading CSV data into Google Cloud Storage and subsequently transferring it to BigQuery. The transformation process adapts user event and product data into a format suitable for Google Retail, facilitating further analysis and recommendation generation. This document provides a comprehensive guide on how to use the provided Python scripts (**`userEvent.py`**, **`product.py`**, **`gcs2bq.py`**) and how to perform operations such as data transformation, uploading to Google Cloud Storage, and data transfer to BigQuery.

## **Prerequisites**

Before you begin, ensure you have the following:

- Python 3.x installed on your system.
- Google Cloud SDK installed and configured for your Google Cloud account.
- Access to Google Cloud Storage and BigQuery.
- The userEvent and product file(s) that you intend to process.

## **Setup Instructions**

1. **Clone the Repository**: Clone this repository to your local machine to get started.

   ```
   git clone [repository URL]
   cd [repository directory]

   ```

2. **Google Cloud SDK Configuration**: Make sure your Google Cloud SDK is configured to access your project.

   ```
   gcloud auth login
   gcloud config set project [YOUR_PROJECT_ID]

   ```

## How To Use

1. **Prepare the Data**: Place your `.csv` files in the root directory of the cloned project.
2. **Transform Data**:

   - Ensure your filename matches the one in the `userEvent.py` script. If your filename is `techorange-pageview-202401.csv`, update the script accordingly:

     ```python
     csv_data = pd.read_csv('techorange-pageview-202401.csv', encoding='utf-8')

     ```

   - Run `userEvent.py` to transform user event data:

     ```
     python userEvent.py

     ```

   - Similarly, ensure your filename matches the one in the `product.py` script. If your filename is `techorange-postmeta-20240206.csv`, update the script accordingly:

     ```python
     csv_data = pd.read_csv('techorange-postmeta-20240206.csv', encoding='utf-8')

     ```

   - Run `product.py` to transform product data:

     ```
     python product.py

     ```

3. **Upload to Google Cloud Storage**: Follow the instructions in the `techorange retail README` to manually upload the transformed data to your Google Cloud Storage bucket.

   - Inside your Google Cloud Storage bucket, locate and click the "Upload Files" button to start the upload process.
   - Navigate through your local file system to find the JSON files you prepared earlier.
   - Select the JSON files you intend to upload to the bucket.

4. **Download Service Account Key**: Refer to the `techorange retail README` for detailed instructions on setting up authentication.

   - Navigate to the IAM & Admin tab in the Google Cloud Console and click on Service Accounts.
   - Find the service account that has the necessary GCS read and BigQuery write permissions.
   - Click on Keys next to the desired service account.
   - Click on Add Key and choose Create New Key.
   - When prompted, select JSON as the key type. The JSON key file will be downloaded to your local download section.
   - Move the JSON file into the project's root directory for authentication purposes.

5. **Transfer to BigQuery**:

   - Before executing `gcs2bq.py`, check if the first few lines match the correct settings for your project, bucket, and dataset:

     ```python
     # Example usage
     project_id = 'example-project'
     gcs_bucket_name = 'techorange'   # Source
     bq_dataset_id = 'techorange'     # Destination

     ```

   - Set the source and destination table names correctly:

     ```python
     source_product = 'product.json'      # Source file name
     table_id_product = 'products'        # Destination table name

     source_user_event = 'userEvent.json' # Source file name
     table_id_user_event = 'userEvents'   # Destination table name

     ```

   - Execute `gcs2bq.py` to transfer data from Google Cloud Storage to BigQuery:

     ```
     python gcs2bq.py

     ```

6. **Verification**: Check the BigQuery console to verify that the tables are created correctly.

7. **Model Creation & Serving Config**: For creating the model and serving configuration, refer back to the `techorange retail README` file.

  (a) **Model Creation**: Follow these steps to set up a new model in Google Retail.

  - Go to the Google Retail platform and access the "Models" section.
  - Click on “Create Model” and input a name for your new model.
  - Select "Others you may like" for the model type and finalize creation with additional custom settings as needed.

  (b) **Serving Configuration**: Set up configurations to serve the model.

  - In the "Serving Configurations" section, click “Create Serving Config”.
    Keep the type as Recommendation, provide a config name, and continue without serving controls.
  - Select the created model to include and configure additional parameters if necessary.

8. **Recommendation Generation**:
   - Find an example CURL request and the corresponding code in the `curl.sh` file for generating recommendations.
   - Use the CURL request to generate a sample recommendation from the model:
     by pasting the CURL request into the terminal to receive recommendations
