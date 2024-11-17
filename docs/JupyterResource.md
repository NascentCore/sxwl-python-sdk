# JupyterResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**models** | [**List[Model]**](Model.md) |  | [optional] 
**datasets** | [**List[Dataset]**](Dataset.md) |  | [optional] 
**adapters** | [**List[Adapter]**](Adapter.md) |  | [optional] 

## Example

```python
from openapi_client.models.jupyter_resource import JupyterResource

# TODO update the JSON string below
json = "{}"
# create an instance of JupyterResource from a JSON string
jupyter_resource_instance = JupyterResource.from_json(json)
# print the JSON string representation of the object
print(JupyterResource.to_json())

# convert the object into a dict
jupyter_resource_dict = jupyter_resource_instance.to_dict()
# create an instance of JupyterResource from a dict
jupyter_resource_from_dict = JupyterResource.from_dict(jupyter_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


