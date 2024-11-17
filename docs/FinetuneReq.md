# FinetuneReq


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
**dataset_id** | **str** |  数据集ID | [optional] 
**dataset_name** | **str** |  数据集名字, owner/dataset | [optional] 
**dataset_path** | **str** |  数据集的绑定路径 | [optional] 
**dataset_size** | **int** |  数据集体积，单位字节 | [optional] 
**dataset_is_public** | **bool** |  是否公共数据集 | [optional] 
**cpod_id** | **str** |  | [optional] 
**gpu_model** | **str** |  | [optional] 
**gpu_count** | **int** |  | [optional] 
**trained_model_name** | **str** |  | [optional] 
**hyperparameters** | [**Hyperparameters**](Hyperparameters.md) |  | 
**model_saved_type** | **str** |  | 
**finetune_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.finetune_req import FinetuneReq

# TODO update the JSON string below
json = "{}"
# create an instance of FinetuneReq from a JSON string
finetune_req_instance = FinetuneReq.from_json(json)
# print the JSON string representation of the object
print(FinetuneReq.to_json())

# convert the object into a dict
finetune_req_dict = finetune_req_instance.to_dict()
# create an instance of FinetuneReq from a dict
finetune_req_from_dict = FinetuneReq.from_dict(finetune_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


