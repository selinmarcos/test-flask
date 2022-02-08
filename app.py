import flask
from flask import request
import pandas as pd
from datetime import datetime as dt

# data = pd.read_csv('data.csv', names=['s', 'e', 'm']).set_index('m')

# series = pd.Series(index=range(data.s.min(), dt.now().year + 1))
# for m in data.index:
#     series.loc[data.loc[m].s:data.loc[m].e] = m

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    fecha = int(request.args['fecha'])
    try:
        return fecha
    except KeyError:
        return "INVALID"
