from typing import Mapping, List, Any

import data


# Update dict of the current contests type with given contest
def getTotalTable(rows: Mapping[str, List[Any]], contests_type: str):

    for index in range(len(rows['name'])):
        if rows['name'][index] in data.order_of_key:
            while len(data.total_result[contests_type]) <= data.order_of_key[rows['name'][index]]:
                data.total_result[contests_type].append(0)
            data.total_result[contests_type][data.order_of_key[rows['name'][index]]] += rows['mark'][index]
        else:
            data.order_of_key[rows['name'][index]] = len(data.total_result['name'])
            data.total_result['name'].append(rows['name'][index])
            data.total_result[contests_type].append(rows['mark'][index])
