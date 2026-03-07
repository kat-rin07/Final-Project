import unittest

import data
import functions

#Tests for functions Written by Kathrin (mark when done/fixed)

class DataTest(unittest.TestCase):

#illness_cases test cases start here

    #Test 1 - illness_cases - Tests basic filtering information into dictionaries
    def test_illness_cases_1(self):
        record = [data.HealthRecord('001', 'Freshman', 'PCV', 'Flu'),
                  data.HealthRecord('002', 'Freshman', 'Santa Lucia','Common Cold'),
                  data.HealthRecord('003', 'Freshman', 'Santa Lucia', 'Common Cold')]
        result = functions.illness_cases(record)
        expected = {'Common Cold':2, 'Flu':1}
        self.assertEqual(result, expected)

    #Test 2 - illness_cases - Test single information input
    def test_illness_cases_2(self):
        record = [data.HealthRecord('001', 'Freshman', 'PCV', 'Flu')]
        result = functions.illness_cases(record)
        expected = {'Flu':1 }
        self.assertEqual(result, expected)

    #Test 3 - illness_cases - Tests empty input
    def test_illness_cases_3(self):
        record = []
        result = functions.illness_cases(record)
        expected = {}
        self.assertEqual(result, expected)

    #Test 4 - illness_cases - Tests same illness different records
    def test_illness_cases_4(self):
        record = [data.HealthRecord('001', 'Freshman', 'PCV', 'Flu'),
                  data.HealthRecord('002', 'Transfer', 'Santa Lucia','Flu')]
        result = functions.illness_cases(record)
        expected = {'Flu':2}
        self.assertEqual(result, expected)

    #Test 5 - illness_cases - test case sensitivity
    def test_illness_cases_5(self):
        record = [data.HealthRecord('001', 'Freshman', 'PCV', 'Flu'),
                  data.HealthRecord('002', 'Freshman', 'Santa Lucia','flu')]
        result = functions.illness_cases(record)
        expected = {'Flu':2}
        self.assertNotEqual(result, expected)

    #Test 6 - illness_cases - tests empty input for desired string
    def test_illness_cases_6(self):
        record = [data.HealthRecord('001', 'Freshman', 'PCV', ''),]
        result = functions.illness_cases(record)
        expected = {'':1}
        self.assertEqual(result, expected)


#illness_with_most_cases test cases start here

    #Test 1 - illness_with_most_cases - Tests basic input information into determining highest case
    def test_illness_with_most_cases_1(self):
        record = {'Common Cold':2, 'Flu':1}
        result = functions.illness_with_most_cases(record)
        expected = (['Common Cold'], 2)
        self.assertEqual(result, expected)

    #Test 2 - illness_with_most_cases - Tests a tie between cases
    def test_illness_with_most_cases_2(self):
        record = {'Common Cold':2, 'Flu':2, 'Covid-19':1}
        result = functions.illness_with_most_cases(record)
        expected = (['Common Cold', 'Flu'], 2)
        self.assertEqual(result, expected)

    #Test 3 - illness_with_most_cases - Tests multi-way tie and zero count
    def test_illness_with_most_cases_3(self):
        record = {'Common Cold':0, 'Flu':0, 'Covid-19':0}
        result = functions.illness_with_most_cases(record)
        expected = (['Common Cold', 'Flu', 'Covid-19'], 0)
        self.assertEqual(result, expected)

    #Test 4 - illness_with_most_cases - Tests empty dictionary
    def test_illness_with_most_cases_4(self):
        record = {}
        result = functions.illness_with_most_cases(record)
        expected = ([], 0)
        self.assertEqual(result, expected)

    #Test 5 - illness_with_most_cases - Tests case sensitivity
    def test_illness_with_most_cases_5(self):
        record = {'flu':1, 'Flu':1}
        result = functions.illness_with_most_cases(record)
        expected = (['flu', 'Flu'], 1)
        self.assertEqual(result, expected)

    #Test 6 - illness_with_most_cases - Tests big numbers
    def test_illness_with_most_cases_6(self):
        record = {'Flu': 9, 'Common Cold':10, 'Covid-19':100}
        result = functions.illness_with_most_cases(record)
        expected = (['Covid-19'], 100)
        self.assertEqual(result, expected)

