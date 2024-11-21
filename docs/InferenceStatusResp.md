# InferenceStatusResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_name** | **str** |  | 
**status** | **str** |  | 
**chat_url** | **str** |  | 
**api_url** | **str** |  | 

## Example

```python
from sxwl_client.models.inference_status_resp import InferenceStatusResp

# TODO update the JSON string below
json = "{}"
# create an instance of InferenceStatusResp from a JSON string
inference_status_resp_instance = InferenceStatusResp.from_json(json)
# print the JSON string representation of the object
print(InferenceStatusResp.to_json())

# convert the object into a dict
inference_status_resp_dict = inference_status_resp_instance.to_dict()
# create an instance of InferenceStatusResp from a dict
inference_status_resp_from_dict = InferenceStatusResp.from_dict(inference_status_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


