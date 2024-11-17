# UserListResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[User]**](User.md) |  | 

## Example

```python
from openapi_client.models.user_list_resp import UserListResp

# TODO update the JSON string below
json = "{}"
# create an instance of UserListResp from a JSON string
user_list_resp_instance = UserListResp.from_json(json)
# print the JSON string representation of the object
print(UserListResp.to_json())

# convert the object into a dict
user_list_resp_dict = user_list_resp_instance.to_dict()
# create an instance of UserListResp from a dict
user_list_resp_from_dict = UserListResp.from_dict(user_list_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


