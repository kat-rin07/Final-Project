from functions import (dorm_with_most_cases, illness_with_most_cases,
                       illness_cases, dorms, total_participants, display)
from dataset import records

#main.py made by Kathrin and Marissa
def main():

    illness_counts = illness_cases(records)
    top_illness, top_illness_count = illness_with_most_cases(illness_counts)

    dorm_counts = dorms(records)
    top_dorm, top_dorm_count = dorm_with_most_cases(dorm_counts)

    participants = total_participants(records)

    display(
        illness_counts,
        participants,
        top_dorm,
        top_dorm_count,
        dorm_counts,
        top_illness,
        top_illness_count,
    )

    print("\nIncrease sanitation and airflow in {} and take care of yourself to lessen cases of {}.".format(top_dorm, top_illness))

if __name__ == '__main__':
    main()