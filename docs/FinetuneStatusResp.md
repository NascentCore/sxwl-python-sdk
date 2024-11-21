# FinetuneStatusResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | 
**status** | **str** |  | 
**adapter_id** | **str** |  适配器ID | [optional] 
**adapter_name** | **str** |  适配器名字, owner/adapter | [optional] 
**adapter_path** | **str** |  适配器的绑定路径 | [optional] 
**adapter_size** | **int** |  适配器体积，单位字节 | [optional] 
**adapter_is_public** | **bool** |  是否公共适配器 | [optional] 

## Example

```python
from sxwl_client.models.finetune_status_resp import FinetuneStatusResp

# TODO update the JSON string below
json = "{}"
# create an instance of FinetuneStatusResp from a JSON string
finetune_status_resp_instance = FinetuneStatusResp.from_json(json)
# print the JSON string representation of the object
print(FinetuneStatusResp.to_json())

# convert the object into a dict
finetune_status_resp_dict = finetune_status_resp_instance.to_dict()
# create an instance of FinetuneStatusResp from a dict
finetune_status_resp_from_dict = FinetuneStatusResp.from_dict(finetune_status_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


