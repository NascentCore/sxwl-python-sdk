# ResourceTaskStatusResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceSyncTask]**](ResourceSyncTask.md) |  | 
**total** | **int** |  | 

## Example

```python
from openapi_client.models.resource_task_status_resp import ResourceTaskStatusResp

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceTaskStatusResp from a JSON string
resource_task_status_resp_instance = ResourceTaskStatusResp.from_json(json)
# print the JSON string representation of the object
print(ResourceTaskStatusResp.to_json())

# convert the object into a dict
resource_task_status_resp_dict = resource_task_status_resp_instance.to_dict()
# create an instance of ResourceTaskStatusResp from a dict
resource_task_status_resp_from_dict = ResourceTaskStatusResp.from_dict(resource_task_status_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


