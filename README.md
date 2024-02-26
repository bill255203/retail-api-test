# **Retail API Testing Project README**

## **Overview**

This project is designed to facilitate Retail API testing by generating fake data for various scenarios including product data, user events on different pages, and prediction queries. The project consists of Python scripts for data generation, JSON files for storing the generated data, and a text file with an example of a successful prediction format.

## **How To Use**

To use the scripts and generate data:

1. Run **`products.py`** to generate the product catalog data:

   ```
   python products.py

   ```

2. Generate user event data - detail page by running:

   ```
   python userEvents-detailpage.py

   ```

- Use **`predict.json`** for testing prediction queries and refer to **`predictCurl.txt`** for the correct format of a successful prediction request.

## **Must Read: EventFlow Details**

Path 1: SEARCH event -> DETAIL-PAGE-VIEW event -> ADD-TO-CART event -> PURCHASE event
Path 2 : SEARCH event -> ADD-TO-CART event -> PURCHASE event

If event timestamps are jumbled, then they will be discarded by the AI model during model training, which will in-turn affect the search performance. AI model trains on these events for CTR optimisation and on SEARCH events and the subsequent DETAIL-PAGE-VIEW events i.e. every DETAIL-PAGE-VIEW event must be traceable to a SEARCH event product-id list. This is what counts as “search impressions”

```
https://medium.com/google-cloud/gcp-retail-search-onboarding-best-practices-for-user-events-part-2-4-393f3d778e1f
```

It also talks about detecting and handling bot traffic and handling cached search results outside of the retail api for best practices

## **Conclusion**

This project aims to streamline the process of testing and demonstrating the capabilities of the Retail API through the use of generated fake data. It covers various aspects of retail interactions, from browsing and interaction to purchase and prediction, providing a comprehensive toolkit for API testing.

## **How To Delete Data**

```
{
   "filter": "eventTime > \"2020-01-01T00:00:00Z\" AND eventTime < \"2024-03-01T00:00:00Z\"",
   "force": true
}
```

1. **Data Preparation:**
   - Raw data from various sources (e.g., databases, CSV files) is collected and preprocessed.
   - Data is transformed to conform to the Google Products format, ensuring consistency and compatibility with the retail API.
2. **Event Sequencing:**
   - Implement logic to ensure that user events follow the recommended sequence for best practices:
     - **SEARCH Event:** User initiates a search.
     - **DETAIL-PAGE-VIEW Event:** User views the details page of a specific item from the search results.
     - **ADD-TO-CART Event:** User adds the viewed item to their cart.
     - **PURCHASE Event:** User completes the purchase of the item.
   - Validate and enforce event sequencing to optimize the effectiveness of the AI models trained on this data.
3. **Data Ingestion:**
   - Ingest prepared data into the retail API, ensuring proper mapping and alignment with product attributes and user events.
4. **Model Selection:**
   - Choose appropriate AI models based on specific page functionalities within the e-commerce website:
     - **Home Page:**
       - Implement a "Recommendation for You" model to personalize product recommendations based on user behavior and preferences.
     - **Shopping Cart Page:**
       - Deploy a "Frequently Bought Together" model to suggest complementary products that users commonly purchase together with items in their cart.
     - **Product Out of Stock Page:**
       - Utilize a "Similar Items" model to recommend alternative products that are similar to the out-of-stock item, ensuring a seamless shopping experience for users.
   - Configure and fine-tune each model to optimize performance and relevance based on user interactions and feedback.
5. **Integration and Testing:**
   - Integrate AI models seamlessly into the e-commerce website's backend infrastructure.
   - Conduct thorough testing to ensure proper functionality, accuracy, and responsiveness of the recommendation system across different pages and user scenarios.
6. **Monitoring and Optimization:**
   - Implement monitoring tools to track key performance metrics (e.g., click-through rates, conversion rates) and user engagement with recommended products.
   - Continuously analyze data and user feedback to refine and optimize AI models, improving recommendation accuracy and user satisfaction over time.
