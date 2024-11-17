# CPODStatusReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_status** | [**List[JobStatus]**](JobStatus.md) |  | 
**inference_status** | [**List[InferenceStatus]**](InferenceStatus.md) |  | 
**jupyter_status** | [**List[JupyterlabStatus]**](JupyterlabStatus.md) |  | 
**app_job_status** | [**List[AppJobStatus]**](AppJobStatus.md) |  | 
**resource_info** | [**ResourceInfo**](ResourceInfo.md) |  | 
**update_time** | **str** |  | 
**cpod_id** | **str** |  | 

## Example

```python
from openapi_client.models.cpod_status_req import CPODStatusReq

# TODO update the JSON string below
json = "{}"
# create an instance of CPODStatusReq from a JSON string
cpod_status_req_instance = CPODStatusReq.from_json(json)
# print the JSON string representation of the object
print(CPODStatusReq.to_json())

# convert the object into a dict
cpod_status_req_dict = cpod_status_req_instance.to_dict()
# create an instance of CPODStatusReq from a dict
cpod_status_req_from_dict = CPODStatusReq.from_dict(cpod_status_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


