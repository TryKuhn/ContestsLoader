import json
from pathlib import Path
from typing import List, Mapping


# Get Contests id as JSON-file (type of contests -> list of contests)
def get_contests_id() -> Mapping[str, Mapping[str, List[int]]]:
    if Path('cache/id.json').stat().st_size != 0:
        contests_id = open('cache/id.json')
        dict_id = json.load(contests_id)
        contests_id.close()
        return dict_id
    else:
        return dict()
