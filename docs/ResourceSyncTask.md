# ResourceSyncTask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** |  | 
**resource_type** | **str** |  | 
**source** | **str** |  | 
**status** | **str** |  | 
**token** | **str** |  | 

## Example

```python
from openapi_client.models.resource_sync_task import ResourceSyncTask

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSyncTask from a JSON string
resource_sync_task_instance = ResourceSyncTask.from_json(json)
# print the JSON string representation of the object
print(ResourceSyncTask.to_json())

# convert the object into a dict
resource_sync_task_dict = resource_sync_task_instance.to_dict()
# create an instance of ResourceSyncTask from a dict
resource_sync_task_from_dict = ResourceSyncTask.from_dict(resource_sync_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


