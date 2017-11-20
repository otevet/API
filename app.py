from flask import Flask, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine

#Create a engine for connecting to SQLite3.
#Assuming takehome.db is in your app folder

e = create_engine('sqlite:///takehome.db')

app = Flask(__name__)
api = Api(app)


class ID(Resource):
    def get(self, interview_id, column):
        #Connect to databse
        conn = e.connect()

        if column.isnumeric():
           #Perform query and return JSON data
           query_stamp = conn.execute("select [Exposure Stamps] from takehome where [Survata Interview ID]='{}'".format(interview_id))
           result = {'Exposure Stamp Count': [i[0] for i in query_stamp.cursor.fetchall()][0].count(str(column))}
           return jsonify(result)

        column = column.replace("_"," ")
        column = column.replace("%20"," ")
        column = column.replace("'","")

        #Check if multiple ID's are provided
        if "," in interview_id:
           interview_id = tuple(interview_id.split(","))
           query = conn.execute("SELECT [Survata Interview ID],[{}] FROM takehome WHERE [Survata Interview ID] IN {}".format(column, interview_id))
        else:
           query = conn.execute("select [{}] from takehome where [Survata Interview ID]='{}'".format(column, interview_id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

api.add_resource(ID, '/<string:interview_id>/<string:column>')

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=3000)
