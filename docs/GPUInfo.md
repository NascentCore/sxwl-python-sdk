# GPUInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cuda** | **str** |  | 
**prod** | **str** |  | 
**driver** | **str** |  | 
**vendor** | **str** |  | 
**mem_size** | **int** |  | 
**status** | **str** |  | 

## Example

```python
from openapi_client.models.gpu_info import GPUInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GPUInfo from a JSON string
gpu_info_instance = GPUInfo.from_json(json)
# print the JSON string representation of the object
print(GPUInfo.to_json())

# convert the object into a dict
gpu_info_dict = gpu_info_instance.to_dict()
# create an instance of GPUInfo from a dict
gpu_info_from_dict = GPUInfo.from_dict(gpu_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


