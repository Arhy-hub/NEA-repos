from flask import Blueprint, render_template, request, flash, redirect, url_for

views = Blueprint('views', __name__)

@views.route('/home')
def home():
    return "<p>This is the home page<p>"

