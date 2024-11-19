from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from datetime import datetime
import requests
import pg8000

pipe_fin_data = Blueprint("pip_fin_data",__name__)


@pipe_fin_data.route('/home', methods=['GET'])
def Display_data():

    return


