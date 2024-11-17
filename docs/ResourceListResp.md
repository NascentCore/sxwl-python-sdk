# ResourceListResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_list** | [**List[Resource]**](Resource.md) |  | 
**user_list** | [**List[Resource]**](Resource.md) |  | 

## Example

```python
from openapi_client.models.resource_list_resp import ResourceListResp

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListResp from a JSON string
resource_list_resp_instance = ResourceListResp.from_json(json)
# print the JSON string representation of the object
print(ResourceListResp.to_json())

# convert the object into a dict
resource_list_resp_dict = resource_list_resp_instance.to_dict()
# create an instance of ResourceListResp from a dict
resource_list_resp_from_dict = ResourceListResp.from_dict(resource_list_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


