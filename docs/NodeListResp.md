# NodeListResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClusterNodeInfo]**](ClusterNodeInfo.md) |  | 

## Example

```python
from openapi_client.models.node_list_resp import NodeListResp

# TODO update the JSON string below
json = "{}"
# create an instance of NodeListResp from a JSON string
node_list_resp_instance = NodeListResp.from_json(json)
# print the JSON string representation of the object
print(NodeListResp.to_json())

# convert the object into a dict
node_list_resp_dict = node_list_resp_instance.to_dict()
# create an instance of NodeListResp from a dict
node_list_resp_from_dict = NodeListResp.from_dict(node_list_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


