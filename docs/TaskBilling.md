# TaskBilling


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  用户ID | 
**job_id** | **str** |  关联任务id | 
**job_type** | **str** |  关联任务类型（例如：finetune、inference） | 
**amount** | **float** |  消费金额 | 
**begin_time** | **str** |  | 
**end_time** | **str** |  | 

## Example

```python
from openapi_client.models.task_billing import TaskBilling

# TODO update the JSON string below
json = "{}"
# create an instance of TaskBilling from a JSON string
task_billing_instance = TaskBilling.from_json(json)
# print the JSON string representation of the object
print(TaskBilling.to_json())

# convert the object into a dict
task_billing_dict = task_billing_instance.to_dict()
# create an instance of TaskBilling from a dict
task_billing_from_dict = TaskBilling.from_dict(task_billing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


