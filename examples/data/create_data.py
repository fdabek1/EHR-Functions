import pandas as pd
import random
import time


# Source: https://stackoverflow.com/a/553320/556935
def str_time_prop(start, end, date_format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, date_format))
    etime = time.mktime(time.strptime(end, date_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(date_format, time.localtime(ptime))


def random_date(start, end):
    return str_time_prop(start, end, '%m/%d/%Y', random.random())


def basic(n=1000):
    data = {
        'PatientID': [],
        'PatientAge': [],
        'PatientGender': [],
        'PatientCategory': [],
    }

    for i in range(1, n + 1):
        data['PatientID'].append(i)
        data['PatientAge'].append(random.randint(18, 100))
        data['PatientGender'].append(random.choice(['M', 'F']))
        data['PatientCategory'].append(random.choice(['A', 'B', 'C']))

    df = pd.DataFrame(data)
    df.to_csv('basic.csv', index=False)


def encounters(n=1000):
    data = {
        'PatientID': [],
        'PatientAge': [],
        'PatientGender': [],
        'PatientCategory': [],
        'EncounterDate': [],
        'Diagnosis1': [],
        'Diagnosis2': [],
        'Diagnosis3': [],
    }

    for i in range(1, n + 1):
        age = random.randint(18, 100)
        gender = random.choice(['M', 'F'])
        category = random.choice(['A', 'B', 'C'])
        for _ in range(random.randint(2, 15)):  # Random number of encounters
            date = random_date('01/01/2015', '12/31/2019')
            year = int(date[-4:])
            data['PatientID'].append(i)
            data['PatientAge'].append(age + (year - 2015))
            data['PatientGender'].append(gender)
            data['PatientCategory'].append(category)
            data['EncounterDate'].append(date)
            data['Diagnosis1'].append(random.choice(['A', 'B', 'C']) + random.choice(['A', 'B', 'C']))
            data['Diagnosis2'].append(random.choice(['A', 'B', 'C']) + random.choice(['A', 'B', 'C']))
            data['Diagnosis3'].append(random.choice(['A', 'B', 'C']) + random.choice(['A', 'B', 'C']))

    df = pd.DataFrame(data)
    df.to_csv('encounters.csv', index=False)


if __name__ == '__main__':
    random.seed(3)
    basic()
    encounters()
