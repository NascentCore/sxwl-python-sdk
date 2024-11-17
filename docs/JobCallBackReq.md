# JobCallBackReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**url** | **str** |  | 
**job_id** | **str** |  | 

## Example

```python
from openapi_client.models.job_call_back_req import JobCallBackReq

# TODO update the JSON string below
json = "{}"
# create an instance of JobCallBackReq from a JSON string
job_call_back_req_instance = JobCallBackReq.from_json(json)
# print the JSON string representation of the object
print(JobCallBackReq.to_json())

# convert the object into a dict
job_call_back_req_dict = job_call_back_req_instance.to_dict()
# create an instance of JobCallBackReq from a dict
job_call_back_req_from_dict = JobCallBackReq.from_dict(job_call_back_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


