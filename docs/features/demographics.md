# Demographics

## get\_features

```python
demographics.get_features(df, cols=None)
```

### Arguments

- **df:** Pandas DataFrame
 
- **cols:** A list of the columns to extract. Defaults to ['PatientAge', 'PatientGender', 'PatientCategory'].


### Returns

- Pandas DataFrame containing PatientID and feature columns in numeric formats.

### Example

```python
from ehr_functions.features import demographics
import pandas as pd 

df = pd.DataFrame({
    'PatientID': [1, 2, 3, 4],
    'PatientAge': [21, 35, 27, 24],
    'PatientGender': ['M', 'F', 'M', 'F'],
    'PatientCategory': ['A', 'B', 'C', 'A'],
})

dems = demographics.get_features(df)
print(dems.head())
```

| PatientID | PatientAge | PatientGender | PatientCategory_A | PatientCategory_B | PatientCategory_C |
|:---------:|:----------:|:-------------:|:-----------------:|:-----------------:|:-----------------:|
|     1     |     21     |       1       |         1         |         0         |         0         |
|     2     |     35     |       0       |         0         |         1         |         0         |
|     3     |     27     |       1       |         0         |         0         |         1         |
|     4     |     24     |       0       |         1         |         0         |         0         |