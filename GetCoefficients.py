import json
from pathlib import Path
from typing import Mapping


# Get coefficients.json of marks
def get_coefficients() -> Mapping[str, int]:
    if Path('cache/coefficients.json').stat().st_size != 0:
        contests_coefficients = open('cache/coefficients.json')
        dict_coefficients = json.load(contests_coefficients)
        contests_coefficients.close()
        return dict_coefficients
    else:
        return dict()
