# AppListResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[App]**](App.md) |  | 
**total** | **int** |  | 

## Example

```python
from openapi_client.models.app_list_resp import AppListResp

# TODO update the JSON string below
json = "{}"
# create an instance of AppListResp from a JSON string
app_list_resp_instance = AppListResp.from_json(json)
# print the JSON string representation of the object
print(AppListResp.to_json())

# convert the object into a dict
app_list_resp_dict = app_list_resp_instance.to_dict()
# create an instance of AppListResp from a dict
app_list_resp_from_dict = AppListResp.from_dict(app_list_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


