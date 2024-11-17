# DiskInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **int** |  | 
**usage** | **int** |  | 

## Example

```python
from openapi_client.models.disk_info import DiskInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DiskInfo from a JSON string
disk_info_instance = DiskInfo.from_json(json)
# print the JSON string representation of the object
print(DiskInfo.to_json())

# convert the object into a dict
disk_info_dict = disk_info_instance.to_dict()
# create an instance of DiskInfo from a dict
disk_info_from_dict = DiskInfo.from_dict(disk_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


