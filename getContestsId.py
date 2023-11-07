import json
from typing import List


# Get Contests id as JSON-file (type of contests -> list of contests)
def get_contests_id() -> List[int]:
    contests_id = open('cache/id.json')
    dict_id = json.load(contests_id)
    contests_id.close()
    return dict_id
