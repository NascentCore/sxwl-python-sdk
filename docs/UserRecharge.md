# UserRecharge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  ID | 
**recharge_id** | **str** |  充值记录id | 
**user_id** | **str** |  用户ID | 
**amount** | **float** |  充值金额 | 
**before_balance** | **float** |  充值前余额 | 
**after_balance** | **float** |  充值后余额 | 
**description** | **str** |  描述 | 
**created_at** | **str** |  创建时间 | 
**updated_at** | **str** |  更新时间 | 

## Example

```python
from openapi_client.models.user_recharge import UserRecharge

# TODO update the JSON string below
json = "{}"
# create an instance of UserRecharge from a JSON string
user_recharge_instance = UserRecharge.from_json(json)
# print the JSON string representation of the object
print(UserRecharge.to_json())

# convert the object into a dict
user_recharge_dict = user_recharge_instance.to_dict()
# create an instance of UserRecharge from a dict
user_recharge_from_dict = UserRecharge.from_dict(user_recharge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


