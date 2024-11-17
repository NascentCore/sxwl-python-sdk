# AppJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**job_name** | **str** |  | 
**user_id** | **str** |  用户ID | 
**app_id** | **str** |  应用ID | 
**app_name** | **str** |  应用名字 | 
**instance_name** | **str** |  实例名称 | 
**cpod_id** | **str** |  cpod id | 
**status** | **str** |  状态 | 
**billing_status** | **int** |  账单状态（0 未结清、1 已结清） | 
**url** | **str** |  URL | 
**start_time** | **str** |  推理服务启动时间 | 
**end_time** | **str** |  推理服务终止时间 | 
**created_at** | **str** |  创建时间 | 
**updated_at** | **str** |  更新时间 | 

## Example

```python
from openapi_client.models.app_job import AppJob

# TODO update the JSON string below
json = "{}"
# create an instance of AppJob from a JSON string
app_job_instance = AppJob.from_json(json)
# print the JSON string representation of the object
print(AppJob.to_json())

# convert the object into a dict
app_job_dict = app_job_instance.to_dict()
# create an instance of AppJob from a dict
app_job_from_dict = AppJob.from_dict(app_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


