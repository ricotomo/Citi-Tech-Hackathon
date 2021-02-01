![Univest](https://s3-alpha-sig.figma.com/img/70f0/95bf/2377c988ae05f61c4a266c9774e0441d?Expires=1612742400&Signature=GkAgtGMTwcFDQohv0INksUi60trNZ89Fy2IfhRWFqP-TtBQXyikO8uZ6Q-duo-HuB2WqD3H2UBZnhKsgiym-rviz7L3dczkhoSlq4vDVQiAXuSmI1eOLxn1Fn25Vz~KQwUO~F9aqQ3vM6QfQxR7-FHsG9D3gWENBaWLZ5exx7-7wkXXe8G19FCWCgs84OreFvGhbuUVelWmpoTtsElVbmJBQYlga3RIq59~6q~Oj-zbO763mWCKfq6qyWFGNWMevDpsLqG-CVg-03ALy77v55kLeknbFQ5zCdtxIZL-5RKfZQFtAvSb5CGGKkdjtTYJ4uuwhdON1i1qBOV2Lty7XNw__&Key-Pair-Id=APKAINTVSUGEWH5XD5UA)

## About
Submission for the Jan 2021 Citi Tech Hackathon. Univest is a two-sided marketplace for Income Share Agreements (ISAs). Students sign up and indicate how much money they need for tuition, then they get offers from investors and choose the best one. Investors submit offers to fund the ISA. They can expect extremely low risk and medium to high returns. ​

In our MVP students can create a request for an ISA. This is posted to our backend and stored in a SQLite DB. Our machine learning algorithms then go to work calculating the expected yearly ROI over a 10 year timespan after graduation. Investors can search for this ISA requests and see the expected ROI. 

![](PredictROI.gif)

## Built With
* Python
* Flask
* Bootstrap
* SQLite  
* Azure
* Linear Regression
* Lasso
* Ridge Regression
* Random Forest
* XGBoost
* Artificial Neural Network

## Dependencies
* Install requirements with "pip install -r requirements.txt"

## Links
Figma clickdummy: https://www.figma.com/proto/Qtv7IkeX6LmxaycgjtDRTP/Citi-ISA?node-id=23%3A2&scaling=min-zoom                                            
Pitchdeck: https://1drv.ms/p/s!Ai_wUCcxJ4B3kg7p5wT6JvKF4ckJ?e=PjSoS5  
Data analytics branch readme: https://github.com/ricotomo/Citi-Tech-Hackathon/tree/data_analytics  
(for a breakdown of how we built and trained a model, tested ML algorithms, and calculate our predictions)

## Contributors

#### [@ricotomo](https://github.com/ricotomo)
#### [@hayuh](https://github.com/hayuh)
#### [@jessmoody](https://github.com/jessmoody)
#### [@HexuanZhang-DS](https://github.com/HexuanZhang-DS)
#### [@BigJonP](https://github.com/BigJonP)
