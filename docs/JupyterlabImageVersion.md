# JupyterlabImageVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_name** | **str** |  | 
**image_size** | **int** |  | 
**tag_name** | **str** |  | 
**full_name** | **str** |  | 
**push_time** | **str** |  | 

## Example

```python
from openapi_client.models.jupyterlab_image_version import JupyterlabImageVersion

# TODO update the JSON string below
json = "{}"
# create an instance of JupyterlabImageVersion from a JSON string
jupyterlab_image_version_instance = JupyterlabImageVersion.from_json(json)
# print the JSON string representation of the object
print(JupyterlabImageVersion.to_json())

# convert the object into a dict
jupyterlab_image_version_dict = jupyterlab_image_version_instance.to_dict()
# create an instance of JupyterlabImageVersion from a dict
jupyterlab_image_version_from_dict = JupyterlabImageVersion.from_dict(jupyterlab_image_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


