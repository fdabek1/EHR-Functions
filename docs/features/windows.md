# Windows

## calculate_days

```python
windows.calculate_days(df, name, date_ref)
```

Helper function to calculate the number of days between a reference event

### Arguments

- **df:** Pandas DataFrame
 
- **name:** The name of the result column (will be appended with "Days").

- **date_ref:**
    - *String:* The name of the column in `df` to reference against.
    - *Pandas DataFrame:* Contains two columns: PatientID and a date column as the reference date.


### Returns

- The same Pandas DataFrame, `df`, with an extra calculated column.

### Example

**String Example**

```python
from ehr_functions.features import windows
import pandas as pd 

df = pd.DataFrame({
    'PatientID': [1, 1, 1, 1],
    'EncounterDate': ['01/01/2020', '01/05/2020', '01/18/2020', '01/30/2020'],
    'InjuryDate': ['01/07/2020', '01/07/2020', '01/07/2020', '01/07/2020'],
    'Diagnosis': ['A', 'F', 'D', 'C'],
})

features = windows.calculate_days(df, 'Injury', 'InjuryDate')
print(features.head())
```

| PatientID | EncounterDate | InjuryDate | Diagnosis | InjuryDays |
|:---------:|:-------------:|:----------:|:---------:|:----------:|
|     1     |   2020-01-01  | 2020-01-07 |     A     |     -6     |
|     1     |   2020-01-05  | 2020-01-07 |     F     |     -2     |
|     1     |   2020-01-18  | 2020-01-07 |     D     |     11     |
|     1     |   2020-01-30  | 2020-01-07 |     C     |     23     |

**DataFrame Example**

```python
from ehr_functions.features import windows
import pandas as pd 

df = pd.DataFrame({
    'PatientID': [1, 1, 1, 1],
    'EncounterDate': ['01/01/2020', '01/05/2020', '01/18/2020', '01/30/2020'],
    'Diagnosis': ['A', 'F', 'D', 'C'],
})

lookup = pd.DataFrame({
    'PatientID': [1],
    'InjuryDate': ['01/07/2020'],
})

features = windows.calculate_days(df, 'Injury', lookup)
print(features.head())
```

| PatientID | EncounterDate | Diagnosis | InjuryDays |
|:---------:|:-------------:|:---------:|:----------:|
|     1     |   2020-01-01  |     A     |     -6     |
|     1     |   2020-01-05  |     F     |     -2     |
|     1     |   2020-01-18  |     D     |     11     |
|     1     |   2020-01-30  |     C     |     23     |

## build_windows

```python
windows.build_windows(df, windows, flip_negative=False)
```

A common technique to count the number of encounters that occur within each window/timeframe.  This method expects for a column that exist that contains the number of days since an event, where 0 is the event of interest to relate against.

### Arguments

- **df:** Pandas DataFrame
 
- **windows:** List of windows with the begin and end day values

- **days_ref:** Name of the column containing days to reference.

- **flip_negative:** A helper variable to multiply all windows by -1 rather than manually having to do it.


### Returns

- Pandas DataFrame with PatientID and a column for each window.

### Example

```python
from ehr_functions.features import windows
import pandas as pd 

df = pd.DataFrame({
    'PatientID': [1, 1, 1, 1],
    'EventDays': [0, 5, 9, 15],
    'Diagnosis1': ['A', 'F', 'D', 'C'],
    'Diagnosis2': [None, 'B', 'B', 'A'],
    'Diagnosis3': [None, None, 'C', 'A'],
})

features = windows.build_windows(df, [[0, 10], [10, 30]], 'EventDays')
print(features.head())
```

| PatientID | Window_0 | Window_1 |
|:---------:|:--------:|:--------:|
|     1     |     3    |     1    |