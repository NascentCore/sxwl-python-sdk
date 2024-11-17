# Model


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_id** | **str** |  模型ID | 
**model_name** | **str** |  模型名字, owner/model | 
**model_path** | **str** |  模型的绑定路径 | [optional] 
**model_size** | **int** |  模型体积，单位字节 | 
**model_is_public** | **bool** |  是否公共模型 | 
**model_template** | **str** |  模型的推理模版 | 
**model_meta** | **str** |  元信息 | 
**model_category** | **str** |  模型分类 | 

## Example

```python
from openapi_client.models.model import Model

# TODO update the JSON string below
json = "{}"
# create an instance of Model from a JSON string
model_instance = Model.from_json(json)
# print the JSON string representation of the object
print(Model.to_json())

# convert the object into a dict
model_dict = model_instance.to_dict()
# create an instance of Model from a dict
model_from_dict = Model.from_dict(model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


