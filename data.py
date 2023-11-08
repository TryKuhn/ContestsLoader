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
