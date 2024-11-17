# InferenceInfoResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SysInference]**](SysInference.md) |  | 

## Example

```python
from openapi_client.models.inference_info_resp import InferenceInfoResp

# TODO update the JSON string below
json = "{}"
# create an instance of InferenceInfoResp from a JSON string
inference_info_resp_instance = InferenceInfoResp.from_json(json)
# print the JSON string representation of the object
print(InferenceInfoResp.to_json())

# convert the object into a dict
inference_info_resp_dict = inference_info_resp_instance.to_dict()
# create an instance of InferenceInfoResp from a dict
inference_info_resp_from_dict = InferenceInfoResp.from_dict(inference_info_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


