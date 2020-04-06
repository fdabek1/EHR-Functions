# EHR-Functions

## What is this?

A library containing useful EHR related functions for use within Python data analysis.

## Installation

> pip install ehr-functions

## Example

```python
from ehr_functions.features import demographics
import pandas as pd 

df = pd.DataFrame({
    'PatientID': [1, 2, 3, 4],
    'PatientAge': [21, 35, 27, 24],
    'PatientGender': ['M', 'F', 'M', 'F'],
    'PatientService': ['A', 'B', 'C', 'A'],
})

dems = demographics.get_features(df)
print(dems.head())
```

Output

| PatientID | PatientAge | PatientGender | PatientService_A | PatientService_B | PatientService_C |
|:---------:|:----------:|:-------------:|:----------------:|:----------------:|:----------------:|
|     1     |     21     |       1       |         1        |         0        |         0        |
|     2     |     35     |       0       |         0        |         1        |         0        |
|     3     |     27     |       1       |         0        |         0        |         1        |
|     4     |     24     |       0       |         1        |         0        |         0        |

