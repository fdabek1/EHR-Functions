# Base Metric

Metrics are used to evaluate models and print results within the Jupyter notebook.  Below is the standard definition of a Metric.

## Methods

### post_train

```python
def post_train(self, train_data, val_data):
    train_true, train_pred = train_data
    val_true, val_pred = val_data
```

Gets called after the model is fit.

## Utilization

Metrics can be passed in one of two ways: class type and class instance.

### Class Type

In this scenario, the metric was passed with just the class type and an instance was not created.  The `train_model` function will automatically create an instance using this class. 

```python
from ehr_functions.models import train_model
from ehr_functions.models.types import LogisticRegression
from ehr_functions.models.metrics import BaseMetric

train_model(LogisticRegression(), features, df[['PatientID', 'Over30']], metrics=[BaseMetric])
```

### Class Instance

In this scenario, a custom argument needs to be passed to the metric and thus an instance of it is created before being passed to the function.

```python
from ehr_functions.models import train_model
from ehr_functions.models.types import LogisticRegression
from ehr_functions.models.metrics import BaseMetric

train_model(LogisticRegression(), features, df[['PatientID', 'Over30']], metrics=[BaseMetric(custom_param=5)])
```