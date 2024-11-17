# MemInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **int** |  | 
**used** | **int** |  | 
**usage** | **int** |  | 

## Example

```python
from openapi_client.models.mem_info import MemInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MemInfo from a JSON string
mem_info_instance = MemInfo.from_json(json)
# print the JSON string representation of the object
print(MemInfo.to_json())

# convert the object into a dict
mem_info_dict = mem_info_instance.to_dict()
# create an instance of MemInfo from a dict
mem_info_from_dict = MemInfo.from_dict(mem_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


