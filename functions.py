
from data import HealthRecord
from data import Student
import data


#Functions go here!
#Marissa's Functions
def illness_cases(records:list[HealthRecord]) -> dict:
    count = {}
    for record in records:
        illness = record.illness
        if illness in count:
            count[illness] += 1
        else:
            count[illness] = 1
    return count

def illness_with_most_cases(count:dict):
    top_illness = []
    top_illness_count = 0
    for illness in count:
        if count[illness] > top_illness_count:
            top_illness_count = count[illness]
            top_illness = [illness]
        elif count[illness] ==  top_illness_count:
            top_illness.append(illness)

    return top_illness, top_illness_count

def dorms(records:list[HealthRecord]) -> dict:
    dorm_count = {}
    for record in records:
        dorm = record.dorm
        if dorm in dorm_count:
            dorm_count[dorm] += 1
        else:
            dorm_count[dorm] = 1
    return dorm_count

def dorm_with_most_cases(dorm_count:dict):
    top_dorm = []
    top_dorm_count = 0
    for dorm in dorm_count:
        if dorm_count[dorm] > top_dorm_count:
            top_dorm_count = dorm_count[dorm]
            top_dorm = [dorm]
        elif dorm_count[dorm] ==  top_dorm_count:
            top_dorm.append(dorm)

    return top_dorm, top_dorm_count

#Made by Kathrin
#This function when given a list should return an integer
#The input is the dataset records list and the output is the total count of how many records are in the dataset
def total_participants(records: list[object]) -> int:
    total = len(records)
    return total


def display(count, total, top_dorm, top_dorm_count, dorm_count, top_illness, top_illness_count):
    print("\n=== Health Report ===")
    print("\nTotal Participants: ", total)
    print("\n--- Illness Breakdown ---")
    print("Illness Cases: ", count)
    print("Illness with the most cases: ", top_illness)
    print("Cases: ", top_illness_count)

    print("\n---Dorm Breakdown ---")
    print("Dorm Cases: ", dorm_count )
    print("Dorm with most cases: ", top_dorm)
    print("Number of Cases in dorm: ", top_dorm_count)