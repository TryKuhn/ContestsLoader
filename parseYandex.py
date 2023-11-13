from makeTable import normalise_file_yandex


def parseYandex(standings):
    if len(standings['rows']) != 0:
        score = max(int(standings['rows'][0]['score']), len(standings['titles']))
    else:
        score = 1

    return normalise_file_yandex(standings['rows'], score)
