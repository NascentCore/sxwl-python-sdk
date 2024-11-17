# BillingListReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**start_time** | **str** |  | [optional] 
**end_time** | **str** |  | [optional] 
**job_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.billing_list_req import BillingListReq

# TODO update the JSON string below
json = "{}"
# create an instance of BillingListReq from a JSON string
billing_list_req_instance = BillingListReq.from_json(json)
# print the JSON string representation of the object
print(BillingListReq.to_json())

# convert the object into a dict
billing_list_req_dict = billing_list_req_instance.to_dict()
# create an instance of BillingListReq from a dict
billing_list_req_from_dict = BillingListReq.from_dict(billing_list_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


