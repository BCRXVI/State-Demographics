from flask import Flask, url_for, render_template, request, Markup
import os
import json
app = Flask(__name__)

def fun_fact(state):
    with open('state_demographics.json') as demographics_data:
        state = json.load(demographics_data)
    boi = 0
    higheststate = ''
    for state in states:
        if state["State"] == state:
            if (state['Income']['Median Household Income'] > boi):
                boi = state['Income']['Median Household Income']
                higheststate = state['State']
    return state + ' ' + higheststate + ' ' + str(boi)

@app.route("/") #annotation tells the URL that will make this function run
def render_main():
    with open('state_demographics.json') as demographics_data:
        states = json.load(demographics_data)
    try:
        state = request.args['states']
        print(state)
        ff=fun_fact(state)
        print(ff)
        return render_template('home.html', states = get_state_options(counties), funfact = ff)
    except:
        return render_template('home.html', states = get_state_options(counties))
  
def get_state_options(counties):
  bom=[]
  

  
  for county in counties:
    state = state["State"]
    trfl = state in bom
    if (trfl == False):
      bom.append(state)
      
      
  options = ""
  for state in bom:
    options += Markup("<option value=\"" + state + "\">" + state + "</option>")

  return options
 

    
if __name__=="__main__":
    app.run(debug=True, port=66666)
