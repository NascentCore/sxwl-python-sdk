# GPUSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocatable** | **int** |  | 
**total** | **int** |  | 
**prod** | **str** |  | 
**mem_size** | **int** |  | 
**vendor** | **str** |  | 

## Example

```python
from openapi_client.models.gpu_summary import GPUSummary

# TODO update the JSON string below
json = "{}"
# create an instance of GPUSummary from a JSON string
gpu_summary_instance = GPUSummary.from_json(json)
# print the JSON string representation of the object
print(GPUSummary.to_json())

# convert the object into a dict
gpu_summary_dict = gpu_summary_instance.to_dict()
# create an instance of GPUSummary from a dict
gpu_summary_from_dict = GPUSummary.from_dict(gpu_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


