# Task
# 1. Write a program to insert a record in sql table via api database
# 2. Write a program to update a record via api
# 3. Write a program to delete a record via api
# 4. Write a program to fetch a record via api
# 5. Do all the above questions you have to answer for mongo

from flask import Flask, request, jsonify
import mysql.connector as connection
import pandas as pd
from sqlalchemy import create_engine
import logging as lg
app=Flask(__name__)

def logger(s):
    lg.basicConfig(filename="task.txt", level=lg.INFO, format='%(asctime)s %(message)s')
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
    data = pd.DataFrame(dt)
    logger("The data is")
    logger(data)
    return data

@app.route('/insert',methods=['GET','POST'])
def insert_data_mysql():
    if (request.method=='POST'):
        user = 'root'
        password = 'admin'
        host = 'localhost'
        port = 3306
        database = 'task1'
        mydb = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")
        df = user_input_data()
        df.to_sql(con=mydb, name="task", index=False, if_exists="append")
        result="Records entered sucessfully... "
        return jsonify(result)

@app.route('/update',methods=['GET','POST'])
def update_record():
    if (request.method=='POST'):
        name = request.json['Name']
        new_name=request.json['New_Name']
        logger("The data is")
        logger(name)
        logger(new_name)
        mydb = connection.connect(host="localhost", user="root", passwd="admin", database='task1', use_pure=True)
        cursor = mydb.cursor()
        cursor.execute("update task set Name='%s' where Name='%s'"%(new_name,name))
        mydb.commit()
        result="Record Updated sucessfully"
        logger(result)
        return jsonify(result)

@app.route('/delete',methods=['GET','POST'])
def delete_record():
    if (request.method == 'POST'):
        name = request.json['Name']
        logger("The data is")
        logger(name)
        mydb = connection.connect(host="localhost", user="root", passwd="admin", database='task1', use_pure=True)
        cursor = mydb.cursor()
        cursor.execute("delete from task where Name = '%s'"%(name))
        mydb.commit()
        result="Record deleted sucessfully"
        logger(result)
        return jsonify(result)

@app.route('/fetch',methods=['GET','POST'])
def fetch_record():
    mydb = connection.connect(host="localhost", user="root", passwd="admin", database='task1', use_pure=True)
    query = f"select * from task"
    cursor = mydb.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    logger("The records are")
    logger(result)
    return jsonify(str(result))

if __name__ == '__main__':
    app.run(debug=True)
