# JupyterlabImageCreateReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_image** | **str** |  | 
**instance_name** | **str** |  | 
**job_name** | **str** |  | 

## Example

```python
from openapi_client.models.jupyterlab_image_create_req import JupyterlabImageCreateReq

# TODO update the JSON string below
json = "{}"
# create an instance of JupyterlabImageCreateReq from a JSON string
jupyterlab_image_create_req_instance = JupyterlabImageCreateReq.from_json(json)
# print the JSON string representation of the object
print(JupyterlabImageCreateReq.to_json())

# convert the object into a dict
jupyterlab_image_create_req_dict = jupyterlab_image_create_req_instance.to_dict()
# create an instance of JupyterlabImageCreateReq from a dict
jupyterlab_image_create_req_from_dict = JupyterlabImageCreateReq.from_dict(jupyterlab_image_create_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


