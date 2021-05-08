# Shipment Status
App based on [FastApi] used to predict shipment delay status based on features like `Customer care calls`, `Customer rating`, etc
[View Demo](https://shipment-status-prediction.herokuapp.com/docs#/default/home__get)


## Table of contents
* [Introduction]
* [Problem statement]
* [Features used for prediction]     (#features-used-for-prediction)
* [Model deployment]
* [Getting Started](#getting-started)
    * [Steps to setup project]     (#steps-to-setup-project)
* [Usage](#usage)
* [Contributing](#contributing)
* [Resources](#resources)

## Introduction
The dataset used is of Product Shipment Tracking
Link: https://www.kaggle.com/prachi13/customer-analytics

## Problem statement
To build a classification model that predicts whether a shipment will be delayed or not. The target variable is 'Reached.on.Time_Y.N'.

## Factors used for prediction
* `Customer care calls`
* `Customer rating`
* `Cost of the Product`
* `Prior purchases`
* `Discount offered`
* `Weight in gms`

## Model deployment 
The shipment prediction model was deployed using 
* FastApi web framework for building APIs 
* Uvicorn for ASGI server implementation
Docker Container was used to package the application environment 

## Getting Started

### Steps to setup project
1. Clone the repo
`git clone https://github.com/aditib47/Shipment_status.git`
2. Run `docker build` for building the project
3. Run `docker run` to start the app locally

## Usage
Please use the [/predict](https://shipment-status-prediction.herokuapp.com/docs#/default/predict_shipment_predict_post) endpoint with following parametes to get the shipment status

```
{
  "Customer_care_calls": xx,
  "Customer_rating": xx,
  "Cost_of_the_Product": xx,
  "Prior_purchases": xx,
  "Discount_offered": xx,
  "Weight_in_gms": xx
}
```

## Contributing
Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## Resources
* [FastApi](https://fastapi.tiangolo.com/)
* [numpy](https://numpy.org/)
* [Heroku](https://www.heroku.com/)
* [scikit-learn](https://scikit-learn.org/stable/)
