# Adapter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adapter_id** | **str** |  适配器ID | 
**adapter_name** | **str** |  适配器名字, owner/adapter | 
**adapter_path** | **str** |  适配器的绑定路径 | [optional] 
**adapter_size** | **int** |  适配器体积，单位字节 | 
**adapter_is_public** | **bool** |  是否公共适配器 | 

## Example

```python
from openapi_client.models.adapter import Adapter

# TODO update the JSON string below
json = "{}"
# create an instance of Adapter from a JSON string
adapter_instance = Adapter.from_json(json)
# print the JSON string representation of the object
print(Adapter.to_json())

# convert the object into a dict
adapter_dict = adapter_instance.to_dict()
# create an instance of Adapter from a dict
adapter_from_dict = Adapter.from_dict(adapter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


