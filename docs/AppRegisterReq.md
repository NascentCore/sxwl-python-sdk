# AppRegisterReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**desc** | **str** |  | 
**crd** | **str** |  | 

## Example

```python
from openapi_client.models.app_register_req import AppRegisterReq

# TODO update the JSON string below
json = "{}"
# create an instance of AppRegisterReq from a JSON string
app_register_req_instance = AppRegisterReq.from_json(json)
# print the JSON string representation of the object
print(AppRegisterReq.to_json())

# convert the object into a dict
app_register_req_dict = app_register_req_instance.to_dict()
# create an instance of AppRegisterReq from a dict
app_register_req_from_dict = AppRegisterReq.from_dict(app_register_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


