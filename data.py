from collections import defaultdict

import pandas as pd

from apiCodeforces import CodeforcesApi
from apiYandex import YandexApi

# Yandex Api
yaApi = YandexApi(host='https://api.contest.yandex.net/api/public/v2/api-docs?group=v2')
yaApi.login()

# Codeforces Api
cfApi = CodeforcesApi(host='https://codeforces.com')
cfApi.login('https://codeforces.com')

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
