########  imports  ##########
from flask import Flask
from flask_restful import Resource, Api
from flask import request
import json

app = Flask(__name__)
api = Api(app)

#APIs

#Get offer deatils
@app.route('/offers',methods=['GET'])
def get_offer():
    #load json file
    file = open('banner_offer_json.json')
    offer = json.load(file)
    return offer

#Get horoscope list
@app.route('/horoscope_list',methods=['GET'])
def get_horoscope_list():
    #load horoscope json file
    file = open('horoscope_json.json')
    data = json.load(file)
    data=data['data']
    #create response variable
    horoscope = {}
    horoscope['list']=[]
    #Extract only names of horoscopes and append in response variable
    for i in range(0,len(data)):
        horoscope['list'].append({'name':data[i]['name']})
    return horoscope

#Fetch Astrologers list and details as json
@app.route('/astro',methods=['GET'])
def get_astrologer():
    #load astrologer json file and return
    file = open('astro.json')
    astrologers = json.load(file)
    return astrologers

#Fetch question category list
@app.route('/question_category',methods=['GET'])
def question_list():
    #load questions json file
    file = open('question_category.json')
    data = json.load(file)
    #Extract data from file and remove others
    data = data['data']
    #Response Variable
    response = {}
    response['data']=[]
    #Extract category from data and append
    for i in range(0,len(data)):
        response['data'].append({'name':data[i]['name']})
    return response

#Take question category as argument and return related question suggestions 
@app.route('/question/<arg>',methods=['POST'])
def get_question(arg):
    #print(arg)
    response = {}
    #response['data']=[{'name':'dfsdf'}]
    response['data']=[]
    file = open('question_category.json')
    data = json.load(file)
    data = data['data']
    for i in range(0,len(data)):
        if data[i]['name'] == arg:
            response['data'].append({'questions':data[i]['suggestions']})
            break
    return response


if __name__ == '__main__':
    app.run(debug=True)