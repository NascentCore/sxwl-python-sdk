# BuildImageReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_image** | **str** |  | 
**user_id** | **str** |  | 
**instance_name** | **str** |  | 
**job_name** | **str** |  | 

## Example

```python
from openapi_client.models.build_image_req import BuildImageReq

# TODO update the JSON string below
json = "{}"
# create an instance of BuildImageReq from a JSON string
build_image_req_instance = BuildImageReq.from_json(json)
# print the JSON string representation of the object
print(BuildImageReq.to_json())

# convert the object into a dict
build_image_req_dict = build_image_req_instance.to_dict()
# create an instance of BuildImageReq from a dict
build_image_req_from_dict = BuildImageReq.from_dict(build_image_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


