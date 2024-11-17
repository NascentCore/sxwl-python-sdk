# AppJobAddReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** |  应用ID | 
**app_name** | **str** |  应用名字 | 
**instance_name** | **str** |  实例名称 | 
**meta** | **str** |  应用实例元信息 | 

## Example

```python
from openapi_client.models.app_job_add_req import AppJobAddReq

# TODO update the JSON string below
json = "{}"
# create an instance of AppJobAddReq from a JSON string
app_job_add_req_instance = AppJobAddReq.from_json(json)
# print the JSON string representation of the object
print(AppJobAddReq.to_json())

# convert the object into a dict
app_job_add_req_dict = app_job_add_req_instance.to_dict()
# create an instance of AppJobAddReq from a dict
app_job_add_req_from_dict = AppJobAddReq.from_dict(app_job_add_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


