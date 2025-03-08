from flask import Flask
from flask_restful import Resource , Api , abort , reqparse
from addingapps import *
from openApps import *

app = Flask(__name__)
api = Api(app)

Appname = reqparse.RequestParser()
Appname.add_argument('app name', type=str, required = True, help="you must enter a app name")

class openApps(Resource):
    
    def get(self):
        ...
    def put(self):
        appname = Appname.parse_args()
        if checkifexist(appname["app name"]):
            openingApps(appname["app name"])
            return {"message":"app oppend sucessfully"} , 200
        else:
            abort(404, message = "app not found")
    def patch(self, video_id):
        ...
    def delete(self, video_id):
        ...


api.add_resource(openApps, '/open')

if __name__ == "__main__":
    app.run(debug=True)
