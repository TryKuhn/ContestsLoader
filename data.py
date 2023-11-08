from collections import defaultdict

import pandas as pd

from apiCodeforces import CodeforcesApi

# Api
api = CodeforcesApi()
api.load_info('https://codeforces.com')

# Database
total_result = defaultdict(list)
coefficients = dict()
order_of_key = dict()
contests_id = list()
writer = pd.ExcelWriter('standings.xlsx')


# Database init
def init():
    global total_result
    total_result = defaultdict(list)

    global coefficients
    coefficients = dict()

    global order_of_key
    order_of_key = dict()

    global contests_id
    contests_id = list()

    global writer
    writer = pd.ExcelWriter('standings.xlsx')
