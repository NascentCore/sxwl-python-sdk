# BalanceAddReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**amount** | **float** |  | 

## Example

```python
from openapi_client.models.balance_add_req import BalanceAddReq

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceAddReq from a JSON string
balance_add_req_instance = BalanceAddReq.from_json(json)
# print the JSON string representation of the object
print(BalanceAddReq.to_json())

# convert the object into a dict
balance_add_req_dict = balance_add_req_instance.to_dict()
# create an instance of BalanceAddReq from a dict
balance_add_req_from_dict = BalanceAddReq.from_dict(balance_add_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


