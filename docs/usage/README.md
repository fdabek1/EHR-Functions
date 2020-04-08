---
sidebarDepth: 2
---

# Usage

## Installation

> pip install ehr_functions


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

| PatientID | PatientAge | PatientGender | PatientService_A | PatientService_B | PatientService_C |
|:---------:|:----------:|:-------------:|:----------------:|:----------------:|:----------------:|
|     1     |     21     |       1       |         1        |         0        |         0        |
|     2     |     35     |       0       |         0        |         1        |         0        |
|     3     |     27     |       1       |         0        |         0        |         1        |
|     4     |     24     |       0       |         1        |         0        |         0        |

## Data Structure & Assumptions

There are some assumptions that are made about the structure of your data.

- PatientID
- train/val/test split

::: warning
This section is under construction
:::