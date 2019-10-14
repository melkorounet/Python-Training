from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)

def gen_special_pybites_dates():
    PYBITES_BORN = datetime(year=2016, month=12, day=19)
    PYBITES_BORN_LIST = []
    while PYBITES_BORN < datetime(year=2019, month=2, day=20):
        PYBITES_BORN += timedelta(days=100)
        PYBITES_BORN_LIST.append(PYBITES_BORN)


    while PYBITES_BORN < datetime(year=2020, month=1, day=1):
        PYBITES_BORN += timedelta(days=365)
        PYBITES_BORN_LIST.append(PYBITES_BORN)

    print(PYBITES_BORN_LIST.sort())
    pass

gen_special_pybites_dates()