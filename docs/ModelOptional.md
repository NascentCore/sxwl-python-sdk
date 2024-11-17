# ModelOptional


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

## Example

```python
from openapi_client.models.model_optional import ModelOptional

# TODO update the JSON string below
json = "{}"
# create an instance of ModelOptional from a JSON string
model_optional_instance = ModelOptional.from_json(json)
# print the JSON string representation of the object
print(ModelOptional.to_json())

# convert the object into a dict
model_optional_dict = model_optional_instance.to_dict()
# create an instance of ModelOptional from a dict
model_optional_from_dict = ModelOptional.from_dict(model_optional_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


