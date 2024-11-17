# ResourceLoadReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  来源(例如huggingface) | 
**resource_id** | **str** |  资源ID | 
**resource_type** | **str** |  资源类型(model/dataset/adapter) | 
**meta** | **str** |  元信息 | 

## Example

```python
from openapi_client.models.resource_load_req import ResourceLoadReq

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceLoadReq from a JSON string
resource_load_req_instance = ResourceLoadReq.from_json(json)
# print the JSON string representation of the object
print(ResourceLoadReq.to_json())

# convert the object into a dict
resource_load_req_dict = resource_load_req_instance.to_dict()
# create an instance of ResourceLoadReq from a dict
resource_load_req_from_dict = ResourceLoadReq.from_dict(resource_load_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


