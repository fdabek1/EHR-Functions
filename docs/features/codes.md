# Codes

## clean

```python
codes.clean(df, cols=None)
```

Removes spaces, special characters, and optional extenders.

### Arguments

- **df:** Pandas DataFrame
 
- **cols:** The columns to convert, defaults to `['Diagnosis1', 'Diagnosis2', 'Diagnosis3']` when `None`.

### Returns

- Pandas DataFrame with cleaned columns.

### Example

```python
from ehr_functions.features import codes
import pandas as pd 

df = pd.DataFrame({
    'PatientID': [1, 2, 3, 4],
    'Diagnosis1': ['0011 ', 'A00912  ', ' 0053', ' 0065 '],
    'Diagnosis2': ['A014 1', '008.44', None, None],
    'Diagnosis3': [None, None, '0011', None],
})

df = codes.clean(df)
print(df.head())
```

| PatientID | Diagnosis1 | Diagnosis2 | Diagnosis3 |
|:---------:|:----------:|:----------:|:----------:|
|     1     |    0011    |    A014    |            |
|     2     |   A00912   |    00844   |            |
|     3     |    0053    |            |    0011    |
|     4     |    0065    |            |            |

## simplify

```python
codes.simplify_codes(df, n=3, cols=None)
```

Cuts the code strings to a certain `n` characters.  This is useful for when simplifying ICD 9 or 10 codes to their base.

### Arguments

- **df:** Pandas DataFrame

- **n:** The number of characters to cut the string to.

- **cols:** The columns to convert, defaults to `['Diagnosis1', 'Diagnosis2', 'Diagnosis3']` when `None`.
 
### Returns

- Pandas DataFrame with the columns simplified.

### Example

```python
from ehr_functions.features import codes
import pandas as pd 

df = pd.DataFrame({
    'PatientID': [1, 2, 3, 4],
    'Diagnosis1': ['0011', 'A00912', '0053', '0065'],
    'Diagnosis2': ['A014', '00844', None, None],
    'Diagnosis3': [None, None, '0011', None],
})

df = codes.simplify(df)
print(df.head())
```

| PatientID | Diagnosis1 | Diagnosis2 | Diagnosis3 |
|:---------:|:----------:|:----------:|:----------:|
|     1     |     001    |     A01    |            |
|     2     |     A00    |     008    |            |
|     3     |     005    |            |     001    |
|     4     |     006    |            |            |

## convert\_to\_icd10

```python
codes.convert_to_icd10(df, cols=None)
```

::: warning
This is only for ICD diagnosis codes.
:::

### Arguments

- **df:** Pandas DataFrame
 
- **cols:** The columns to convert, defaults to `['Diagnosis1', 'Diagnosis2', 'Diagnosis3']` when `None`.

### Returns

- Pandas DataFrame with the columns converted.

### Example

```python
from ehr_functions.features import codes
import pandas as pd 

df = pd.DataFrame({
    'PatientID': [1, 2, 3, 4],
    'Diagnosis1': ['0011', 'A009', '0053', '0065'],
    'Diagnosis2': ['A014', '00844', None, None],
    'Diagnosis3': [None, None, '0011', None],
})

df = codes.convert_to_icd10(df)
print(df.head())
```

| PatientID | Diagnosis1 | Diagnosis2 | Diagnosis3 |
|:---------:|:----------:|:----------:|:----------:|
|     1     |    A001    |    A014    |            |
|     2     |    A009    |    A046    |            |
|     3     |    A058    |            |    A001    |
|     4     |    A066    |            |            |


## convert\_to\_icd9

```python
codes.convert_to_icd9(df, cols=None)
```

::: warning
This is only for ICD diagnosis codes.
:::

### Arguments

- **df:** Pandas DataFrame
 
- **cols:** The columns to convert, defaults to `['Diagnosis1', 'Diagnosis2', 'Diagnosis3']` when `None`.

### Returns

- Pandas DataFrame with the columns converted.

### Example

```python
from ehr_functions.features import codes
import pandas as pd 

df = pd.DataFrame({
    'PatientID': [1, 2, 3, 4],
    'Diagnosis1': ['0011', 'A009', '0053', '0065'],
    'Diagnosis2': ['A014', '00844', None, None],
    'Diagnosis3': [None, None, '0011', None],
})

df = codes.convert_to_icd10(df)
print(df.head())
```

| PatientID | Diagnosis1 | Diagnosis2 | Diagnosis3 |
|:---------:|:----------:|:----------:|:----------:|
|     1     |    0011    |    0029    |            |
|     2     |    0019    |    00844   |            |
|     3     |    0053    |            |    0011    |
|     4     |    0065    |            |            |



## get\_ccs\_mapping

```python
codes.get_ccs_mapping(name, code_type=10, level=None, data_type='dx')
```

::: details Sources
[CCS ICD-9](https://www.hcup-us.ahrq.gov/toolssoftware/ccs/ccs.jsp)

[CCS ICD-10 Diagnoses](https://www.hcup-us.ahrq.gov/toolssoftware/ccs10/ccs_dx_icd10cm_2019_1.zip)

[CCS ICD-10 Procedures](https://www.hcup-us.ahrq.gov/toolssoftware/ccs10/ccs10.jsp)
:::

### Arguments

- **name:** 
    - *String:* The name of the CCS level (e.g. `1.1`).
    - *List:* A list of string names of the CCS level.
    
- **code_type:** Whether to use ICD `9` or `10`.

- **level:** The CCS level to utilize:
    - **None:** Single level
    - **1:** Level 1 of multi-level
    - **2:** Level 2 of multi-level

- **data_type:** The type of icd (`dx` or `pr`).

### Returns

- ICD codes for the given level:
    - List of codes, if **name** was a String. 
    - Dictionary where keys are level names and values are list of codes, if **name** was a List. 

### Example

```python
from ehr_functions.features import codes

print(codes.get_ccs_mapping('2'))  # ICD-10 Diagnoses - Single Level for '2'
print(codes.get_ccs_mapping('2.1.1', level=3, code_type=9))  # ICD-9 Diagnoses - Multi Level #3 for '2.1.1'
print(codes.get_ccs_mapping(['11.6.4', '11.6.5'], level=3, code_type=9))  # ICD-9 Diagnoses - Multi Level #3 for '2.1.1'
```

```bash
['A021', 'A207', 'A227', 'A267', 'A327', 'A392', 'A393', 'A394', 'A400', 'A401', 'A403', 'A408', 'A409', 'A4101', 'A4102', 'A411', 'A412', 'A413', 'A414', 'A4150', 'A4151', 'A4152', 'A4153', 'A4159', 'A4181', 'A4189', 'A419', 'A427', 'A5486', 'B007', 'B377', 'I76', 'P360', 'P3610', 'P3619', 'P362', 'P3630', 'P3639', 'P364', 'P365', 'P368', 'P369', 'R6520']

['1530', '1531', '1532', '1533', '1534', '1535', '1536', '1537', '1538', '1539', '1590', '20910', '20911', '20912', '20913', '20914', '20915', '20916', '2303', 'V1005']

{'65610': '11.6.4', '65611': '11.6.4', '65613': '11.6.4', '65640': '11.6.5', '65641': '11.6.5', '65643': '11.6.5'}
```