# AppJobInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_name** | **str** |  | 
**instance_name** | **str** |  | 
**user_id** | **str** |  | 
**app_id** | **str** |  | 
**app_name** | **str** |  | 
**crd** | **str** |  | 
**meta** | **str** |  | 

## Example

```python
from openapi_client.models.app_job_info import AppJobInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppJobInfo from a JSON string
app_job_info_instance = AppJobInfo.from_json(json)
# print the JSON string representation of the object
print(AppJobInfo.to_json())

# convert the object into a dict
app_job_info_dict = app_job_info_instance.to_dict()
# create an instance of AppJobInfo from a dict
app_job_info_from_dict = AppJobInfo.from_dict(app_job_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


