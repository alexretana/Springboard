import unittest
import LoadModelPredict as lmp
import numpy as np
import pandas as pd
import random
import sklearn
from datetime import datetime, timedelta

def gen_datetime(min_year=1900, max_year=datetime.now().year):
    # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random.random()

class TestModel(unittest.TestCase):
    random.seed(42)
    complaintID = 3398126
    resp = lmp.checkAndGetComplaintData(complaintID)

    def test_getRespUsinArgv(self):
        with self.assertRaises(SystemExit) as cm:
            lmp.getRespUsinArgv(None)
        self.assertIsNone(cm.exception.code)

    
    def test_checkAndGetComplaintData(self):
        complaintIDreturn = int(self.__class__.resp.json()['hits']['hits'][0]['_source']['complaint_id'])
        #asserts complaint from api call equals the one inquired
        self.assertEqual(complaintIDreturn,self.__class__.complaintID)

        #asserts the status code for the response is indeed 200
        self.assertEqual(self.__class__.resp.status_code, 200)

        #Checks that 0 hits is returned correctly
        with self.assertRaises(SystemExit):
            badResp = lmp.checkAndGetComplaintData(00000000)
            self.assertEqual(badResp.json()['hits']['total'], 0)
    
    def test_convertToOther(self):
        keepList = ['One','Two','Three']
        testList = ['Three', 'Four', 'Five', 'Two', '']
        testAns = ['Three','Other','Other','Two', 'Other']
        self.assertEqual(lmp.convertToOther('',[]), 'Other')
        self.assertEqual(lmp.convertToOther('Not', keepList), 'Other')
        self.assertEqual(lmp.convertToOther('One', keepList), 'One')
        testedList = [lmp.convertToOther(val, keepList) for val in testList]
        self.assertEqual(testAns, testedList)

    def test_cleanReduceConvert(self):
        valList = ['val'+ str(val) for val in range(30)]
        df = pd.DataFrame({'vals':valList})
        self.assertEqual(24, len(lmp.cleanReduceConvert(df, 'vals').value_counts()))
        self.assertIsInstance(lmp.cleanReduceConvert(df,'vals'), pd.Series)
        self.assertTrue(lmp.cleanReduceConvert(df, 'vals').notna().any())

    def test_entryOrNull(self):
        val1 = np.nan
        val2 = ''
        self.assertEqual(0.0, lmp.entryOrNull(val1))
        self.assertEqual(1.0, lmp.entryOrNull(val2))
        valList = [2, '12', np.nan, 'test', np.nan]
        df = pd.DataFrame({'vals':valList})
        testSeries = pd.Series(index=[1.0,0.0])
        self.assertEqual(df['vals'].apply(lmp.entryOrNull).value_counts().index[0], testSeries.index[0])
        self.assertEqual(df['vals'].apply(lmp.entryOrNull).value_counts().index[1], testSeries.index[1])

    def test_dtToCols(self):
        vals = [gen_datetime(), gen_datetime(), gen_datetime(), gen_datetime(), gen_datetime()]
        dtdf = pd.DataFrame({'test':vals})
        dtdf['test'] = pd.to_datetime(dtdf.test)
        lmp.dtToCols(dtdf, 'test')
        self.assertEqual(dtdf.columns.to_list(), ['test','test day', 'test month','test year'])
        self.assertTrue(dtdf['test day'].le(31).all())
        self.assertTrue(dtdf['test month'].le(12).all())

    def test_createDF(self):
        df = lmp.createDF(self.__class__.complaintID, self.__class__.resp)
        final_cols = ['Date received',
                    'Product',
                    'Sub-product',
                    'Issue',
                    'Sub-issue',
                    'Consumer complaint narrative',
                    'Company public response',
                    'Company',
                    'State',
                    'ZIP code',
                    'Tags',
                    'Consumer consent provided?',
                    'Submitted via',
                    'Date sent to company',
                    'Company response to consumer',
                    'Timely response?',
                    'Consumer disputed?',
                    'Consumer complaint narrative submitted?',
                    'Date received day',
                    'Date received month',
                    'Date received year',
                    'Date sent to company day',
                    'Date sent to company month',
                    'Date sent to company year']
        self.assertEqual(df.columns.to_list(), final_cols)

    def test_dropUnusedCols(self):
        df = lmp.createDF(self.__class__.complaintID, self.__class__.resp)
        X, Y = lmp.dropUnusedCols(df)
        self.assertFalse(X.isna().any().any())
        final_cols = ['Product',
                    'Sub-product',
                    'Issue',
                    'Sub-issue',
                    'Company',
                    'ZIP code',
                    'Consumer consent provided?',
                    'Submitted via',
                    'Timely response?',
                    'Consumer complaint narrative submitted?',
                    'Date received day',
                    'Date received month',
                    'Date received year',
                    'Date sent to company day',
                    'Date sent to company month',
                    'Date sent to company year']
        self.assertEqual(X.columns.to_list(), final_cols)

    def test_loadModelPredict(self):
        df = lmp.createDF(self.__class__.complaintID, self.__class__.resp)
        X, Y = lmp.dropUnusedCols(df)
        model, pred, perc = lmp.loadModelPredict(X)
        self.assertIsNotNone(model)
        self.assertTrue((pred in ['Closed with relief', 'Closed without relief']))
        self.assertGreaterEqual(perc, 0)
        self.assertLessEqual(perc,100)

if __name__ == '__main__':
    unittest.main(exit=False)