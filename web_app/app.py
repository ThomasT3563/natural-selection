from __future__ import print_function
# use :print("Hello world", file=sys.stderr)
import sys
import os
import time

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/',methods=['GET'])
def main(): 
    
    global variable_1
    global variable_2
    
    if request.method == 'GET':
        variable_1 = request.args.get('variable_1', variable_1)
        variable_2 = request.args.get('variable_2', variable_2)
        
    return render_template("my_template.html",
                           var1=variable_1,
                           var2=variable_2)

@app.route('/simulation/init',methods=['POST'])
def simulation_init():
    print("Initialisation of simulation object", file=sys.stderr)
    
    # INITIALISATION
    simulation = None
    
    try:
        image = "static/image_example.jpg"
        return image
    except Exception as e:
        return e 
    

@app.route('/simulation',methods=['GET'])
def simulation_next_step():
    
    global simulation
    
    # COMPUTATION
    # IMAGE GENERATION
    
    try:
        image = "static/image_example.jpg"
        return image
    except Exception as e:
        return e
    

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    
    # global variables
    variable_1 = int(os.environ.get("VAR_1", None))
    variable_2 = int(os.environ.get("VAR_2", None))
    
    app.run(debug=True,host='0.0.0.0',port=port) 
    