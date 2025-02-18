#!/usr/bin/env python3

from flask import Flask, request, render_template

app = Flask(__name__,template_folder='./frontend/templates',static_folder='./frontend/static')

@app.route("/")
def main():
    return render_template('index.html')

    # return '''
    #  <form action="/echo_user_input" method="POST">
    #      <input name="user_input">
    #      <input type="submit" value="Submit!">
    #  </form>
    #  '''

@app.route("/echo_user_input", methods=["POST","GET"])
def echo_input():
    text = request.form.get("user_input", "")
    return render_template('echo_input.html',input_text=text)