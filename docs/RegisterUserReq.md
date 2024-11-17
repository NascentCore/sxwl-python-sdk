# RegisterUserReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**email** | **str** |  | 
**enabled** | **int** |  | 
**password** | **str** |  | 
**var_from** | **str** |  | [optional] 
**user_type** | **int** |  | [optional] 
**company_name** | **str** |  | [optional] 
**company_phone** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.register_user_req import RegisterUserReq

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterUserReq from a JSON string
register_user_req_instance = RegisterUserReq.from_json(json)
# print the JSON string representation of the object
print(RegisterUserReq.to_json())

# convert the object into a dict
register_user_req_dict = register_user_req_instance.to_dict()
# create an instance of RegisterUserReq from a dict
register_user_req_from_dict = RegisterUserReq.from_dict(register_user_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


