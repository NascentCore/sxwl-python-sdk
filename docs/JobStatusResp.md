# JobStatusResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from openapi_client.models.job_status_resp import JobStatusResp

# TODO update the JSON string below
json = "{}"
# create an instance of JobStatusResp from a JSON string
job_status_resp_instance = JobStatusResp.from_json(json)
# print the JSON string representation of the object
print(JobStatusResp.to_json())

# convert the object into a dict
job_status_resp_dict = job_status_resp_instance.to_dict()
# create an instance of JobStatusResp from a dict
job_status_resp_from_dict = JobStatusResp.from_dict(job_status_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


