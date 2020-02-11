from flask import Flask, request, Blueprint, abort
from flask_restplus import Resource, Api, fields, Model
import TrainSaveModel as tsm
import LoadModelPredict as lmp

app = Flask(__name__)
api = Api(app, version='1.0.0', title= 'CFPB Compalint Predictor', description= 'An API to predict the Resolution Outcome of Complaints submitted to the Consumer Financial Protection Bureau (CFPB)')
ns = api.namespace('devs', description= 'Tools for developers')


prediction = api.model('Prediction', 
                        {'complaintID': fields.Integer(required='Compalint ID Number'),
                        'Outcome_Prediction': fields.String('Outcome of prediction'),
                        'Proba': fields.Float('Percent chance of resolution with relief')})

@ns.route('/prediction/<int:complaintID>', endpoint='prediciton')
class Prediction(Resource):
    @ns.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 401: 'Compalint not found'},
            params={ 'complaintID': 'Number that indentifies consumer\'s complaint'})
    @ns.expect(prediction)
    @ns.marshal_with(prediction)
    def get(self, complaintID):
        """
        Returns the prediction of a complaint submitted. Requires valid complaintID
        """
        apiModelPrediction = ['complaintID', 'Outcome_Prediction', 'Proba']
        try:
            pred = lmp.main(complaintID)
        except:
            abort(401)
        else:
            predictionObj = dict(zip(apiModelPrediction, pred))
            return predictionObj

@ns.route('/train_model')
class Train_model(Resource):
    @ns.doc(responses = {200: 'OK', 400: 'Model Training Failed', 201: 'Model Trained, but did not out preform the previous model'})
    def put(self):
        tsm.run()
        return 200



if __name__ == '__main__':
    app.run(debug=True)