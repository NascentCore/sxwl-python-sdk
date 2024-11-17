# SysInference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_name** | **str** |  | 
**status** | **str** |  | 
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
**url** | **str** |  | 
**api** | **str** |  | 
**gpu_model** | **str** |  | 
**gpu_count** | **int** |  | 
**create_time** | **str** |  推理服务创建时间 | 
**start_time** | **str** |  推理服务启动时间 | 
**end_time** | **str** |  推理服务终止时间 | 

## Example

```python
from openapi_client.models.sys_inference import SysInference

# TODO update the JSON string below
json = "{}"
# create an instance of SysInference from a JSON string
sys_inference_instance = SysInference.from_json(json)
# print the JSON string representation of the object
print(SysInference.to_json())

# convert the object into a dict
sys_inference_dict = sys_inference_instance.to_dict()
# create an instance of SysInference from a dict
sys_inference_from_dict = SysInference.from_dict(sys_inference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


