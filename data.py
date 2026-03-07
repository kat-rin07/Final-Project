

#(Classes Created by Kathrin, mark done when checked and/or fixed)
#(Classes fixed/debugged by ___)

#Representation of a student, parent class
class Student:

    #Intialize a new Student object
    #Input: the student's participant ID as a string
    #Input: the student's year as a string
    #Input: the student's dorm as a string
    def __init__(self, id, year, dorm):
        self.id = id
        self.year = year
        self.dorm = dorm

    #Developer-friendly string representation of the object.
    #Input: Student information that a string representation is desired
    #Output: string representation
    def __repr__(self):
        return "Student('{}', '{}', '{}')".format(self.id, self.year, self.dorm)
        #alternative code in f-string:
        #return f"Student('{self.id}', '{self.year}', '{self.dorm}')"


    #Compare the student object with another value to determine equality
    #input: Student against which to compare
    #input_2: Another value to compare to student
    #output: boolean indicating equality
    def __eq__(self, other):
        return (self is other or
                type(other) == Student and
                self.id == other.id and
                self.year == other.year and
                self.dorm == other.dorm)



#Representation of a health record, child class using student object
class HealthRecord(Student):


    #Intialize HealthRecords object with set up from parent class
    #input: the student objects id, year, and dorm from student class
    #input: the student's illness
    #input: the student's frequency of illness
    def __init__(self, id, year, dorm, illness, frequency: int):
        super().__init__(id, year, dorm)
        self.illness = illness


    #Develper-friendly string representation of the object
    #input: HealthRecord for which a string representation is desired
    #output: string representation
    def __repr__(self):
        return "HealthRecord('{}', '{}', '{}', '{}')".format(self.id, self.year, self.dorm, self.illness)

        #Alternative code in f-string but may not be developer friendly???:
        #return f"HealthRecord('{self.id}', '{self.year}', '{self.dorm}', '{self.illness}', '{self.frequency}')"


    #Compare the HealthRecord object with another value to determine equality.
    #input: HealthRecord which to compare
    #input_2: Another value to compare to the HealthRecord
    #output: boolean indicating equality
    def __eq__(self, other):
        return (self is other or
                type(other) == HealthRecord and
                self.id == other.id and
                self.year == other.year and
                self.dorm == other.dorm and
                self.illness == other.illness)

        #alternative version of code
        #return (self.id, self.year, self.dorm, self.frequency) == (other.id, other.year, other.dorm, other.frequency)