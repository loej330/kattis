import sys
from datetime import datetime

cases = sys.stdin.readlines()[1:]
get_datetime = lambda d : datetime.strptime(d, "%Y/%m/%d")
min_study = datetime(2010, 1, 1)
min_birth = datetime(1991, 1, 1)

for case in cases:
    [name, study, birth, hours] = case.split(" ")
    v_study = get_datetime(study) >= min_study
    v_birth = get_datetime(birth) >= min_birth
    v_hours = int(hours) < 41

    if v_study or v_birth: print(name, "eligible")
    elif v_hours: print(name, "coach petitions")
    else: print(name, "ineligible")