from typing import Any, List, Mapping
from collections import defaultdict


# Grader [0; 10]
def get_mark(points: int, results: int) -> float:
    return round(points / results * 10, 2)


# Get dict with standing of the current contest
def normalise_file(file: List[Mapping[str, Any]], score: int) -> Mapping[str, list]:
    rows = defaultdict(list)

    for row in file:
        rows['name'].append(row['party']['members'][0]['name']
                            if 'name' in row['party']['members'][0] else
                            row['party']['members'][0][
                                'handle'])
        rows['points'].append(row['points'])
        rows['mark'].append(get_mark(row['points'], score))

    return rows
