# GPUJobStatusResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from sxwl_client.models.gpu_job_status_resp import GPUJobStatusResp

# TODO update the JSON string below
json = "{}"
# create an instance of GPUJobStatusResp from a JSON string
gpu_job_status_resp_instance = GPUJobStatusResp.from_json(json)
# print the JSON string representation of the object
print(GPUJobStatusResp.to_json())

# convert the object into a dict
gpu_job_status_resp_dict = gpu_job_status_resp_instance.to_dict()
# create an instance of GPUJobStatusResp from a dict
gpu_job_status_resp_from_dict = GPUJobStatusResp.from_dict(gpu_job_status_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


