# CpodJobResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_list** | [**List[MapStringinterface]**](MapStringinterface.md) |  | 
**inference_service_list** | [**List[InferenceService]**](InferenceService.md) |  | 
**jupyter_lab_list** | [**List[JupyterLab]**](JupyterLab.md) |  | 
**app_job_list** | [**List[AppJobInfo]**](AppJobInfo.md) |  | 

## Example

```python
from openapi_client.models.cpod_job_resp import CpodJobResp

# TODO update the JSON string below
json = "{}"
# create an instance of CpodJobResp from a JSON string
cpod_job_resp_instance = CpodJobResp.from_json(json)
# print the JSON string representation of the object
print(CpodJobResp.to_json())

# convert the object into a dict
cpod_job_resp_dict = cpod_job_resp_instance.to_dict()
# create an instance of CpodJobResp from a dict
cpod_job_resp_from_dict = CpodJobResp.from_dict(cpod_job_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


