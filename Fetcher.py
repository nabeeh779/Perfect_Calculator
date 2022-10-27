from email.base64mime import body_decode
from pickle import NONE
from xml.dom.minidom import Element
from flask import Flask, jsonify, request
import pika
import uuid
from Fetcher_Connect import send_to_rmqServer
app = Flask(__name__)

#Options to let the user choose
options = {
    'option1': 'If number X Exist and Saved, example: http://127.0.0.1:5000/option1?number=5',
    'option2': 'Show All perfect numbers, example: http://127.0.0.1:5000/option2',
    'option3': 'Show All perfect numbers in range [ , ], example: http://127.0.0.1:5000/option3?start=4&end=72'
}

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
    number = args.get('number')
    result = send_to_rmqServer(number)
    msg = f" (Was {number} in DB ?, is {number} Perfect ?)  "+ result
    return jsonify(msg)

@app.route("/")
def hello_world():
    
    return jsonify(options)
 
if __name__ == '__main__':
    app.run()