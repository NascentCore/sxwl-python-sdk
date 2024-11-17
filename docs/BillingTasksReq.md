# BillingTasksReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**page** | **int** |  | 
**page_size** | **int** |  | 

## Example

```python
from openapi_client.models.billing_tasks_req import BillingTasksReq

# TODO update the JSON string below
json = "{}"
# create an instance of BillingTasksReq from a JSON string
billing_tasks_req_instance = BillingTasksReq.from_json(json)
# print the JSON string representation of the object
print(BillingTasksReq.to_json())

# convert the object into a dict
billing_tasks_req_dict = billing_tasks_req_instance.to_dict()
# create an instance of BillingTasksReq from a dict
billing_tasks_req_from_dict = BillingTasksReq.from_dict(billing_tasks_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


