# Jupyterlab


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**job_name** | **str** |  | [optional] 
**instance_name** | **str** |  | 
**cpu_count** | **int** |  | 
**memory** | **int** |  | 
**cpod_id** | **str** |  | [optional] 
**gpu_count** | **int** |  | [optional] 
**gpu_product** | **str** |  | [optional] 
**data_volume_size** | **int** |  | 
**resource** | [**JupyterResource**](JupyterResource.md) |  | 
**url** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.jupyterlab import Jupyterlab

# TODO update the JSON string below
json = "{}"
# create an instance of Jupyterlab from a JSON string
jupyterlab_instance = Jupyterlab.from_json(json)
# print the JSON string representation of the object
print(Jupyterlab.to_json())

# convert the object into a dict
jupyterlab_dict = jupyterlab_instance.to_dict()
# create an instance of Jupyterlab from a dict
jupyterlab_from_dict = Jupyterlab.from_dict(jupyterlab_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


