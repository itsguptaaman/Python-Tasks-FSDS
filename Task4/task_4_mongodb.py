# Task
# 1. Write a program to insert a record in sql table via api database
# 2. Write a program to update a record via api
# 3. Write a program to delete a record via api
# 4. Write a program to fetch a record via api
# 5. Do all the above questions you have to answer for mongo

from flask import Flask, request, jsonify
import logging as lg
import pymongo
import certifi

# print(x)

app=Flask(__name__)

def logger(s):
    lg.basicConfig(filename="task_mongo.txt", level=lg.INFO, format='%(asctime)s %(message)s')
    lg.info(s)

def user_input_data():
    try:
        name = request.json['Name']
    except Exception as e:
        name = "unknown"
    try:
        age = request.json['Age']
    except Exception as e:
        age = 0
    dt = {'Name': [name], 'Age': [age]}
    logger("The data is")
    logger(dt)
    return dt

@app.route('/insert',methods=['GET','POST'])
def insert_data_mongo():
    ca = certifi.where()
    client = pymongo.MongoClient("mongodb+srv://admin:Aman@cluster0.a75efai.mongodb.net/?retryWrites=true&w=majority",
                                 tlsCAFile=ca)
    db = client['Task']
    collection = db['Task4']
    data=user_input_data()
    collection.insert_one(data)
    result = "Record Updated sucessfully"
    logger(result)
    return jsonify(result)


@app.route('/update',methods=['GET','POST'])
def update_record():
    ca = certifi.where()
    client = pymongo.MongoClient("mongodb+srv://admin:Aman@cluster0.a75efai.mongodb.net/?retryWrites=true&w=majority",
                                 tlsCAFile=ca)
    db = client['Task']
    collection = db['Task4']
    name = request.json['Name']
    new_name = request.json['New_Name']
    logger("The data is")
    logger(name)
    logger(new_name)
    dt1={"Name":name}
    dt2={"$set":{"Name":new_name}}
    collection.update_one(dt1,dt2)
    x=collection.find_one()
    result = "Record Updated sucessfully"
    logger(result)
    return jsonify(result)

@app.route('/delete',methods=['GET','POST'])
def delete_record():
    ca = certifi.where()
    client = pymongo.MongoClient("mongodb+srv://admin:Aman@cluster0.a75efai.mongodb.net/?retryWrites=true&w=majority",
                                 tlsCAFile=ca)
    db = client['Task']
    collection = db['Task4']
    name = request.json['Name']
    dt={"Name":name}
    collection.delete_one(dt)
    result = "Record deleted sucessfully"
    logger(result)
    return jsonify(result)

@app.route('/fetch',methods=['GET','POST'])
def fetch_record():
    ca = certifi.where()
    client = pymongo.MongoClient("mongodb+srv://admin:Aman@cluster0.a75efai.mongodb.net/?retryWrites=true&w=majority",
                                 tlsCAFile=ca)
    db = client['Task']
    collection = db['Task4']
    x=collection.find()
    result=[]
    for i in x:
        result.append(i)

    logger("The records are")
    logger(result)
    return jsonify(str(result))

if __name__ == '__main__':
    app.run(debug=True)
