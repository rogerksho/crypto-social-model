# crypto-social-model
this is a model that aims to predict bitcoin price changes based on twitter sentiments and google trends (pertinent data/data crawlers also included).

## summary
with a regression problem at hand and only two features to work off, I considered the following models:
- support vector regression
- bayesian ridge regression
- elasticnet
- ordinary least squares

as expected, the ordinary least squares method yielded the most errors and was quickly scrapped. moving along with the first three models, I trained it on data on these date ranges:
> since: 2016-04-01

> before: 2020-02-26

and tested it on these date ranges:
> since: 2020-02-27

> before: 2020-09-13

***note:*** the 2021 data was mostly left out due to the massive spikes in bitcoin prices (which were due to causes way larger in magnitude than what our features can capture), which would indubitably introduce quite a bit of noise into the training data/testing data. 

## evaluation
the prediction results can be visualised in the pyplot below:
![prediction_image](https://i.ibb.co/8sLhP6g/test.png)

note that bayesian ridge regression predictions lie almost coincidentally with the elasticnet regression predictions - this is no surprise as bayesian ridge regressoin (L2 penalty) is a special case of elasticnet (L1 and L2 penalty).

just by looking at the plot, you can see clearly that the regression models fail to capture the long-term growth of bitcoin - it seems to hover around a near horizontal "asymptote". however, it seems to be more fit at singling out shorter-term changes, highlighted below:
![prediction_annotated](https://i.ibb.co/Dw6h9xz/test.png)

## todo
this model is just a rough draft - many optimizations can be made, especially in the hyperparameters of bayesian ridge regression and elasticnet regression. in a concise list, some possible areas of improvement include:
- BR, elasticnet hyperparameter optimization
- continual learning
- comparison with NN learning (keras)
- VAR modelling
- data for different coins

***
## resources
1. [The Predictor Impact of Web Search Media On Bitcoin Trading Volumes](https://www.researchgate.net/publication/282152077_The_Predictor_Impact_of_Web_Search_Media_On_Bitcoin_Trading_Volumes?enrichId=rgreq-c494c8d5f7b6e38d18a5c6d1c93ee872-XXX&enrichSource=Y292ZXJQYWdlOzI4MjE1MjA3NztBUzoyNzc1NTM1NTk0MjUwMjdAMTQ0MzE4NTMzMzgzOA%3D%3D&el=1_x_2&_esc=publicationCoverPdf)
2. [Advanced sentiment analysis of social media for short-term cryptocurrency price prediction](https://www.researchgate.net/publication/337442647_Advanced_social_media_sentiment_analysis_for_short-term_cryptocurrency_price_prediction)
