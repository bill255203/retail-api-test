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

   ```bash
   bashCopy code
   git clone [repository URL]
   cd [repository directory]

   ```

2. **Install Dependencies**: Install the necessary Python libraries.

   ```
   Copy code
   pip install -r requirements.txt

   ```

3. **Google Cloud SDK Configuration**: Make sure your Google Cloud SDK is configured to access your project.

   ```
   gcloud auth login
   gcloud config set project [YOUR_PROJECT_ID]

   ```

## **How To Use**

1. **Prepare the Data**: Place your **`.csv`** files in the root directory of the cloned project.
2. **Transform Data**:
   - Run **`userEvent.py`** to transform user event data.
     ```
     Copy code
     python userEvent.py

     ```
   - Run **`product.py`** to transform product data.
     ```
     Copy code
     python product.py

     ```
3. **Upload to Google Cloud Storage**: Follow the instructions prompted by the scripts or manually upload the transformed data to your Google Cloud Storage bucket.
4. **Transfer to BigQuery**:
   - Execute **`gcs2bq.py`** to transfer data from Google Cloud Storage to BigQuery.
     ```
     Copy code
     python gcs2bq.py

     ```
5. **Verification**: Use the provided screenshots in the documentation to verify the correct setup and data transfer. For further data manipulation and query execution, refer to the BigQuery documentation.
6. **Recommendation Generation**: A curl request example and the corresponding code can be found in the **`curl.txt`** file for generating recommendations.

## **How To Delete Data**

```
{
   "filter": "eventTime > \"2020-01-01T00:00:00Z\" AND eventTime < \"2024-03-01T00:00:00Z\"",
   "force": true
}
```
