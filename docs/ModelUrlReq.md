# ModelUrlReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_urls** | **List[str]** |  | 
**job_name** | **str** |  | 

## Example

```python
from openapi_client.models.model_url_req import ModelUrlReq

# TODO update the JSON string below
json = "{}"
# create an instance of ModelUrlReq from a JSON string
model_url_req_instance = ModelUrlReq.from_json(json)
# print the JSON string representation of the object
print(ModelUrlReq.to_json())

# convert the object into a dict
model_url_req_dict = model_url_req_instance.to_dict()
# create an instance of ModelUrlReq from a dict
model_url_req_from_dict = ModelUrlReq.from_dict(model_url_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


