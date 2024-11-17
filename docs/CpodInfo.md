# CpodInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpod_id** | **str** |  | 
**cpod_version** | **str** |  | 
**node_name** | **str** |  | 
**gpu_vendor** | **str** |  | 
**gpu_prod** | **str** |  | 
**gpu_mem** | **int** |  | 
**gpu_total** | **int** |  | 
**gpu_allocatable** | **int** |  | 
**create_time** | **str** |  | 
**update_time** | **str** |  | 

## Example

```python
from openapi_client.models.cpod_info import CpodInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CpodInfo from a JSON string
cpod_info_instance = CpodInfo.from_json(json)
# print the JSON string representation of the object
print(CpodInfo.to_json())

# convert the object into a dict
cpod_info_dict = cpod_info_instance.to_dict()
# create an instance of CpodInfo from a dict
cpod_info_from_dict = CpodInfo.from_dict(cpod_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


