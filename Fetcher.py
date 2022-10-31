from email.base64mime import body_decode
from logging import exception
from pickle import NONE
from xml.dom.minidom import Element
from flask import Flask, jsonify, request
import pika
import uuid
from Fetcher_Connect import send_to_rmqServer
from flask import json,render_template
from werkzeug.exceptions import HTTPException

app = Flask(__name__,template_folder='templateFiles', static_folder='staticFiles')

@app.errorhandler(HTTPException)
def handle_exception(e):
    
    return render_template('index.html')

@app.route("/option3", methods=['GET', 'POST'])
def option3():
        args = request.args
        start = args.get('start')
        end = args.get('end')
        msg = start+'-'+end
        result = send_to_rmqServer(msg)
        msg = f"Perfect numbers in range {start}-{end} is:"+ result
        return  jsonify(msg)

@app.route("/option2", methods=['GET', 'POST'])
def option2():
    result = send_to_rmqServer(-1)
    msg = f" (exist perfect numbers, Count Of exist Perfect number )  "+ result
    
    return jsonify(msg)

@app.route("/option1", methods=['GET', 'POST'])
def option1():
    args = request.args
    print(args)
    number = args.get('number')
    result = send_to_rmqServer(number)
    msg = f" (Was {number} in DB ?, is {number} Perfect ?)  "+ result
    return jsonify(msg)

@app.route("/")
def hello_world():
    return render_template('index.html')
    #return jsonify(options)
 
if __name__ == '__main__':
    app.run()