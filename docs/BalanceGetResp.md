# BalanceGetResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**balance** | **float** |  | 

## Example

```python
from openapi_client.models.balance_get_resp import BalanceGetResp

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceGetResp from a JSON string
balance_get_resp_instance = BalanceGetResp.from_json(json)
# print the JSON string representation of the object
print(BalanceGetResp.to_json())

# convert the object into a dict
balance_get_resp_dict = balance_get_resp_instance.to_dict()
# create an instance of BalanceGetResp from a dict
balance_get_resp_from_dict = BalanceGetResp.from_dict(balance_get_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


