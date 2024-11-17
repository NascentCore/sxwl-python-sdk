# UploaderAccessResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_id** | **str** |  | 
**access_key** | **str** |  | 
**user_id** | **str** |  | 
**is_admin** | **bool** |  | 

## Example

```python
from openapi_client.models.uploader_access_resp import UploaderAccessResp

# TODO update the JSON string below
json = "{}"
# create an instance of UploaderAccessResp from a JSON string
uploader_access_resp_instance = UploaderAccessResp.from_json(json)
# print the JSON string representation of the object
print(UploaderAccessResp.to_json())

# convert the object into a dict
uploader_access_resp_dict = uploader_access_resp_instance.to_dict()
# create an instance of UploaderAccessResp from a dict
uploader_access_resp_from_dict = UploaderAccessResp.from_dict(uploader_access_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


