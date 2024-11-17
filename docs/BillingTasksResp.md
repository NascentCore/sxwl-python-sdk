# BillingTasksResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TaskBilling]**](TaskBilling.md) |  | 
**total** | **int** |  | 

## Example

```python
from openapi_client.models.billing_tasks_resp import BillingTasksResp

# TODO update the JSON string below
json = "{}"
# create an instance of BillingTasksResp from a JSON string
billing_tasks_resp_instance = BillingTasksResp.from_json(json)
# print the JSON string representation of the object
print(BillingTasksResp.to_json())

# convert the object into a dict
billing_tasks_resp_dict = billing_tasks_resp_instance.to_dict()
# create an instance of BillingTasksResp from a dict
billing_tasks_resp_from_dict = BillingTasksResp.from_dict(billing_tasks_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


