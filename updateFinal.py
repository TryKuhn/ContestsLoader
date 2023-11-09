import logging

import data


# TODO: exception-safety

# Get table with final results and normalise marks
def update_final():
    data.total_result['total'] = []
    for type_of_contests in data.total_result.keys():
        if type_of_contests == 'name' or type_of_contests == 'total':
            continue
        for index in range(len(data.total_result['name'])):
            while len(data.total_result[type_of_contests]) < len(data.total_result['name']):
                data.total_result[type_of_contests].append(0)

            data.total_result[type_of_contests][index] = round(data.total_result[type_of_contests][index] /
                                                               max(len(data.contests_id[type_of_contests]), 1), 2)
            mark = data.total_result[type_of_contests][index]

            while len(data.total_result['total']) < len(data.total_result['name']):
                data.total_result['total'].append(0.0)

            data.total_result['total'][index] += mark * data.coefficients[type_of_contests] \
                if type_of_contests in data.coefficients else 0

            if type_of_contests not in data.coefficients:
                logging.warning(f"{type_of_contests} is not in coefficients, given coefficient 0")

    for index in range(len(data.total_result['name'])):
        data.total_result['total'][index] = round(data.total_result['total'][index], 2)
