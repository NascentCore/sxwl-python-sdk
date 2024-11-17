# AdapterOptional


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adapter_id** | **str** |  适配器ID | [optional] 
**adapter_name** | **str** |  适配器名字, owner/adapter | [optional] 
**adapter_path** | **str** |  适配器的绑定路径 | [optional] 
**adapter_size** | **int** |  适配器体积，单位字节 | [optional] 
**adapter_is_public** | **bool** |  是否公共适配器 | [optional] 

## Example

```python
from sxwl_client.models.adapter_optional import AdapterOptional

# TODO update the JSON string below
json = "{}"
# create an instance of AdapterOptional from a JSON string
adapter_optional_instance = AdapterOptional.from_json(json)
# print the JSON string representation of the object
print(AdapterOptional.to_json())

# convert the object into a dict
adapter_optional_dict = adapter_optional_instance.to_dict()
# create an instance of AdapterOptional from a dict
adapter_optional_from_dict = AdapterOptional.from_dict(adapter_optional_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


