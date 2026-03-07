
from data import HealthRecord
from data import Student
import data



#Functions go here!
#Marissa's Functions
def cases(records):
    count = {}
    for record in records:
        illness = record.illness
        if illness in count:
            count[illness] += 1
        else:
            count[illness] = 1
    return count

def most_cases(count):
    top_illness = []
    top_illness_count = 0
    for illness in count:
        if count[illness] > top_illness_count:
            top_illness_count = count[illness]
            top_illness = [illness]
        elif count[illness] ==  top_illness_count:
            top_illness.append(illness)

    return top_illness, top_illness_count
