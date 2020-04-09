---
home: true
heroImage: /hero.png
actionText: Get Started →
actionLink: /usage/
footer: 
---

## EHR Functions

> A library of useful EHR related functions.

## About

This is a library of useful EHR functions for use within Python, especially when using Jupyter notebooks.

When utilizing Jupyter notebooks for processing data and training models I found myself copying the same code between notebooks.  This code consisted of steps to split my data, create a model, compute some metrics, etc.; and thus the notebooks became very long with little focus on the actual analysis.  Therefore, this set of functions were created to allow for a focus on analysis and to abstract away the process of cleaning data and running models.

::: warning
The documentation is still being written out so a lot of sections are left blank.
:::

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
