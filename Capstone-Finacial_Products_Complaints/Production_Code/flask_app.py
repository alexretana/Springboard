from flask import Flask, request, Blueprint, abort
from flask_restplus import Resource, Api, fields, Model
import TrainSaveModel as tsm
import LoadModelPredict as lmp

app = Flask(__name__)
api = Api(app, version='1.0.0', title= 'CFPB Compalint Predictor', description= 'An API to predict the Resolution Outcome of Complaints submitted to the Consumer Financial Protection Bureau (CFPB)')
ns = api.namespace('devs', description= 'Tools for developers')


prediction = api.model('prediction', 
                        {'complaintID': fields.Integer(default= None, required=True, example = 3398126, description= 'Compalint ID Number'),
                        'Outcome_Prediction': fields.String(default=None, example= 'Closed without relief', description='Outcome of prediction'),
                        'Proba': fields.Float(default=None, example= 20.31, description='Percent chance of resolution with relief')})

model_scores = api.model('model_scores',
                        {'date': fields.String(default=None,description='String describing time and date of training for a model', example='2020-02-11 14:50:40', required=True),
                        'precision': fields.Float(default=None,description='Precision score of model', example=0.324879),
                        'recall': fields.Float(default=None,description='Recall score of model', example=0.666638),
                        'fscore': fields.Float(default=None,description='F1-score of model', example=0.436859),
                        'accuracy': fields.Float(default=None,description='Accuracy score of model', example=0.6749668)})

score_log = api.model('score_log', 
                    {'score_log': fields.List(fields.Nested(model_scores), description= "List of model_scores for all scores currently store in server logfile")})

@ns.route('/prediction/<int:complaintID>', endpoint='prediciton')
class Prediction(Resource):
    @ns.doc(params={ 'complaintID': 'Number that indentifies consumer\'s complaint'})
    @ns.response(200, 'OK', prediction)
    @ns.response(400, 'Error Occured')
    @ns.response(401, 'Complaint could not be found')
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
    @ns.response(200, 'OK', model_scores)
    @ns.response(201, 'Model Trained, but did not out preform the previous model', model_scores)
    @ns.response(400, 'Model Training Failed')
    @ns.marshal_with(model_scores)
    def put(self):
        """
        Trains the model in the server. If the model is best to date, it becomes the primary model
        """
        model_score, status_code = tsm.run()
        return model_score, status_code

    @ns.response(200, 'OK', score_log)
    @ns.response(400, 'Unable to fetch log')
    @ns.marshal_list_with(model_scores)
    def get(self):
        """
        Returns json of all model scores. All the model scores in the ModelScore.log file are returned
        """
        entry_count = len(open('./LogsAndModels/ModelScore.log').readlines())
        score_log = []

        for i in range(entry_count):
            log_entry = tsm.readScore(i)
            score_log.append(log_entry)
        
        return score_log




if __name__ == '__main__':
    app.run(debug=True)