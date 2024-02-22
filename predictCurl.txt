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