from flask import Flask, jsonify, request
import os
import json
import sys
import threading

def loadJson_it():
    with open('ithome.json','r',encoding = 'utf-8') as file:
        return json.load(file)

def loadJson_notice():
    with open('corona_notice.json','r',encoding = 'utf-8') as file:
        return json.load(file)

def loadJson_new():
    with open('corona_new.json','r',encoding = 'utf-8') as file:
        return json.load(file)

def loadJson_data():
    with open('data.json','r',encoding = 'utf-8') as file:
        return json.load(file)

def loadJson_creative():
    with open('creative.json','r',encoding = 'utf-8') as file:
        return json.load(file)

def loadJson_cpp():
    with open('cpp.json','r',encoding = 'utf-8') as file:
        return json.load(file)

def loadJson_electrical():
    with open('electrical.json','r',encoding = 'utf-8') as file:
        return json.load(file)

def loadJson_global():
    with open('global.json','r',encoding = 'utf-8') as file:
        return json.load(file)

def loadJson_DMath():
    with open('DMath.json','r',encoding = 'utf-8') as file:
        return json.load(file)

it_json = None
corona_notice_json = None
corona_new_json = None
data_json = None
creative_json =None
cpp_json = None
electrical_json = None
global_json = None
DMath_json = None
 
class Repeat:
    def __init__(self):
        pass

    def Reflask(self):
        global it_json, corona_notice_json, corona_new_json, data_json, creative_json, cpp_json, electrical_json, global_json, DMath_json
        it_json = loadJson_it()
        corona_notice_json = loadJson_notice()
        corona_new_json = loadJson_new()
        data_json = loadJson_data()
        creative_json = loadJson_creative()
        cpp_json = loadJson_cpp()
        electrical_json = loadJson_electrical()
        global_json = loadJson_global()
        DMath_json = loadJson_DMath()
        print("load")
        threading.Timer(3600, self.Reflask).start()

re = Repeat()
re.Reflask()

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def start():
    response_data = {
                "version" : "2.0",
                "template" : {
                    "outputs" : [
                        {
                            "simpleText" : {
                                "text" : "< 최신공지 >\n1. " + corona_new_json[0]['text'] + "(" + corona_new_json[0]['date'] + ")\n" + corona_new_json[0]['link'] + "\n\n2. " + corona_new_json[1]['text'] + "(" + corona_new_json[1]['date'] + ")\n" + corona_new_json[1]['link'] + "\n\n3. " + corona_new_json[2]['text'] + "(" + corona_new_json[2]['date'] + ")\n" + corona_new_json[2]['link'] + "\n\n4. " + corona_new_json[3]['text'] + "(" + corona_new_json[3]['date'] + ")\n" + corona_new_json[3]['link'] + "\n\n5. " + corona_new_json[4]['text'] + "(" + corona_new_json[4]['date'] + ")\n" + corona_new_json[4]['link']        
                            }}]}}
    return jsonify(response_data)

