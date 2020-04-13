import os
import time

from flask import Flask, request, render_template, redirect
from wtforms import TextField, Form, SubmitField

app = Flask(__name__)

@app.route('/',methods=['GET'])
def variable_def(): 
    
    global variable_1
    global variable_2
    
    if request.method == 'GET':
        variable_1 = request.args.get('variable_1', variable_1)
        variable_2 = request.args.get('variable_2', variable_2)
    
    return render_template("template.html",
                           var1=variable_1,
                           var2=variable_2)
     
@app.route('/simulation')
def simulation():
    """
    if request.method == 'POST':
        if 'start_stop_button' in request.form:
            simulation_running = not simulation_running
        
    if simulation_running:
        # generate new png (from simulation code)
        time.sleep(1)
        return render_template("template.html", 
                               var1=variable_1,
                               var2=variable_2, 
                               image="static/image_example.jpg")
    else:
        return render_template("template.html",
                               var1=variable_1,
                               var2=variable_2)
    """
    return "SIMULATION"
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    
    # global variables
    variable_1 = int(os.environ.get("VAR_1", None))
    variable_2 = int(os.environ.get("VAR_2", None))
    
    app.run(debug=True,host='0.0.0.0',port=port) 
    