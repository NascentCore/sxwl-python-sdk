# Dataset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_id** | **str** |  数据集ID | 
**dataset_name** | **str** |  数据集名字, owner/dataset | 
**dataset_path** | **str** |  数据集的绑定路径 | [optional] 
**dataset_size** | **int** |  数据集体积，单位字节 | 
**dataset_is_public** | **bool** |  是否公共数据集 | 

## Example

```python
from sxwl_client.models.dataset import Dataset

# TODO update the JSON string below
json = "{}"
# create an instance of Dataset from a JSON string
dataset_instance = Dataset.from_json(json)
# print the JSON string representation of the object
print(Dataset.to_json())

# convert the object into a dict
dataset_dict = dataset_instance.to_dict()
# create an instance of Dataset from a dict
dataset_from_dict = Dataset.from_dict(dataset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


