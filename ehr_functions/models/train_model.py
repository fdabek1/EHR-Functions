from sklearn.model_selection import train_test_split
# from ehr_functions.visualization.visualize import show_results
import pandas as pd
import numpy as np
import copy


def show_results(*kwargs):
    pass


def __split(x, y):
    x_train, x, y_train, y = train_test_split(x, y, test_size=0.33, random_state=3)
    x_val, x_test, y_val, y_test = train_test_split(x, y, test_size=0.5, random_state=3)
    return x_train, x_val, y_train, y_val


# def split_stats(x, y):
#     x_train, x_test, y_train, y_test = split(x, y)
#
#     print('Percent Positive Train:', (len([True for val in y_train if val]) / len(y_train)))
#     print('Percent Positive Test:', (len([True for val in y_test if val]) / len(y_test)))
#
#
# def __split_stats_complex(outcome, df):
#     print(outcome)
#     print('Percent Positive Train:', (len([True for val in y_train if val]) / len(y_train)))
#     print('Percent Positive Test:', (len([True for val in y_test if val]) / len(y_test)))
#     print('')
#
#
# def split_stats_complex(outcomes, lookup):
#     for col in outcome_columns:
#         __split_stats_complex(col, df)


def __train_model(model, train_data, val_data):
    x_train, y_train = train_data
    x_val, y_val = val_data

    model.train(x_train, y_train)
    train_pred = model.predict(x_train)
    val_pred = model.predict(x_val)

    return model, (train_pred, val_pred)


def __is_multiple_output(outcome):
    if isinstance(outcome, str) or isinstance(outcome, pd.Series):
        return False

    if isinstance(outcome, list) or (isinstance(outcome, pd.DataFrame) and outcome.shape[1] > 2):
        return True

    raise ValueError('Unknown type for outcome in train_model.')


def __get_outcomes(df, outcome):
    if isinstance(outcome, str):
        return df[outcome].values

    if isinstance(outcome, list):
        return df[outcome].values

    if isinstance(outcome, pd.Series):
        return outcome.values

    if isinstance(outcome, pd.DataFrame) and outcome.shape[1] > 2:
        return outcome[[col for col in outcome.columns if col != 'PatientID']].values

    raise ValueError('Unknown type for outcome in train_model.')


def __get_x_y(df, features, outcome):
    if 'Type' in df.columns:
        df_train = df[df['Type'] == 'train']
        df_val = df[df['Type'] == 'val']

        x_train = df_train[features].values
        x_val = df_val[features].values

        y_train = __get_outcomes(df_train, outcome)
        y_val = __get_outcomes(df_val, outcome)
    else:
        x = df[features].values
        y = __get_outcomes(df, outcome)

        x_train, x_val, y_train, y_val = __split(x, y)

    return x_train, x_val, y_train, y_val


def train_model(model, df: pd.DataFrame, outcome, features=None, data_type=None,
                return_results=False, print_results=True):
    if features is None:
        features = [col for col in df.columns if col != 'PatientID']
        if isinstance(outcome, str):
            features.remove(outcome)

        if isinstance(outcome, list):
            for col in outcome:
                features.remove(col)

    if data_type is not None:
        df = pd.merge(df, data_type[['PatientID', 'Type']], on='PatientID', how='outer')

    if isinstance(outcome, pd.DataFrame) or (data_type is not None and isinstance(outcome, pd.DataFrame)):
        df = pd.merge(df, outcome, on='PatientID', how='outer')
        outcome = [col for col in outcome if col != 'PatientID']
        if len(outcome) == 1:
            outcome = outcome[0]

    if __is_multiple_output(outcome) and not model.multiple_output:
        models = []
        train_pred, val_pred = [], []
        for col in outcome:
            x_train, x_val, y_train, y_val = __get_x_y(df, features, col)

            m, results = __train_model(copy.deepcopy(model), (x_train, y_train), (x_val, y_val))
            models.append(m)

            train_pred.append(results[0])
            val_pred.append(results[1])

        if return_results:
            return models, (train_pred, val_pred)

        return models
    else:
        x_train, x_val, y_train, y_val = __get_x_y(df, features, outcome)

        model, results = __train_model(model, (x_train, y_train), (x_val, y_val))
        if return_results:
            return model, results

        return model
