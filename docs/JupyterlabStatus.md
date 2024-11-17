# JupyterlabStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_name** | **str** |  | 
**status** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from openapi_client.models.jupyterlab_status import JupyterlabStatus

# TODO update the JSON string below
json = "{}"
# create an instance of JupyterlabStatus from a JSON string
jupyterlab_status_instance = JupyterlabStatus.from_json(json)
# print the JSON string representation of the object
print(JupyterlabStatus.to_json())

# convert the object into a dict
jupyterlab_status_dict = jupyterlab_status_instance.to_dict()
# create an instance of JupyterlabStatus from a dict
jupyterlab_status_from_dict = JupyterlabStatus.from_dict(jupyterlab_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


