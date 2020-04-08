# Demographics

## get_features

```python
demographics.get_features(df, cols=None)
```

### Arguments

- **df:** Pandas DataFrame
 
- **cols:** A list of the columns to extract. Defaults to ['PatientAge', 'PatientGender', 'PatientService', 'PatientPayGrade'].


### Returns

- Pandas DataFrame containing PatientID and feature columns in numeric formats.