from ehr_functions.features import demographics
import pandas as pd


def test_get_features():
    df = pd.DataFrame({
        'PatientID': [1, 2, 3, 4],
        'PatientAge': [21, 35, 27, 24],
        'PatientGender': ['M', 'F', 'M', 'F'],
        'PatientService': ['A', 'B', 'C', 'A'],
    })

    dems = demographics.get_features(df)

    pd.testing.assert_frame_equal(dems, pd.DataFrame({
        'PatientID': [1, 2, 3, 4],
        'PatientAge': [21, 35, 27, 24],
        'PatientGender': [1, 0, 1, 0],
        'PatientService_A': [1, 0, 0, 1],
        'PatientService_B': [0, 1, 0, 0],
        'PatientService_C': [0, 0, 1, 0],
    }))
