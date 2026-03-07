import unittest

import data
import functions

#Tests for functions Written by Kathrin (mark when done/fixed)

class DataTest(unittest.TestCase):

    #Test 1 - Illness_Cases
    def test_illness_cases_1(self):
        record = [data.HealthRecord('001', 'Freshman', 'PCV', 'Flu'),
                  data.HealthRecord('002', 'Freshman', 'Santa Lucia','Common Cold')]
        result = functions.illness_cases(record)
        expected = {'Common Cold':1, 'Flu':1}
        self.assertEqual(result, expected)