#dorms test cases start here

    #Test 1 - dorms - Tests basic filtering information into dictionaries 
    def test_dorms_1(self):
        record = [data.HealthRecord('001', 'Freshman', 'PCV', 'Flu'),
                  data.HealthRecord('002', 'Freshman', 'Santa Lucia', 'Common Cold'),
                  data.HealthRecord('003', 'Freshman', 'Santa Lucia', 'Common Cold')]
        result = functions.dorms(record)
        expected = {'PCV': 1, 'Santa Lucia': 2}
        self.assertEqual(result, expected)

    #Test 2 - dorms - Tests for single information input
    def test_dorms_2(self):
        record = [data.HealthRecord('001', 'Freshman', 'PCV', 'Flu')]
        result = functions.dorms(record)
        expected = {'PCV': 1}
        self.assertEqual(result, expected)

    #Test 3 - dorms - Tests empty input
    def test_dorms_3(self):
        record = []
        result = functions.dorms(record)
        expected = {}
        self.assertEqual(result, expected)

    #Test 4 - dorms - Tests different participant information except for key input
    def test_dorms_4(self):
        record = [data.HealthRecord('001', 'Freshman', 'PCV', 'Flu'),
                  data.HealthRecord('002', 'Transfer', 'PCV', 'Common Cold')]
        result = functions.dorms(record)
        expected = {'PCV': 2}
        self.assertEqual(result, expected)

    #Test 5 - dorms - Tests case sensitivity
    def test_dorms_5(self):
        record = [data.HealthRecord('001', 'Freshman', 'santa lucia', 'Flu'),
                  data.HealthRecord('002', 'Freshman', 'Santa Lucia', 'Flu')]
        result = functions.illness_cases(record)
        expected = {'Santa Lucia': 1, 'santa lucia': 1}
        self.assertNotEqual(result, expected)

    #Test 6 - dorms - Tests empty input for desired string
    def test_dorms_6(self):
        record = [data.HealthRecord('001', 'Freshman', '', 'Common Cold'),]
        result = functions.dorms(record)
        expected = {'':1}
        self.assertEqual(result, expected)

#dorms_with_most_cases test cases start here

    #Test 1 - dorm_with_most_cases - Test basic input information in determining dorm with highest case
    def test_dorm_with_most_cases_1(self):
        record = {'PCV':2, 'Santa Lucia':1}
        result = functions.dorm_with_most_cases(record)
        expected = (['PCV'], 2)
        self.assertEqual(result, expected)

    #Test 2 - dorm_with_most_cases - Tests tie between cases
    def test_dorm_with_most_cases_2(self):
        record = {'PCV':2, 'Santa Lucia':2, 'Sequoia':1}
        result = functions.dorm_with_most_cases(record)
        expected = (['PCV', 'Santa Lucia'], 2)
        self.assertEqual(result, expected)

    #Test 3 - dorms_with_most_cases - Tests multi-way tie with zero counts
    def test_dorm_with_most_cases_3(self):
        record = {'PCV':0, 'Santa Lucia':0, 'Sequoia':0}
        result = functions.illness_with_most_cases(record)
        expected = (['PCV', 'Santa Lucia', 'Sequoia'], 0)
        self.assertEqual(result, expected)

    #Test 4 - dorms_with_most_cases - Tests empty input of dictionary
    def test_dorm_with_most_cases_4(self):
        record = {}
        result = functions.dorm_with_most_cases(record)
        expected = ([], 0)
        self.assertEqual(result, expected)

    #Test 5 - dorms_with_most_cases - Tests case sensitivity
    def test_dorm_with_most_cases_5(self):
        record = {'santa lucia':1, 'Santa Lucia':1}
        result = functions.dorm_with_most_cases(record)
        expected = (['santa lucia', 'Santa Lucia'], 1)
        self.assertEqual(result, expected)

    #Test 6 - dorms_with_most_cases - Tests big numbers
    def test_dorm_with_most_cases_6(self):
        record = {'PCV': 9, 'Santa Lucia':10, 'Cerro Vista':100}
        result = functions.dorm_with_most_cases(record)
        expected = (['Cerro Vista'], 100)
        self.assertEqual(result, expected)


#total_participants tests start here

    #Test 1 - total_participants - Tests multiple entries
    def test_total_participants_1(self):
        record = [data.HealthRecord('001', 'Freshman', 'PCV', 'Flu'),
                  data.HealthRecord('002', 'Freshman', 'PCV', 'Flu'),
                  data.HealthRecord('003', 'Freshman', 'PCV', 'Flu'),
                  data.HealthRecord('004', 'Freshman', 'PCV', 'Flu')]
        result = functions.total_participants(record)
        expected = 4
        self.assertEqual(result, expected)

    #Test 2 - total_participants - Tests empty entries
    def test_total_participants_2(self):
        record = []
        result = functions.total_participants(record)
        expected = 0
        self.assertEqual(result, expected)

    #Test 3 - total_participants - Tests single entry
    def test_total_participants_3(self):
        record = [data.HealthRecord('001', 'Freshman', 'PCV', 'Flu')]
        result = functions.total_participants(record)
        expected = 1
        self.assertEqual(result, expected)

    #Test 4 - total_participants - Tests different entries
    def test_total_participants_4(self):
        record = [data.HealthRecord('001', 'Freshman', 'PCV', 'Flu'),
                  data.HealthRecord('002', 'Junior', 'Cerro Vista', 'Flu')]
        result = functions.total_participants(record)
        expected = 2
        self.assertEqual(result, expected)

    #Tests 5 - total_participants - Tests empty string entries
    def test_total_participants_5(self):
        record = [data.HealthRecord('', '', '', '')]
        result = functions.total_participants(record)
        expected = 1
        self.assertEqual(result, expected)