@app.route('/assign', methods = ['POST'])
def assign():
    content = request.get_json()
    content = content['userRequest']
    content = content['utterance']

    if content == u"전부":
        response_data = {
                "version" : "2.0",
                "template" : {
                    "outputs" : [
                        {
                            "simpleText" : {
                                "text" : "< 이산수학 과제 >\n과제명 :  " + DMath_json[7]['title'] + "\n제출기한 : " + DMath_json[7]['date'] +"\n\n< c++프로그래밍 과제 >\n과제명 : " + cpp_json[0]['title'] + "\n제출기한 : " + cpp_json[0]['date'] + "\n\n< 자료구조 과제 >\n과제명 : " + data_json[0]['title'] + "\n제출기한 : " + data_json[0]['date'] + "\n\n< 전기전자기초실험 과제 >\n과제명 : " + electrical_json[0]['title'] + "\n제출기한 : " + electrical_json[0]['date'] + "\n\n과제명 :  " + electrical_json[1]['title'] + "\n제출기한 : " + electrical_json[1]['date'] + "\n\n과제명 :  " + electrical_json[2]['title'] + "\n제출기한 : " + electrical_json[2]['date'] + "\n\n< 창의적it공학설계입문 과제 >\n과제명 : " + creative_json[0]['title'] + "\n제출기한 : " + creative_json[0]['date'] + "\n\n< 글로벌공학윤리 과제 >\n과제명 : " + global_json[0]['title'] + "\n제출기한 : " + global_json[0]['date']
                            }}]}}
    
    elif content == u"이산수학":
        response_data = {
                "version" : "2.0",
                "template" : {
                    "outputs" : [
                        {
                            "simpleText" : {
                                "text" : "< 이산수학 과제 >\n과제명 :  " + DMath_json[7]['title'] + "\n제출기한 : " + DMath_json[7]['date']
                            }}]}}
    elif content == u"자료구조":
        response_data = {
                "version" : "2.0",
                "template" : {
                    "outputs" : [
                        {
                            "simpleText" : {
                                "text" : "< 자료구조 과제 >\n과제명 :  " + data_json[0]['title'] + "\n제출기한 : " + data_json[0]['date']
                            }}]}}
    elif content == u"c++프로그래밍":
        response_data = {
                "version" : "2.0",
                "template" : {
                    "outputs" : [
                        {
                            "simpleText" : {
                                "text" : "< c++프로그래밍 과제 >\n과제명 :  " + cpp_json[0]['title'] + "\n제출기한 : " + cpp_json[0]['date']
                            }}]}}
    elif content == u"전기전자기초실험":
                response_data = {
                "version" : "2.0",
                "template" : {
                    "outputs" : [
                        {
                            "simpleText" : {
                                "text" : "< 전기전자기초실험 과제 >\n과제명 :  " + electrical_json[0]['title'] + "\n제출기한 : " + electrical_json[0]['date'] + "\n\n과제명 :  " + electrical_json[1]['title'] + "\n제출기한 : " + electrical_json[1]['date'] + "\n\n과제명 :  " + electrical_json[2]['title'] + "\n제출기한 : " + electrical_json[2]['date']
                            }}]}}

    elif content == u"글로벌공학윤리":
                response_data = {
                "version" : "2.0",
                "template" : {
                    "outputs" : [
                        {
                            "simpleText" : {
                                "text" : "< 글로벌공학윤리 과제 >\n과제명 :  " + global_json[0]['title'] + "\n제출기한 : " + global_json[0]['date']
                            }}]}}

    elif content == u"창의적it공학설계입문":
                response_data = {
                "version" : "2.0",
                "template" : {
                    "outputs" : [
                        {
                            "simpleText" : {
                                "text" : "< 전기전자기초실험 과제 >\n과제명 :  " + creative_json[0]['title'] + "\n제출기한 : " + creative_json[0]['date']
                            }}]}}
    return jsonify(response_data)
@app.route('/ithome', methods = ['POST'])
def ithome():
    content = request.get_json()
    content = content['userRequest']
    content = content['utterance']

    if  content == u"학과 공지":
     response_data = {
         "version" : "2.0",
            "template" : {
             "outputs" : [
                 {
                        "simpleText" : {
                         "text" : "1. " + it_json[0]['title'] + "(" + it_json[0]['date'] + ")\n" + it_json[0]['url'] + "\n\n2. " + it_json[1]['title'] + "(" + it_json[1]['date'] + ")\n" + it_json[1]['url'] + "\n\n3. " + it_json[2]['title'] + "(" + it_json[2]['date'] + ")\n" + it_json[2]['url'] + "\n\n4. " + it_json[3]['title'] + "(" + it_json[3]['date'] + ")\n" + it_json[3]['url'] + "\n\n5. " + it_json[4]['title'] + "(" + it_json[4]['date'] + ")\n" + it_json[4]['url']
                            }
                        }
                    ]
                }
            }
    return jsonify(response_data)

