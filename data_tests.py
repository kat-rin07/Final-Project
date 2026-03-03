import data
import unittest

#Test for Classes started by Kathrin (mark done when checked/or fixed)
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
                         "Student('Participant 1', 'Freshman', 'Santa Lucia')"
)