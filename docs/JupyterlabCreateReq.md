# JupyterlabCreateReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**job_name** | **str** |  | [optional] 
**instance_name** | **str** |  | [optional] 
**cpu_count** | **int** |  | [optional] 
**memory** | **int** |  | [optional] 
**cpod_id** | **str** |  | [optional] 
**gpu_count** | **int** |  | [optional] 
**gpu_product** | **str** |  | [optional] 
**data_volume_size** | **int** |  | [optional] 
**resource** | [**JupyterResource**](JupyterResource.md) |  | [optional] 
**url** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.jupyterlab_create_req import JupyterlabCreateReq

# TODO update the JSON string below
json = "{}"
# create an instance of JupyterlabCreateReq from a JSON string
jupyterlab_create_req_instance = JupyterlabCreateReq.from_json(json)
# print the JSON string representation of the object
print(JupyterlabCreateReq.to_json())

# convert the object into a dict
jupyterlab_create_req_dict = jupyterlab_create_req_instance.to_dict()
# create an instance of JupyterlabCreateReq from a dict
jupyterlab_create_req_from_dict = JupyterlabCreateReq.from_dict(jupyterlab_create_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


