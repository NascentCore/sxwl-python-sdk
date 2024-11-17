# InferenceDeployResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_name** | **str** |  | 

## Example

```python
from sxwl_client.models.inference_deploy_resp import InferenceDeployResp

# TODO update the JSON string below
json = "{}"
# create an instance of InferenceDeployResp from a JSON string
inference_deploy_resp_instance = InferenceDeployResp.from_json(json)
# print the JSON string representation of the object
print(InferenceDeployResp.to_json())

# convert the object into a dict
inference_deploy_resp_dict = inference_deploy_resp_instance.to_dict()
# create an instance of InferenceDeployResp from a dict
inference_deploy_resp_from_dict = InferenceDeployResp.from_dict(inference_deploy_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


