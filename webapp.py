from flask import Flask, url_for, render_template, request, Markup
import os
import json
app = Flask(__name__)

def fun_fact(state):
    with open('state_demographics.json') as demographics_data:
        states = json.load(demographics_data)
    boi = 0
    for s in states:
        if s["State"] == state:
            if (s['Income']['Median Household Income'] > boi):
                boi = s['Income']['Median Household Income']
                higheststate = s['State']
    return state + "'s Median Household Income is " + "$"+"{:,}".format(boi)

@app.route("/") #annotation tells the URL that will make this function run
def render_main():
    with open('state_demographics.json') as demographics_data:
        states = json.load(demographics_data)
    try:
        state = request.args['states']
        ff=fun_fact(state)
        return render_template('home.html', states = get_state_options(states), funfact = ff)
    except:
        return render_template('home.html', states = get_state_options(states))

def get_state_options(states):
  bom=[]

  for state in states:
    state = state["State"]
    trfl = state in bom
    if (trfl == False):
      bom.append(state)


  options = ""
  for state in bom:
    options += Markup("<option value=\"" + state + "\">" + state + "</option>")

  return options

def page1(state):
    with open('state_demographics.json') as demographics_data:
        states = json.load(demographics_data)
    hgf = 0
    for s in states:
        if s["State"] == state:
            if (s['Population']['2014 Population'] > hgf):
                hgf = s['Population']['2014 Population']
                states = s['Population']
    return state + "'s Population in 2014 is " + "{:,}".format(hgf) + " people."

@app.route("/page1")
def b_b():
    with open('state_demographics.json') as demographics_data:
        states = json.load(demographics_data)
    try:
        state = request.args['states']
        bb=page1(state)
        return render_template('page1.html', states = get_state_options(states), b_b = bb)
    except:
        return render_template('page1.html', states = get_state_options(states))

        return options

@app.route("/page3")
def page3():
    return render_template('page3.html')

if __name__=="__main__":
    app.run(debug=False, port=66666)
