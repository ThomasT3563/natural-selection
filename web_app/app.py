from __future__ import print_function
print("Hello world", file=sys.stderr)

import sys
import os
import time

from src.simulation_handler import Simulation
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():

    global variable_1
    global variable_2
    
    if request.method == 'GET':
        variable_1 = request.args.get('variable_1', variable_1)
        variable_2 = request.args.get('variable_2', variable_2)
        
    return render_template("my_template.html",
                           var1=variable_1,
                           var2=variable_2)


@app.route('/simulation/init', methods=['POST'])
def simulation_init():
    print("Initialisation of simulation object", file=sys.stderr)
    try:
        picture_filepath = "static/simulation_test.jpg"
        simulation = Simulation(map_size=[40,40])
        simulation.display(filename=picture_filepath)
        return picture_filepath
    except Exception as e:
        return e


@app.route('/simulation', methods=['GET'])
def simulation_next_step():
    print("Simulation next step", file=sys.stderr)
    #picture_filepath = "static/image_example.jpg"
    try:
        global simulation
        picture_filepath = "static/simulation_test.jpg"
        simulation.next_iteration()
        simulation.display(filename=picture_filepath)
        return picture_filepath
    except Exception as e:
        return e


@app.route('/simulation/delete', methods=['DELETE'])
def simulation_delete():
    print("Delete simulation object and files generated", file=sys.stderr)
    try:
        # DELETE PNG FILES
        return None
    except Exception as e:
        return e


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    
    # global variables
    variable_1 = int(os.environ.get("VAR_1", None))
    variable_2 = int(os.environ.get("VAR_2", None))
    
    app.run(debug=True, host='0.0.0.0', port=port)