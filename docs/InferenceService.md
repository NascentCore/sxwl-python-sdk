# InferenceService


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_name** | **str** |  | 
**status** | **str** |  | 
**model_name** | **str** |  | 
**model_id** | **str** |  | 
**model_size** | **int** |  | 
**model_is_public** | **bool** |  | 
**model_category** | **str** |  | 
**model_meta** | **str** |  | 
**adapter_name** | **str** |  | 
**adapter_id** | **str** |  | 
**adapter_size** | **int** |  | 
**adapter_is_public** | **bool** |  | 
**gpu_type** | **str** |  | 
**gpu_number** | **int** |  | 
**min_instances** | **int** |  | 
**max_instances** | **int** |  | 
**template** | **str** |  | 
**cpod_id** | **str** |  | 
**user_id** | **str** |  | 

## Example

```python
from openapi_client.models.inference_service import InferenceService

# TODO update the JSON string below
json = "{}"
# create an instance of InferenceService from a JSON string
inference_service_instance = InferenceService.from_json(json)
# print the JSON string representation of the object
print(InferenceService.to_json())

# convert the object into a dict
inference_service_dict = inference_service_instance.to_dict()
# create an instance of InferenceService from a dict
inference_service_from_dict = InferenceService.from_dict(inference_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


