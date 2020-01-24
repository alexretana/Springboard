import unittest
import TrainSaveModel as tsm
import pandas as pd
import numpy as np
import io
import random
from datetime import datetime, timedelta

def gen_datetime(min_year=1900, max_year=datetime.now().year):
    # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random.random()

class TestModel(unittest.TestCase):

    def test_downloadCFPBDataset(self):
        tsm.downloadCFPBDataset()
        self.assertIsInstance(open('complaints.csv'), io.TextIOWrapper)
        with self.assertRaises(FileNotFoundError):
            open('complaints.csv.zip')

    def test_convertToOther(self):
        keepList = ['One','Two','Three']
        testList = ['Three', 'Four', 'Five', 'Two', '']
        testAns = ['Three','Other','Other','Two', 'Other']
        self.assertEqual(tsm.convertToOther('',[]), 'Other')
        self.assertEqual(tsm.convertToOther('Not', keepList), 'Other')
        self.assertEqual(tsm.convertToOther('One', keepList), 'One')
        testedList = [tsm.convertToOther(val, keepList) for val in testList]
        self.assertEqual(testAns, testedList)

    def test_cleanReduceConvert(self):
        valList = ['val'+ str(val) for val in range(30)]
        df = pd.DataFrame({'vals':valList})
        self.assertEqual(24, len(tsm.cleanReduceConvert(df, 'vals').value_counts()))
        self.assertIsInstance(tsm.cleanReduceConvert(df,'vals'), pd.Series)
        self.assertTrue(tsm.cleanReduceConvert(df, 'vals').notna().any())

    def test_entryOrNull(self):
        val1 = np.nan
        val2 = ''
        self.assertEqual(0.0, tsm.entryOrNull(val1))
        self.assertEqual(1.0, tsm.entryOrNull(val2))
        valList = [2, '12', np.nan, 'test', np.nan]
        df = pd.DataFrame({'vals':valList})
        testSeries = pd.Series(index=[1.0,0.0])
        self.assertEqual(df['vals'].apply(tsm.entryOrNull).value_counts().index[0], testSeries.index[0])
        self.assertEqual(df['vals'].apply(tsm.entryOrNull).value_counts().index[1], testSeries.index[1])

    def test_dtToCols(self):
        vals = [gen_datetime(), gen_datetime(), gen_datetime(), gen_datetime(), gen_datetime()]
        dtdf = pd.DataFrame({'test':vals})
        dtdf['test'] = pd.to_datetime(dtdf.test)
        tsm.dtToCols(dtdf, 'test')
        self.assertEqual(dtdf.columns.to_list(), ['test','test day', 'test month','test year'])
        self.assertTrue(dtdf['test day'].le(31).all())
        self.assertTrue(dtdf['test month'].le(12).all())

    def test_createDF(self):
        df = pd.DataFrame()



if __name__ == '__main__':
    unittest.main(exit=False)