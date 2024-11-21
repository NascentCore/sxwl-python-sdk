# InferenceStatusReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_name** | **str** |  | 

## Example

```python
from sxwl_client.models.inference_status_req import InferenceStatusReq

# TODO update the JSON string below
json = "{}"
# create an instance of InferenceStatusReq from a JSON string
inference_status_req_instance = InferenceStatusReq.from_json(json)
# print the JSON string representation of the object
print(InferenceStatusReq.to_json())

# convert the object into a dict
inference_status_req_dict = inference_status_req_instance.to_dict()
# create an instance of InferenceStatusReq from a dict
inference_status_req_from_dict = InferenceStatusReq.from_dict(inference_status_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


