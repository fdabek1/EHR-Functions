# Codes

## get_nth_occurrence

```python
codes.get_nth_occurrence(df, codes, nth=0)
```

### Arguments

- **df:** Pandas DataFrame
 
- **codes:** A list of diagnosis codes to search for, can optionally be a single string.

- **nth:** An integer representing the nth occurrence to search for (0 indexed so 0 indicates the first).


### Returns

- Pandas DataFrame with two columns:
    - PatientID
    - EncounterDate corresponding to the date of the nth occurrence

### Example

```python
from ehr_functions.features import codes
import pandas as pd 

df = pd.DataFrame({
    'PatientID': [1, 1, 2, 2],
    'EncounterDate': ['01/01/2020', '01/05/2020', '01/01/2020', '01/02/2020'],
    'Diagnosis1': ['A', 'F', 'D', 'C'],
    'Diagnosis2': [None, 'B', 'B', 'A'],
    'Diagnosis3': [None, None, 'C', 'A'],
})
df['EncounterDate'] = pd.to_datetime(df['EncounterDate'])

dates = codes.get_nth_occurrence(df, 'B')
print(dates.head())
```

| PatientID | EncounterDate |
|:---------:|:-------------:|
|     1     |   2020-01-05  |
|     2     |   2020-01-01  |


## tag_had_code

```python
codes.tag_had_code(df, name, codes, nth=None)
```

Helper method to tag a list of encounters with whether or not a patient had a code.

### Arguments

- **df:** Pandas DataFrame
 
- **name:** Name of the new boolean column to create

- **codes:** A list of diagnosis codes to search for, can optionally be a single string.

- **nth:** An integer representing the nth occurrence to search for (0 indexed so 0 indicates the first).


### Returns

- Pandas DataFrame with two columns:
    - PatientID
    - EncounterDate corresponding to the date of the nth occurrence

### Example

```python
from ehr_functions.features import codes
import pandas as pd 

df = pd.DataFrame({
    'PatientID': [1, 1, 2, 2],
    'EncounterDate': ['01/01/2020', '01/05/2020', '01/01/2020', '01/02/2020'],
    'Diagnosis1': ['A', 'F', 'D', 'C'],
    'Diagnosis2': [None, 'B', 'B', 'A'],
    'Diagnosis3': [None, None, 'C', 'A'],
})
df['EncounterDate'] = pd.to_datetime(df['EncounterDate'])

dates = codes.get_nth_occurrence(df, 'B')
print(dates.head())
```

| PatientID | EncounterDate |
|:---------:|:-------------:|
|     1     |   2020-01-05  |
|     2     |   2020-01-01  |