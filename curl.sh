curl -X POST \ 
-H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
  -H "x-goog-user-project: tw-rd-de-bill-404606" \ 
-H "Content-Type: application/json; charset=utf-8" \
  --data '{       
  "userEvent": {                  
    "eventType": "home-page-view",                      
    "visitorId": "626d2871-ad9c-4374-9ad0-e40586e96138",
    "userInfo": {                                      
      "userId": "35acc714-a65f-43ed-bed7-1de8b6a7cf67",
      "ipAddress": "69.87.138.134",                                             
      "userAgent": "Mozilla/5.0 (compatible; MSIE 6.0; Windows 95; Trident/4.1)"
    }
  },             
  "pageSize": 10,                   
  "filter": "filterOutOfStockItems",
  "params": {             
    "returnProduct": true, 
    "strictFiltering": true
  }          
}' \
  https://retail.googleapis.com/v2/projects/tw-rd-de-bill-404606/locations/global/catalogs/default_catalog/servingConfigs/recently_viewed_default:predict

{
  "attributionToken": "ChM4MTM1Njk1MjQ0NDQ2NTI2MTYzEA0aAlJWIgJSVigA"
}

# example request

curl -X POST \
  -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
  -H "x-goog-user-project: tw-rd-de-bill-404606" \
  -H "Content-Type: application/json; charset=utf-8" \
  --data '{
  "userEvent": {
    "eventType": "detail-page-view",
    "visitorId": "visitor123",
    "eventTime": "2024-03-01T15:30:00Z",
    "userInfo": {
      "userId": "user123",
      "ipAddress": "203.0.113.0",
      "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    },
    "productEventDetail": {
      "productDetails": [
        {
          "id": "33738",
          "title": "AI人工智能,儲存,雲端",
          "attributes": {
            "categories": ["雲端儲存"],
            "tags": ["Google","NVIDIA","雲端"]
          }
        }
      ]
    }
  }
}' \
  https://retail.googleapis.com/v2/projects/tw-rd-de-bill-404606/locations/global/catalogs/default_catalog/servingConfigs/recently_viewed_default:predict
