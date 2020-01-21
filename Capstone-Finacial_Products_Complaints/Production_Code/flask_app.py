from import Flask, requests
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Prediction(Resource):
    def get(self):
        pass

class Train_model(Resource):
    def post(self):
        pass

if __name__ == '__main__':
    app.run(debug=True)