
from data import HealthRecord
from data import Student
import data



#Functions go here!
#Marissa
def cases(records):
    count = {}
    for record in records:
        illness = record.illness
        if illness in count:
            count[illness] += 1
        else:
            count[illness] = 1
    return count