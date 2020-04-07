from ehr_functions.models import train_model
from ehr_functions.models.types._base import Model
import pandas as pd
import numpy as np


class FakeModel(Model):
    def __init__(self):
        super().__init__()

    def train(self, x, y):
        pass

    def predict(self, x):
        return (x > 30).astype(np.int).flatten()


def test_train_model_simple():
    df = pd.DataFrame({
        'PatientID': [1, 2, 3, 4],
        'PatientAge': [21, 27, 35, 24],
        'PatientGender': ['M', 'F', 'M', 'F'],
        'PatientService': ['A', 'B', 'C', 'A'],
        'Over30': [0, 0, 1, 0],
    })

    model, results = train_model(FakeModel(), df, 'Over30', features=['PatientAge'], return_results=True)
    train_pred, val_pred = results
    np.testing.assert_array_equal(train_pred, np.asarray([0, 1]))
    np.testing.assert_array_equal(val_pred, np.asarray([0]))


def test_train_model_simple_type():
    df = pd.DataFrame({
        'PatientID': [1, 2, 3, 4],
        'PatientAge': [21, 27, 35, 24],
        'PatientGender': ['M', 'F', 'M', 'F'],
        'PatientService': ['A', 'B', 'C', 'A'],
        'Over30': [0, 0, 1, 0],
        'Type': ['train', 'train', 'val', 'test'],
    })

    model, results = train_model(FakeModel(), df, 'Over30', features=['PatientAge'], return_results=True)
    train_pred, val_pred = results
    np.testing.assert_array_equal(train_pred, np.asarray([0, 0]))
    np.testing.assert_array_equal(val_pred, np.asarray([1]))


def test_train_model_multiple_output():
    df = pd.DataFrame({
        'PatientID': [1, 2, 3, 4],
        'PatientAge': [21, 27, 35, 24],
        'PatientGender': ['M', 'F', 'M', 'F'],
        'PatientService': ['A', 'B', 'C', 'A'],
        'Over30': [0, 0, 1, 0],
        'Under30': [1, 1, 0, 1],
        'Type': ['train', 'train', 'val', 'test'],
    })

    model, results = train_model(FakeModel(), df, ['Over30', 'Under30'], features=['PatientAge'], return_results=True)
    train_pred, val_pred = results
    np.testing.assert_array_equal(train_pred[0], np.asarray([0, 0]))
    np.testing.assert_array_equal(train_pred[1], np.asarray([0, 0]))

    np.testing.assert_array_equal(val_pred[0], np.asarray([1]))
    np.testing.assert_array_equal(val_pred[1], np.asarray([1]))


# def test_train_model_encounters():
#     patients = pd.DataFrame({
#         'PatientID': [1, 2, 3, 4],
#         'Type': ['train', 'train', 'val', 'test'],
#     })
#
#     encounters = pd.DataFrame({
#         'PatientID': [1, 1, 2, 3, 4],
#         'PatientAge': [21, 21, 35, 27, 24],
#         'PatientGender': ['M', 'M', 'F', 'M', 'F'],
#         'PatientService': ['A', 'A', 'B', 'C', 'A'],
#     })
#
#     model = train_model(FakeModel())
