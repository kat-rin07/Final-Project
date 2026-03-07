
from data import HealthRecord
from data import Student
import data



#Functions go here!
#Marissa's Functions
def illness_cases(records):
    count = {}
    for record in records:
        illness = record.illness
        if illness in count:
            count[illness] += 1
        else:
            count[illness] = 1
    return count

def illness_with_most_cases(count):
    top_illness = []
    top_illness_count = 0
    for illness in count:
        if count[illness] > top_illness_count:
            top_illness_count = count[illness]
            top_illness = [illness]
        elif count[illness] ==  top_illness_count:
            top_illness.append(illness)

    return top_illness, top_illness_count

def dorms(records):
    dorm_count = {}
    for record in records:
        dorm = record.dorm
        if dorm in dorm_count:
            dorm_count[dorm] += 1
        else:
            dorm_count[dorm] = 1
    return dorm_count

def dorm_with_most_cases(dorm_count):
    top_dorm = []
    top_dorm_count = 0
    for dorm in dorm_count:
        if dorm_count[dorm] > top_dorm_count:
            top_dorm_count = dorm_count[dorm]
            top_dorm = [dorm]
        elif dorm_count[dorm] ==  top_dorm_count:
            top_dorm.append(dorm)

    return top_dorm, top_dorm_count