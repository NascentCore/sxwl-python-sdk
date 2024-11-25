# GPUJobStopResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 

## Example

```python
from sxwl_client.models.gpu_job_stop_resp import GPUJobStopResp

# TODO update the JSON string below
json = "{}"
# create an instance of GPUJobStopResp from a JSON string
gpu_job_stop_resp_instance = GPUJobStopResp.from_json(json)
# print the JSON string representation of the object
print(GPUJobStopResp.to_json())

# convert the object into a dict
gpu_job_stop_resp_dict = gpu_job_stop_resp_instance.to_dict()
# create an instance of GPUJobStopResp from a dict
gpu_job_stop_resp_from_dict = GPUJobStopResp.from_dict(gpu_job_stop_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


