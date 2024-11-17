# RechargeListResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**data** | [**List[UserRecharge]**](UserRecharge.md) |  | 

## Example

```python
from openapi_client.models.recharge_list_resp import RechargeListResp

# TODO update the JSON string below
json = "{}"
# create an instance of RechargeListResp from a JSON string
recharge_list_resp_instance = RechargeListResp.from_json(json)
# print the JSON string representation of the object
print(RechargeListResp.to_json())

# convert the object into a dict
recharge_list_resp_dict = recharge_list_resp_instance.to_dict()
# create an instance of RechargeListResp from a dict
recharge_list_resp_from_dict = RechargeListResp.from_dict(recharge_list_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


