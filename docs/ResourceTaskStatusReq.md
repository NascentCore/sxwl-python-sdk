# ResourceTaskStatusReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** |  | [optional] 
**resource_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.resource_task_status_req import ResourceTaskStatusReq

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceTaskStatusReq from a JSON string
resource_task_status_req_instance = ResourceTaskStatusReq.from_json(json)
# print the JSON string representation of the object
print(ResourceTaskStatusReq.to_json())

# convert the object into a dict
resource_task_status_req_dict = resource_task_status_req_instance.to_dict()
# create an instance of ResourceTaskStatusReq from a dict
resource_task_status_req_from_dict = ResourceTaskStatusReq.from_dict(resource_task_status_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


