import functions
import dataset

cases = functions.illness_cases(dataset.records)
top_illness, top_illness_count = functions.illness_with_most_cases(cases)
print("most illness:", top_illness)
print("most illness count:", top_illness_count)