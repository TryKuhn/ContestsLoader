from main import total_result, contests_id


# Get table with final results and normalise marks
def update_final(coefficients):
    for type_of_contests in coefficients.keys():
        for index in range(len(total_result['names'])):
            total_result[type_of_contests] = round(total_result[type_of_contests] / len(contests_id[type_of_contests]), 2)
            mark = total_result[type_of_contests]

            if len(total_result['total']) <= index:
                total_result['total'].append(coefficients[type_of_contests] * mark)
            else:
                total_result['total'] += coefficients[type_of_contests] * mark
