# JupyterlabUpdateReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_name** | **str** |  | 
**cpu_count** | **int** |  | 
**memory** | **int** |  | 
**gpu_count** | **int** |  | 
**gpu_product** | **str** |  | 
**data_volume_size** | **int** |  | 

## Example

```python
from openapi_client.models.jupyterlab_update_req import JupyterlabUpdateReq

# TODO update the JSON string below
json = "{}"
# create an instance of JupyterlabUpdateReq from a JSON string
jupyterlab_update_req_instance = JupyterlabUpdateReq.from_json(json)
# print the JSON string representation of the object
print(JupyterlabUpdateReq.to_json())

# convert the object into a dict
jupyterlab_update_req_dict = jupyterlab_update_req_instance.to_dict()
# create an instance of JupyterlabUpdateReq from a dict
jupyterlab_update_req_from_dict = JupyterlabUpdateReq.from_dict(jupyterlab_update_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


