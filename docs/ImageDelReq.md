# ImageDelReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**image_name** | **str** |  | 
**tag** | **str** |  | 

## Example

```python
from openapi_client.models.image_del_req import ImageDelReq

# TODO update the JSON string below
json = "{}"
# create an instance of ImageDelReq from a JSON string
image_del_req_instance = ImageDelReq.from_json(json)
# print the JSON string representation of the object
print(ImageDelReq.to_json())

# convert the object into a dict
image_del_req_dict = image_del_req_instance.to_dict()
# create an instance of ImageDelReq from a dict
image_del_req_from_dict = ImageDelReq.from_dict(image_del_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


