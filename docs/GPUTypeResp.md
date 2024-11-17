# GPUTypeResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | 
**gpu_prod** | **str** |  | 
**gpu_allocatable** | **int** |  | 

## Example

```python
from openapi_client.models.gpu_type_resp import GPUTypeResp

# TODO update the JSON string below
json = "{}"
# create an instance of GPUTypeResp from a JSON string
gpu_type_resp_instance = GPUTypeResp.from_json(json)
# print the JSON string representation of the object
print(GPUTypeResp.to_json())

# convert the object into a dict
gpu_type_resp_dict = gpu_type_resp_instance.to_dict()
# create an instance of GPUTypeResp from a dict
gpu_type_resp_from_dict = GPUTypeResp.from_dict(gpu_type_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