@app.route('/corona', methods = ['POST'])
def corona():
    content = request.get_json()
    content = content['userRequest']
    content = content['utterance']

    if  content == u"코로나 공지":
        if len(corona_notice_json) > 5:
            response_data = {
                "version" : "2.0",
                "template" : {
                    "outputs" : [
                        {
                            "simpleText" : {
                                "text" : "< 필독공지 >\n1. " + corona_notice_json[0]['text'] + "(" + corona_notice_json[0]['date'] + ")\n" + corona_notice_json[0]['link'] + "\n\n2. " + corona_notice_json[1]['text'] + "(" + corona_notice_json[1]['date'] + ")\n" + corona_notice_json[1]['link'] + "\n\n3. " + corona_notice_json[2]['text'] + "(" + corona_notice_json[2]['date'] + ")\n" + corona_notice_json[2]['link'] + "\n\n4. " + corona_notice_json[3]['text'] + "(" + corona_notice_json[3]['date'] + ")\n" + corona_notice_json[3]['link'] + "\n\n5. " + corona_notice_json[4]['text'] + "(" + corona_notice_json[4]['date'] + ")\n" + corona_notice_json[4]['link']        
                            }},
                        {
                            "simpleText" : {
                                "text" : "< 최신공지 >\n1. " + corona_new_json[0]['text'] + "(" + corona_new_json[0]['date'] + ")\n" + corona_new_json[0]['link'] + "\n\n2. " + corona_new_json[1]['text'] + "(" + corona_new_json[1]['date'] + ")\n" + corona_new_json[1]['link'] + "\n\n3. " + corona_new_json[2]['text'] + "(" + corona_new_json[2]['date'] + ")\n" + corona_new_json[2]['link'] + "\n\n4. " + corona_new_json[3]['text'] + "(" + corona_new_json[3]['date'] + ")\n" + corona_new_json[3]['link'] + "\n\n5. " + corona_new_json[4]['text'] + "(" + corona_new_json[4]['date'] + ")\n" + corona_new_json[4]['link']        
                            }}
                        ]}}
        elif len(corona_notice_json) == 4:
            response_data = {
                "version" : "2.0",
                "template" : {
                    "outputs" : [
                        {
                            "simpleText" : {
                                "text" : "< 필독공지 >\n1. " + corona_notice_json[0]['text'] + "(" + corona_notice_json[0]['date'] + ")\n" + corona_notice_json[0]['link'] + "\n\n2. " + corona_notice_json[1]['text'] + "(" + corona_notice_json[1]['date'] + ")\n" + corona_notice_json[1]['link'] + "\n\n3. " + corona_notice_json[2]['text'] + "(" + corona_notice_json[2]['date'] + ")\n" + corona_notice_json[2]['link'] + "\n\n4. " + corona_notice_json[3]['text'] + "(" + corona_notice_json[3]['date'] + ")\n" + corona_notice_json[3]['link']      
                            }},
                        {
                            "simpleText" : {
                                "text" : "< 최신공지 >\n1. " + corona_new_json[0]['text'] + "(" + corona_new_json[0]['date'] + ")\n" + corona_new_json[0]['link'] + "\n\n2. " + corona_new_json[1]['text'] + "(" + corona_new_json[1]['date'] + ")\n" + corona_new_json[1]['link'] + "\n\n3. " + corona_new_json[2]['text'] + "(" + corona_new_json[2]['date'] + ")\n" + corona_new_json[2]['link'] + "\n\n4. " + corona_new_json[3]['text'] + "(" + corona_new_json[3]['date'] + ")\n" + corona_new_json[3]['link'] + "\n\n5. " + corona_new_json[4]['text'] + "(" + corona_new_json[4]['date'] + ")\n" + corona_new_json[4]['link']        
                            }}
                        ]}}
        elif len(corona_notice_json) == 3:
            response_data = {
                "version" : "2.0",
                "template" : {
                    "outputs" : [
                        {
                            "simpleText" : {
                                "text" : "< 필독공지 >\n1. " + corona_notice_json[0]['text'] + "(" + corona_notice_json[0]['date'] + ")\n" + corona_notice_json[0]['link'] + "\n\n2. " + corona_notice_json[1]['text'] + "(" + corona_notice_json[1]['date'] + ")\n" + corona_notice_json[1]['link'] + "\n\n3. " + corona_notice_json[2]['text'] + "(" + corona_notice_json[2]['date'] + ")\n" + corona_notice_json[2]['link'] 
                            }},
                        {
                            "simpleText" : {
                                "text" : "< 최신공지 >\n1. " + corona_new_json[0]['text'] + "(" + corona_new_json[0]['date'] + ")\n" + corona_new_json[0]['link'] + "\n\n2. " + corona_new_json[1]['text'] + "(" + corona_new_json[1]['date'] + ")\n" + corona_new_json[1]['link'] + "\n\n3. " + corona_new_json[2]['text'] + "(" + corona_new_json[2]['date'] + ")\n" + corona_new_json[2]['link'] + "\n\n4. " + corona_new_json[3]['text'] + "(" + corona_new_json[3]['date'] + ")\n" + corona_new_json[3]['link'] + "\n\n5. " + corona_new_json[4]['text'] + "(" + corona_new_json[4]['date'] + ")\n" + corona_new_json[4]['link']        
                            }}
                        ]}}
        elif len(corona_notice_json) == 2:
            response_data = {
                "version" : "2.0",
                "template" : {
                    "outputs" : [
                        {
                            "simpleText" : {
                                "text" : "< 필독공지 >\n1. " + corona_notice_json[0]['text'] + "(" + corona_notice_json[0]['date'] + ")\n" + corona_notice_json[0]['link'] + "\n\n2. " + corona_notice_json[1]['text'] + "(" + corona_notice_json[1]['date'] + ")\n" + corona_notice_json[1]['link'] 
                            }},
                        {
                            "simpleText" : {
                                "text" : "< 최신공지 >\n1. " + corona_new_json[0]['text'] + "(" + corona_new_json[0]['date'] + ")\n" + corona_new_json[0]['link'] + "\n\n2. " + corona_new_json[1]['text'] + "(" + corona_new_json[1]['date'] + ")\n" + corona_new_json[1]['link'] + "\n\n3. " + corona_new_json[2]['text'] + "(" + corona_new_json[2]['date'] + ")\n" + corona_new_json[2]['link'] + "\n\n4. " + corona_new_json[3]['text'] + "(" + corona_new_json[3]['date'] + ")\n" + corona_new_json[3]['link'] + "\n\n5. " + corona_new_json[4]['text'] + "(" + corona_new_json[4]['date'] + ")\n" + corona_new_json[4]['link']        
                            }}
                        ]}}
        elif len(corona_notice_json) == 1:
            response_data = {
                "version" : "2.0",
                "template" : {
                    "outputs" : [
                        {
                            "simpleText" : {
                                "text" : "< 필독공지 >\n1. " + corona_notice_json[0]['text'] + "(" + corona_notice_json[0]['date'] + ")\n" + corona_notice_json[0]['link'] 
                            }},
                        {
                            "simpleText" : {
                                "text" : "< 최신공지 >\n1. " + corona_new_json[0]['text'] + "(" + corona_new_json[0]['date'] + ")\n" + corona_new_json[0]['link'] + "\n\n2. " + corona_new_json[1]['text'] + "(" + corona_new_json[1]['date'] + ")\n" + corona_new_json[1]['link'] + "\n\n3. " + corona_new_json[2]['text'] + "(" + corona_new_json[2]['date'] + ")\n" + corona_new_json[2]['link'] + "\n\n4. " + corona_new_json[3]['text'] + "(" + corona_new_json[3]['date'] + ")\n" + corona_new_json[3]['link'] + "\n\n5. " + corona_new_json[4]['text'] + "(" + corona_new_json[4]['date'] + ")\n" + corona_new_json[4]['link']        
                            }}
                        ]}}
        else:
            response_data = {
                "version" : "2.0",
                "template" : {
                    "outputs" : [
                        {
                            "simpleText" : {
                                "text" : "< 최신공지 >\n1. " + corona_new_json[0]['text'] + "(" + corona_new_json[0]['date'] + ")\n" + corona_new_json[0]['link'] + "\n\n2. " + corona_new_json[1]['text'] + "(" + corona_new_json[1]['date'] + ")\n" + corona_new_json[1]['link'] + "\n\n3. " + corona_new_json[2]['text'] + "(" + corona_new_json[2]['date'] + ")\n" + corona_new_json[2]['link'] + "\n\n4. " + corona_new_json[3]['text'] + "(" + corona_new_json[3]['date'] + ")\n" + corona_new_json[3]['link'] + "\n\n5. " + corona_new_json[4]['text'] + "(" + corona_new_json[4]['date'] + ")\n" + corona_new_json[4]['link']        
                            }}]}}
    return jsonify(response_data)

if __name__ == "__main__":              
    app.run(host="0.0.0.0", port="8080")
