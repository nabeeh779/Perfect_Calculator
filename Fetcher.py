from crypt import methods
from flask import Flask, jsonify, request
import Save 
 
app = Flask(__name__)

options = {
    'option1': 'If number X Exist and Saved',
    'option2': 'Show All perfect numbers',
    'option3': 'Show All perfect numbers in range [ , ]'
}

@app.route('/option3/<var>',methods=['GET'])
def option1(var):
    return ''

@app.route('/option2/',methods=['GET'])
def option1(var):
    return ''

@app.route('/option1/<var>',methods=['GET'])
def option1(var):
    return ''
    
@app.route("/options")
def get_options():
    return jsonify(options)

@app.route("/")
def hello_world():
    return "Welcome , choose option from /options"
 
if __name__ == '__main__':
    app.run()