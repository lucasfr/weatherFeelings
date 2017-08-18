# weatherFeelings

The idea is to:

* Identify your location
* Get the latest tweets with hashtag #weather near location using twitter api
* Use a sentiment analysis tool e.g. Python NLTK to analyse the tweets 
* Display: current weather, public mood and animated GIF
* Options to tweet the result or save results to database (possibly with interval)

![alt text](https://raw.githubusercontent.com/lucasfr/weatherFeelings/master/docs/img/weatherfeelings-diagram.png)  

**Create Virtual Environment**

```virtualenv venv```

Source:

```source venv/bin/activate```

Install requirements:

```pip install -r requirements.txt```

run file 'app.py' (not currently working) and open your browser localhost:5000