from makeTable import normalise_file_codeforces


def parseCodeforces(standings):
    score = len(standings['problems'])
    if standings['contest']['type'] == 'IOI':
        score = 0
        if len(standings['rows']) != 0:
            for problem in standings['rows'][0]['problemResults']:
                score += int(problem['points'])
        if score == 0:
            score = 1

    return normalise_file_codeforces(standings['rows'], score)
