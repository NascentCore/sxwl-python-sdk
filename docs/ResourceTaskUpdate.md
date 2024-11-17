# ResourceTaskUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** |  | 
**resource_type** | **str** |  | 
**source** | **str** |  | 
**size** | **int** |  | 
**err** | **str** |  | 
**ok** | **bool** |  | 

## Example

```python
from openapi_client.models.resource_task_update import ResourceTaskUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceTaskUpdate from a JSON string
resource_task_update_instance = ResourceTaskUpdate.from_json(json)
# print the JSON string representation of the object
print(ResourceTaskUpdate.to_json())

# convert the object into a dict
resource_task_update_dict = resource_task_update_instance.to_dict()
# create an instance of ResourceTaskUpdate from a dict
resource_task_update_from_dict = ResourceTaskUpdate.from_dict(resource_task_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


