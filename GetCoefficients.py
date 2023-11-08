import json


# Get coefficients of marks
def get_coefficients():
    contests_coefficients = open('cache/coefficients.json')
    dict_coefficients = json.load(contests_coefficients)
    contests_coefficients.close()
    return dict_coefficients
