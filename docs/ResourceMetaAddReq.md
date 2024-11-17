# ResourceMetaAddReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** |  | 
**resource_type** | **str** |  | 
**resource_name** | **str** |  | 
**resource_size** | **int** |  | 
**is_public** | **bool** |  | 
**user_id** | **str** |  | 
**meta** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.resource_meta_add_req import ResourceMetaAddReq

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceMetaAddReq from a JSON string
resource_meta_add_req_instance = ResourceMetaAddReq.from_json(json)
# print the JSON string representation of the object
print(ResourceMetaAddReq.to_json())

# convert the object into a dict
resource_meta_add_req_dict = resource_meta_add_req_instance.to_dict()
# create an instance of ResourceMetaAddReq from a dict
resource_meta_add_req_from_dict = ResourceMetaAddReq.from_dict(resource_meta_add_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


