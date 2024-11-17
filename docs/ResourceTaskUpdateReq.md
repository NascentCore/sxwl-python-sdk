# ResourceTaskUpdateReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceTaskUpdate]**](ResourceTaskUpdate.md) |  | 

## Example

```python
from openapi_client.models.resource_task_update_req import ResourceTaskUpdateReq

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceTaskUpdateReq from a JSON string
resource_task_update_req_instance = ResourceTaskUpdateReq.from_json(json)
# print the JSON string representation of the object
print(ResourceTaskUpdateReq.to_json())

# convert the object into a dict
resource_task_update_req_dict = resource_task_update_req_instance.to_dict()
# create an instance of ResourceTaskUpdateReq from a dict
resource_task_update_req_from_dict = ResourceTaskUpdateReq.from_dict(resource_task_update_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


