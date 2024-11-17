# InferenceDeployReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_id** | **str** |  模型ID | [optional] 
**model_name** | **str** |  模型名字, owner/model | [optional] 
**model_path** | **str** |  模型的绑定路径 | [optional] 
**model_size** | **int** |  模型体积，单位字节 | [optional] 
**model_is_public** | **bool** |  是否公共模型 | [optional] 
**model_template** | **str** |  模型的推理模版 | [optional] 
**model_meta** | **str** |  元信息 | [optional] 
**model_category** | **str** |  模型分类 | [optional] 
**adapter_id** | **str** |  适配器ID | [optional] 
**adapter_name** | **str** |  适配器名字, owner/adapter | [optional] 
**adapter_path** | **str** |  适配器的绑定路径 | [optional] 
**adapter_size** | **int** |  适配器体积，单位字节 | [optional] 
**adapter_is_public** | **bool** |  是否公共适配器 | [optional] 
**cpod_id** | **str** |  | [optional] 
**gpu_model** | **str** |  | [optional] 
**gpu_count** | **int** |  | [optional] 
**min_instances** | **int** |  | [optional] 
**max_instances** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.inference_deploy_req import InferenceDeployReq

# TODO update the JSON string below
json = "{}"
# create an instance of InferenceDeployReq from a JSON string
inference_deploy_req_instance = InferenceDeployReq.from_json(json)
# print the JSON string representation of the object
print(InferenceDeployReq.to_json())

# convert the object into a dict
inference_deploy_req_dict = inference_deploy_req_instance.to_dict()
# create an instance of InferenceDeployReq from a dict
inference_deploy_req_from_dict = InferenceDeployReq.from_dict(inference_deploy_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


