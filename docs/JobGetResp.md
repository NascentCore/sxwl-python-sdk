# JobGetResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[Job]**](Job.md) |  | 
**total_elements** | **int** |  | 

## Example

```python
from openapi_client.models.job_get_resp import JobGetResp

# TODO update the JSON string below
json = "{}"
# create an instance of JobGetResp from a JSON string
job_get_resp_instance = JobGetResp.from_json(json)
# print the JSON string representation of the object
print(JobGetResp.to_json())

# convert the object into a dict
job_get_resp_dict = job_get_resp_instance.to_dict()
# create an instance of JobGetResp from a dict
job_get_resp_from_dict = JobGetResp.from_dict(job_get_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


