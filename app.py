#importing libraries
from flask import *
import json
import Stock_Direction as sd

app = Flask(__name__)

#defining the companies for stock
_companys = {
    "FB": "FACEBOOK",
    "AAPL": "APPLE",
    "AMZN": "AMAZON",
    "NFLX": "NETFLIX",
    "GOOGL": "GOOGLE",
    "SBUX": "STARBUCKS",
    "XOM": "EXXON MOBILE",
    "JNJ": "JHONSON & JHONSON",
    "BAC": "BANK OF AMERICA",
    "GM": "GENARAL MOTORS"
    }
#route web page to log in
@app.route("/", methods = ['GET','POST'])
def index():
    dict_of_items = None
    if request.is_json:
        dict_of_items = request.get_json()
    else:
        dict_of_items = request.args.to_dict()

    #dict_of_items = {0:"GOOGL", 1:"NFLX", 2:"AMZN"}
    #print("\n\npost_request:\n {}\n\n".format(str(dict_of_items)))
    x = {}
    for i in dict_of_items.keys():
        x[dict_of_items[i]] = [_companys[dict_of_items[i]]]

    #print("\n\ninitial x :\n {}\n\n".format(str(x)))

    #get prediction from backend for next day stocks
    f_pred = sd.main_function(ticker_list=list(x.keys()))
    f_pred = dict(f_pred)

    #print("\n\nprediction :\n {}\n\n".format(str(f_pred)))

    for key in f_pred.keys():
        x[key].append(f_pred[key])

    #print("\n\nafter x :\n {}\n\n".format(str(x)))

    return jsonify(x)


if __name__ == "__main__":
    #app.debug = True
    app.run()
    #app.run(debug=True)
