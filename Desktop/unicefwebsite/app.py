from flask import Flask, render_template, request, session, redirect

@app.route("index.html")
def index():
    return render_template("index.html")