# ResourceSyncTaskResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceSyncTask]**](ResourceSyncTask.md) |  | 
**total** | **int** |  | 

## Example

```python
from openapi_client.models.resource_sync_task_resp import ResourceSyncTaskResp

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSyncTaskResp from a JSON string
resource_sync_task_resp_instance = ResourceSyncTaskResp.from_json(json)
# print the JSON string representation of the object
print(ResourceSyncTaskResp.to_json())

# convert the object into a dict
resource_sync_task_resp_dict = resource_sync_task_resp_instance.to_dict()
# create an instance of ResourceSyncTaskResp from a dict
resource_sync_task_resp_from_dict = ResourceSyncTaskResp.from_dict(resource_sync_task_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


