from flask import Flask, jsonify
from flask_restful import Resource , Api , abort , reqparse
from addingapps import *
from openApps import *
from commands import *

app = Flask(__name__)
api = Api(app)

Appname = reqparse.RequestParser()
Appname.add_argument('appname', type=str, required = True, help="you must enter a app name")
command = reqparse.RequestParser()
command.add_argument('command', type=str, required = True, help="you must enter a command")

class openApps(Resource):
    def put(self):
        gg = Appname.parse_args()
        if checkifexist(gg["appname"]):
            openingApps(gg["appname"])
            return {"message":"app oppend sucessfully"} , 200
        else:
            abort(404, message = "app not found")
class commands(Resource):
    def put(self):
        gg = command.parse_args()
        if gg["command"] in funcs:
            choose(gg["command"])
            return {"message":"app oppend sucessfully"} , 200
        else:
            abort(404, message = "command is not exist")
        
api.add_resource(openApps, '/open')
api.add_resource(commands, "/command")
app.run(debug=True)