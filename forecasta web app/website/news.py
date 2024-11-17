from flask import Blueprint, render_template, flash, redirect, url_for
import requests
import pg8000
import json
from pandas import json_normalize
import pandas as pd

fin_news = Blueprint('fin_news',__name__)

@fin_news.route('/fin_news', methods=['GET'])
def time_series():
    url=""
    return
