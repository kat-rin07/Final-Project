import data
import unittest

from data import HealthRecord


#Test for Classes Written by Kathrin (mark done when checked/or fixed)
#Test for Classes debugged/fixed by ___

class DataTests(unittest.TestCase):

#Test 1 - Class Student
    def test_Student(self):
        student = data.Student('Participant 1', 'Freshman', 'Sierra Madre')
        self.assertEqual(student.id, 'Participant 1')
        self.assertEqual(student.year, 'Freshman')
        self.assertEqual(student.dorm, 'Sierra Madre')

#Test 2 - Class Student
    def test_Student_eq_1(self):
        student1 = data.Student('Participant 1', 'Freshman', 'Sierra Madre')
        student2 = data.Student('Participant 1', 'Freshman', 'Sierra Madre')
        self.assertEqual(student1, student2)


#Test 3 - Class Student

    def test_Student_eq_2(self):
        student = data.Student('Participant 1', 'Freshman', 'Sierra Madre')
        self.assertEqual(student, student)

#Test 4 - Class Student

    def test_Student_eq_3(self):
        student1 = data.Student('Participant 1', 'Freshman', 'Sierra Madre')
        student2 = data.Student('Participant 2', 'Sophmore', 'Poly Canyon Village')
        self.assertNotEqual(student1, student2)

#Test 5 - Class Student (can remove)

    def test_Student_eq_4(self):
        student = data.Student('Participant 1', 'Freshman', 'Santa Lucia')
        other = 20
        self.assertNotEqual(student, other)

#Test 6 - Class Student

    def test_Student_repr(self):
        student = data.Student('Participant 1', 'Freshman', 'Santa Lucia')
        self.assertEqual(repr(student),
                         "Student('Participant 1', 'Freshman', 'Santa Lucia')")

#Test 1 - Class HealthRecord

    def test_HealthRecord(self):
        record = data.HealthRecord('Participant 1', 'Freshman', 'Santa Lucia', 'Common Cold', '3')
        self.assertEqual(record.id, 'Participant 1')
        self.assertEqual(record.year, 'Freshman')
        self.assertEqual(record.dorm, 'Santa Lucia')
        self.assertEqual(record.illness, 'Common Cold')
        self.assertEqual(record.frequency, '3')

#Test 2 - Class HealthRecord
    def test_HealthRecord_eq_1(self):
        student_1 = data.HealthRecord('Participant 1', 'Freshman', 'Santa Lucia', 'Common Cold', '3')
        student_2 = data.HealthRecord('Participant 1', 'Freshman', 'Santa Lucia', 'Common Cold', '3')
        self.assertEqual(student_1, student_2)

#Test 3 - Class HealthRecord

    def test_HealthRecord_eq_2(self):
        student = data.HealthRecord('Participant 1', 'Freshman', 'Santa Lucia', 'Common Cold', '3')
        self.assertEqual(student, student)

#Test 4 - Class Health Record
    def test_HealthRecord_eq_3(self):
        student = data.HealthRecord('Participant 1', 'Freshman', 'Santa Lucia', 'Common Cold', '3')
        student1 = data.HealthRecord('Participant 2', 'Transfer', "Poly Canyon Village", 'Flu', '1')
        self.assertNotEqual(student, student1)

#Test 5 - Class Health Record
    def test_HealthRecord_eq_4(self):
        student = data.HealthRecord('Participant', 'Freshman', 'Santa Lucia', 'Common Cold', '3')
        other = 10
        self.assertNotEqual(student, other)

    def test_HealthRecord_repr(self):
        student = data.HealthRecord('Participant', 'Freshman', 'Santa Lucia', 'Common Cold', '3')
        self.assertEqual(repr(student),
                         "HealthRecord('Participant', 'Freshman', 'Santa Lucia', 'Common Cold', '3')")
