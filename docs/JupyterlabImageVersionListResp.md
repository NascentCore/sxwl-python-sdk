# JupyterlabImageVersionListResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[JupyterlabImageVersion]**](JupyterlabImageVersion.md) |  | 

## Example

```python
from openapi_client.models.jupyterlab_image_version_list_resp import JupyterlabImageVersionListResp

# TODO update the JSON string below
json = "{}"
# create an instance of JupyterlabImageVersionListResp from a JSON string
jupyterlab_image_version_list_resp_instance = JupyterlabImageVersionListResp.from_json(json)
# print the JSON string representation of the object
print(JupyterlabImageVersionListResp.to_json())

# convert the object into a dict
jupyterlab_image_version_list_resp_dict = jupyterlab_image_version_list_resp_instance.to_dict()
# create an instance of JupyterlabImageVersionListResp from a dict
jupyterlab_image_version_list_resp_from_dict = JupyterlabImageVersionListResp.from_dict(jupyterlab_image_version_list_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


