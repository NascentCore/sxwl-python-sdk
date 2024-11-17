# AppJobGetResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AppJob]**](AppJob.md) |  | 
**total** | **int** |  | 

## Example

```python
from openapi_client.models.app_job_get_resp import AppJobGetResp

# TODO update the JSON string below
json = "{}"
# create an instance of AppJobGetResp from a JSON string
app_job_get_resp_instance = AppJobGetResp.from_json(json)
# print the JSON string representation of the object
print(AppJobGetResp.to_json())

# convert the object into a dict
app_job_get_resp_dict = app_job_get_resp_instance.to_dict()
# create an instance of AppJobGetResp from a dict
app_job_get_resp_from_dict = AppJobGetResp.from_dict(app_job_get_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


