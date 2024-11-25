# GPUJobStatusReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | 

## Example

```python
from sxwl_client.models.gpu_job_status_req import GPUJobStatusReq

# TODO update the JSON string below
json = "{}"
# create an instance of GPUJobStatusReq from a JSON string
gpu_job_status_req_instance = GPUJobStatusReq.from_json(json)
# print the JSON string representation of the object
print(GPUJobStatusReq.to_json())

# convert the object into a dict
gpu_job_status_req_dict = gpu_job_status_req_instance.to_dict()
# create an instance of GPUJobStatusReq from a dict
gpu_job_status_req_from_dict = GPUJobStatusReq.from_dict(gpu_job_status_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


