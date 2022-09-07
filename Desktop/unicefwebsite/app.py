import os
from flask import Flask, render_template, request, session, redirect
from flask_session import Session
from functools import wraps
from cs50 import SQL
from werkzeug.security import check_password_hash, generate_password_hash
import psycopg2
from flask_mail import Mail, Message


app = Flask(__name__)


@app.route("/index.html")
def index():
    return render_template("index.html")