# RechargeListReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**page** | **int** |  | 
**page_size** | **int** |  | 

## Example

```python
from openapi_client.models.recharge_list_req import RechargeListReq

# TODO update the JSON string below
json = "{}"
# create an instance of RechargeListReq from a JSON string
recharge_list_req_instance = RechargeListReq.from_json(json)
# print the JSON string representation of the object
print(RechargeListReq.to_json())

# convert the object into a dict
recharge_list_req_dict = recharge_list_req_instance.to_dict()
# create an instance of RechargeListReq from a dict
recharge_list_req_from_dict = RechargeListReq.from_dict(recharge_list_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


