# AppJobStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_name** | **str** |  | 
**status** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from openapi_client.models.app_job_status import AppJobStatus

# TODO update the JSON string below
json = "{}"
# create an instance of AppJobStatus from a JSON string
app_job_status_instance = AppJobStatus.from_json(json)
# print the JSON string representation of the object
print(AppJobStatus.to_json())

# convert the object into a dict
app_job_status_dict = app_job_status_instance.to_dict()
# create an instance of AppJobStatus from a dict
app_job_status_from_dict = AppJobStatus.from_dict(app_job_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


