# prediction_engine
> this repo shows how to get the prediction result by post request to the server.

# usage
* run [post.py](https://github.com/raita0100/prediction_engine/blob/master/post.py) in your local machine to get result.
* *you can also edit :pencil: the list of stock file according to your use.* </br>
```querystring = {"0":"GOOGL","1":"AAPL","2":"AMZN","3":"SBUX","4":"NFLX","5":"FB"}```

# info
1. Program make the post request to the target url to get the result.
2. The result will be of form JSON :point_down:
```
{
  "AAPL": ["APPLE", "SELL"],
  "AMZN": ["AMAZON", "BUY"],
  "FB": ["FACEBOOK", "SELL"],
  "GOOGL": ["GOOGLE", "BUY"],
  "NFLX": ["NETFLIX", "BUY"],
  "SBUX": ["STARBUCKS", "BUY"]
}
```
