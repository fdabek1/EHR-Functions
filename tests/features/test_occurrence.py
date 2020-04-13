from ehr_functions.features import occurrence
import pandas as pd


def test_nth_occurrence():
    df = pd.DataFrame({
        'PatientID': [1, 1, 2, 2],
        'EncounterDate': ['01/01/2020', '01/05/2020', '01/01/2020', '01/02/2020'],
        'Diagnosis1': ['A', 'F', 'D', 'C'],
        'Diagnosis2': [None, 'B', 'B', 'A'],
        'Diagnosis3': [None, None, 'C', 'A'],
    })
    df['EncounterDate'] = pd.to_datetime(df['EncounterDate'])
    dates = occurrence.get_nth_occurrence(df, 'B')

    result = pd.DataFrame({
        'PatientID': [1, 2],
        'EncounterDate': ['01/05/2020', '01/01/2020'],
    })
    result['EncounterDate'] = pd.to_datetime(result['EncounterDate'])

    pd.testing.assert_frame_equal(dates, result)
