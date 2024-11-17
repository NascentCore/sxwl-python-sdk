# BillingListResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UserBilling]**](UserBilling.md) |  | 

## Example

```python
from openapi_client.models.billing_list_resp import BillingListResp

# TODO update the JSON string below
json = "{}"
# create an instance of BillingListResp from a JSON string
billing_list_resp_instance = BillingListResp.from_json(json)
# print the JSON string representation of the object
print(BillingListResp.to_json())

# convert the object into a dict
billing_list_resp_dict = billing_list_resp_instance.to_dict()
# create an instance of BillingListResp from a dict
billing_list_resp_from_dict = BillingListResp.from_dict(billing_list_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


