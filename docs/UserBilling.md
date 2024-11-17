# UserBilling


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_id** | **str** |  账单ID | 
**user_id** | **str** |  用户ID | 
**amount** | **float** |  消费金额 | 
**billing_status** | **int** |  账单状态（0 未支付、1 已支付、2 欠费） TODO 返回字符串 | 
**job_id** | **str** |  关联任务id | 
**job_type** | **str** |  关联任务类型（例如：finetune、inference） | 
**billing_time** | **str** |  账单生成时间 | 
**payment_time** | **str** |  支付时间 | 
**description** | **str** |  账单描述（可选，详细说明此次费用的具体内容） | 

## Example

```python
from openapi_client.models.user_billing import UserBilling

# TODO update the JSON string below
json = "{}"
# create an instance of UserBilling from a JSON string
user_billing_instance = UserBilling.from_json(json)
# print the JSON string representation of the object
print(UserBilling.to_json())

# convert the object into a dict
user_billing_dict = user_billing_instance.to_dict()
# create an instance of UserBilling from a dict
user_billing_from_dict = UserBilling.from_dict(user_billing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


