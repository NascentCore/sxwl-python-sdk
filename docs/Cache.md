# Cache


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** |  | 
**data_name** | **str** |  | 
**data_id** | **str** |  | 
**data_size** | **int** |  | 
**template** | **str** |  | 
**data_source** | **str** |  | 
**is_public** | **bool** |  | 
**user_id** | **str** |  | 
**finetune_gpu_count** | **int** |  | 
**inference_gpu_count** | **int** |  | 

## Example

```python
from openapi_client.models.cache import Cache

# TODO update the JSON string below
json = "{}"
# create an instance of Cache from a JSON string
cache_instance = Cache.from_json(json)
# print the JSON string representation of the object
print(Cache.to_json())

# convert the object into a dict
cache_dict = cache_instance.to_dict()
# create an instance of Cache from a dict
cache_from_dict = Cache.from_dict(cache_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


