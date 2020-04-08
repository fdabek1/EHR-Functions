from ehr_functions.features import windows
import pandas as pd


def test_calculate_days_string():
    df = pd.DataFrame({
        'PatientID': [1, 1, 1, 1],
        'EncounterDate': ['01/01/2020', '01/05/2020', '01/18/2020', '01/30/2020'],
        'InjuryDate': ['01/07/2020', '01/07/2020', '01/07/2020', '01/07/2020'],
        'Diagnosis': ['A', 'F', 'D', 'C'],
    })
    df['EncounterDate'] = pd.to_datetime(df['EncounterDate'])
    df['InjuryDate'] = pd.to_datetime(df['InjuryDate'])

    features = windows.calculate_days(df, 'Injury', 'InjuryDate')

    result = pd.DataFrame({
        'PatientID': [1, 1, 1, 1],
        'EncounterDate': ['01/01/2020', '01/05/2020', '01/18/2020', '01/30/2020'],
        'InjuryDate': ['01/07/2020', '01/07/2020', '01/07/2020', '01/07/2020'],
        'Diagnosis': ['A', 'F', 'D', 'C'],
        'InjuryDays': [-6, -2, 11, 23],
    })
    result['EncounterDate'] = pd.to_datetime(result['EncounterDate'])
    result['InjuryDate'] = pd.to_datetime(result['InjuryDate'])

    pd.testing.assert_frame_equal(features, result)


def test_calculate_days_dataframe():
    df = pd.DataFrame({
        'PatientID': [1, 1, 1, 1],
        'EncounterDate': ['01/01/2020', '01/05/2020', '01/18/2020', '01/30/2020'],
        'Diagnosis': ['A', 'F', 'D', 'C'],
    })
    df['EncounterDate'] = pd.to_datetime(df['EncounterDate'])

    lookup = pd.DataFrame({
        'PatientID': [1],
        'InjuryDate': ['01/07/2020'],
    })
    lookup['InjuryDate'] = pd.to_datetime(lookup['InjuryDate'])

    features = windows.calculate_days(df, 'Injury', lookup)

    result = pd.DataFrame({
        'PatientID': [1, 1, 1, 1],
        'EncounterDate': ['01/01/2020', '01/05/2020', '01/18/2020', '01/30/2020'],
        'Diagnosis': ['A', 'F', 'D', 'C'],
        'InjuryDays': [-6, -2, 11, 23],
    })
    result['EncounterDate'] = pd.to_datetime(result['EncounterDate'])

    pd.testing.assert_frame_equal(features, result)


def test_build_windows():
    df = pd.DataFrame({
        'PatientID': [1, 1, 1, 1],
        'EventDays': [0, 5, 9, 15],
        'Diagnosis1': ['A', 'F', 'D', 'C'],
        'Diagnosis2': [None, 'B', 'B', 'A'],
        'Diagnosis3': [None, None, 'C', 'A'],
    })

    features = windows.build_windows(df, [[0, 10], [10, 30]], 'EventDays')
    pd.testing.assert_frame_equal(features, pd.DataFrame({
        'PatientID': [1],
        'Window_0': [3],
        'Window_1': [1],
    }), check_dtype=False)
