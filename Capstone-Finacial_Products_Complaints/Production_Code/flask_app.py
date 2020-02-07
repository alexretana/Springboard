from flask import Flask, request, Blueprint
from flask_restplus import Resource, Api
import LoadModelPredict as lmp

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