import data
from getTotalByType import getTotalTable
import pandas as pd
from parseCodeforces import parseCodeforces
from parseYandex import parseYandex


# Update all contests standings
def update_contests():
    for contest in data.contests_id.keys():
        for contest_system in data.contests_id[contest].keys():
            for contest_id in data.contests_id[contest][contest_system]:
                if contest_system == "Yandex":
                    standings = data.yaApi.get_standings(contest_id)
                    standings_dict = parseYandex(standings)
                elif contest_system == "Codeforces":
                    standings = data.cfApi.get_standings(contest_id)
                    standings_dict = parseCodeforces(standings)
                else:
                    raise RuntimeError(f"Incorrect system: {contest_system}")

                getTotalTable(standings_dict, contest)

                final_result_df = pd.DataFrame(standings_dict)
                final_result_df.to_excel(data.writer, f'contest{contest_id}')
