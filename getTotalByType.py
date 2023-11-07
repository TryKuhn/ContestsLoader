from typing import Mapping, List, Any


# Update dict of the current contests type with given contest
def getTotalTable(rows: Mapping[str, List[Any]], order_of_key: dict, contests_type: str, total_result: dict) \
        -> Mapping[str, List[Any]]:

    for index in range(len(rows['name'])):
        if rows['name'][index] in order_of_key:
            while len(total_result[contests_type]) <= order_of_key[rows['name'][index]]:
                total_result[contests_type].append(0)
            total_result[contests_type][order_of_key[rows['name'][index]]] += rows['mark'][index]
        else:
            order_of_key[rows['name'][index]] = len(total_result['name'])
            total_result['name'].append(rows['name'][index])
            total_result[contests_type].append(rows['mark'][index])

    return total_result
