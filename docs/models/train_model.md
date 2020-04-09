# train\_model

```python
models.train_model(model, df: pd.DataFrame, outcome, features=None, data_type=None, metrics=None, return_preds=False)
```

This function trains a given model using train/val data.

If outcome is multiple and the model does not support multiple output then an ensemble of models is used.

## Arguments

- **model:** A Model instance. Optionally can be a String to save an import statement, if using default parameters.
 
- **df:** Pandas DataFrame containing patients and the features to utilize.

- **features:** A list of the feature columns, only if a subset of the *df* should be utilized.  By default all columns within *df* will be used except for *PatientID*.
 
- **outcome:**
    - **String:** If the outcome is a column in the *df* then provide the name of the column as a String
    - **List:** List of outcomes as strings.
    - **Pandas Series:** For a single output scenario.
    - **Pandas DataFrame:** For multiple output scenarios, each column should be an output. 

- **data_type:** An optional Pandas DataFrame containing a column named *Type* with the values `train`, `val`, or `test`, indicating which dataset the patient belongs in.  To use this feature, the *outcome* cannot be a Pandas Series due to inability to correctly reference patients.

- **metrics:** A list of [metrics](metrics/base.md) for the model to be evaluated against and to be printed out.  Optionally can be a String to save an import statement, if using default parameters.
 
- **return_preds:** Whether to return the model predictions.  If enabled then returns a tuple containing the train and val predictions.


## Returns

- Trained model instance.
- Numpy array containing predicted values, if *return_results* is `True`.

## Examples