# Hyperparameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**n_epochs** | **str** |  | 
**batch_size** | **str** |  | 
**learning_rate_multiplier** | **str** |  | 

## Example

```python
from openapi_client.models.hyperparameters import Hyperparameters

# TODO update the JSON string below
json = "{}"
# create an instance of Hyperparameters from a JSON string
hyperparameters_instance = Hyperparameters.from_json(json)
# print the JSON string representation of the object
print(Hyperparameters.to_json())

# convert the object into a dict
hyperparameters_dict = hyperparameters_instance.to_dict()
# create an instance of Hyperparameters from a dict
hyperparameters_from_dict = Hyperparameters.from_dict(hyperparameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


