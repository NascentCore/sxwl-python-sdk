# DatasetOptional


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_id** | **str** |  数据集ID | [optional] 
**dataset_name** | **str** |  数据集名字, owner/dataset | [optional] 
**dataset_path** | **str** |  数据集的绑定路径 | [optional] 
**dataset_size** | **int** |  数据集体积，单位字节 | [optional] 
**dataset_is_public** | **bool** |  是否公共数据集 | [optional] 

## Example

```python
from sxwl_client.models.dataset_optional import DatasetOptional

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetOptional from a JSON string
dataset_optional_instance = DatasetOptional.from_json(json)
# print the JSON string representation of the object
print(DatasetOptional.to_json())

# convert the object into a dict
dataset_optional_dict = dataset_optional_instance.to_dict()
# create an instance of DatasetOptional from a dict
dataset_optional_from_dict = DatasetOptional.from_dict(dataset_optional_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


