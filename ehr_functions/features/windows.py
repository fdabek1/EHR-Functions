import pandas as pd


def calculate_days(df, name, date_ref):
    if isinstance(date_ref, pd.DataFrame):
        date_ref = date_ref.set_index('PatientID')
        date_ref = date_ref.to_dict()['InjuryDate']
        df[name + 'Days'] = (df['EncounterDate'] - df['PatientID'].map(date_ref)).dt.days
        return df

    df[name + 'Days'] = (df['EncounterDate'] - df[date_ref]).dt.days
    return df


# TODO - Expand this to accept counting of symptoms/diagnoses
# TODO - Optimize this method's calculations
def build_windows(df, windows, days_ref, flip_negative=False):
    """
    :param df:
    :param windows:
    :param flip_negative: A helper variable to flip windows without having to manually do it.
    :return:
    """

    if flip_negative:
        for w, window in enumerate(windows):
            temp = window[0]
            windows[w][0] = window[1] * -1
            windows[w][1] = temp * -1

    df = df[['PatientID', days_ref]]

    # noinspection PyShadowingNames
    # Assign the window index to each encounter
    def get_window_index(x):
        for w, window in enumerate(windows):
            if window[0] <= x <= window[1]:
                return w

        return -1

    df = df.assign(WindowIndex=df[days_ref].apply(lambda x: get_window_index(x)))

    # Delete any encounters that are outside of the windows
    df = df[df['WindowIndex'] > -1]

    for w in range(len(windows)):
        df['Window' + '_' + str(w)] = (df['WindowIndex'] == w).astype(int)

    df = df.drop(columns=['EventDays', 'WindowIndex'])
    df = df.groupby(['PatientID']).sum().reset_index()

    return df


if __name__ == '__main__':
    df = pd.DataFrame({
        'PatientID': [1, 1, 1, 1],
        'EventDays': [0, 5, 9, 15],
        'Diagnosis1': ['A', 'F', 'D', 'C'],
        'Diagnosis2': [None, 'B', 'B', 'A'],
        'Diagnosis3': [None, None, 'C', 'A'],
    })

    print(build_windows(df, [[0, 10], [10, 30]], 'EventDays'))
