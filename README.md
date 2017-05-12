### Twitter Sentiment Analysis - Chilean Spanish

Sentiment Analysis is the process of ‘computationally’ determining whether a piece of writing is positive, negative or neutral. It’s also known as opinion mining, deriving the opinion or attitude of a speaker.

This repository contains the code to do sentiment analysis on Tweets, but not any tweets, Chilean Spanish tweets! Any of you familiar with chilean spanish knows that Chileans speak there own special flavor of very incorrect spanish.

What are we using?
* Python 2.7
* [Tweepy](https://github.com/tweepy/tweepy) 

What do we need to do?
1. Open a streaming and record the tweets about a certain topic, username, location, etc. [1_streaming.py](https://github.com/17-56cl/sentiment_analysis_chileanTweets/blob/master/1_streaming.py)
2. Do the sentiment analysis on them, i.e. classify them on negative, positive or neutral. For english text, you have multiple packages to do so, for example [NLKT](http://www.nltk.org/howto/sentiment.html). But for spanish, we havent been able to find any good pre-built analyzer. So we will have to build it ourselves! 

 * From the tweets we have been streaming, we hace to select a training sample, let's say 5,000 tweets.

 * We have many ways to do the sentiment analysis. One is building a list of "negative" words and a list of "positive" words, using the training sample as guide, then we tokenize the tweets and we get an indicator of positive vs negative words. The second one consists in simply classifying (by hand :expressionless:) the training sample of tweets in negative, neutral and positive. Then, we use this sample to train a machine learning algorithm to determine the sentiment of a tweet. 

We are ready with step 1., recording tweets about presidential elections in Chile around the clock. Fot step 2, we will be uploading our progress. 
