# UserInfoResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**UserInfo**](UserInfo.md) |  | 

## Example

```python
from openapi_client.models.user_info_resp import UserInfoResp

# TODO update the JSON string below
json = "{}"
# create an instance of UserInfoResp from a JSON string
user_info_resp_instance = UserInfoResp.from_json(json)
# print the JSON string representation of the object
print(UserInfoResp.to_json())

# convert the object into a dict
user_info_resp_dict = user_info_resp_instance.to_dict()
# create an instance of UserInfoResp from a dict
user_info_resp_from_dict = UserInfoResp.from_dict(user_info_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


