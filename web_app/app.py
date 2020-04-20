from __future__ import print_function
import sys
import os
import time
import glob
import random
import json

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
    global simulation
    try:
        # delete previously generated files
        for fname in glob.glob("static/display_simulation/*.png"):
            if os.path.isfile(fname):
                os.remove(fname)
        # instantiate simulation object
        fsimulation = f"static/display_simulation/simulation_{random.randint(1e6,9e6)}.png"
        fdemographic = f"static/display_simulation/demographic_{random.randint(1e6,9e6)}.png"
        simulation = Simulation(map_size=[40, 40])
        simulation.display(filename=fsimulation)
        simulation.display_demographic(filename=fdemographic)
        return json.dumps([fsimulation,fdemographic])
    except Exception as e:
        print(f"Exception during initialisation: {picture_filepath}")
        return e


@app.route('/simulation', methods=['GET'])
def simulation_next_step():
    print("Simulation next step", file=sys.stderr)
    global simulation
    # picture_filepath = "static/image_example.jpg"
    try:
        fsimulation = f"static/display_simulation/simulation_{random.randint(1e6,9e6)}.png"
        fdemographic = f"static/display_simulation/demographic_{random.randint(1e6,9e6)}.png"
        simulation.next_iteration()
        simulation.display(filename=fsimulation)
        simulation.display_demographic(filename=fdemographic)
        return json.dumps([fsimulation,fdemographic])
    except Exception as e:
        return e


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    
    # global variables
    simulation = ""
    variable_1 = int(os.environ.get("VAR_1", None))
    variable_2 = int(os.environ.get("VAR_2", None))
    
    app.run(debug=True, host='0.0.0.0', port=port)
