from flask import Flask, request, Blueprint
from flask_restplus import Resource, Api, fields
import TrainSaveModel as tsm
import LoadModelPredict as lmp

app = Flask(__name__)
api = Api(app)

prediction = api.model('Prediction', 
                        {'complaintID': fields.Integer('Compalint ID Number'),
                        'Outcome_Prediction': fields.String('Outcome of prediction'),
                        'Proba': fields.Float('Percent chance of resolution with relief')})


@api.route('/prediction/<int:complaintID>', endpoint='prediciton')
class Prediction(Resource):
    @api.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 401: 'Compalint not found'},
            params={ 'complaintID': 'Number that indentifies consumer\'s complaint'})
    def get(self, complaintID):
        """
        Returns the prediction of a complaint submitted. Requires valid complaintID
        """
        return lmp.main(complaintID)

@api.route('/train_models')
class Train_model(Resource):
    def put(self):
        pass

api.add_resource(Prediction, '/prediction/<int:complaintID>')
api.add_resource(Train_model, '/train_models')

if __name__ == '__main__':
    app.run(debug=True)