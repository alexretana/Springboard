from flask import Flask, requests
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Prediction(Resource):
    def get(self):
        pass

class Train_model(Resource):
    def post(self):
        pass

api.add_resource(Prediction, '/')
api.add_resource(Train_model, '/train')

if __name__ == '__main__':
    app.run(debug=True)