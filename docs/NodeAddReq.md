# NodeAddReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_role** | **str** |  | [optional] 
**node_name** | **str** |  | [optional] 
**node_ip** | **str** |  | [optional] 
**ssh_port** | **int** |  | [optional] 
**ssh_user** | **str** |  | [optional] 
**ssh_password** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.node_add_req import NodeAddReq

# TODO update the JSON string below
json = "{}"
# create an instance of NodeAddReq from a JSON string
node_add_req_instance = NodeAddReq.from_json(json)
# print the JSON string representation of the object
print(NodeAddReq.to_json())

# convert the object into a dict
node_add_req_dict = node_add_req_instance.to_dict()
# create an instance of NodeAddReq from a dict
node_add_req_from_dict = NodeAddReq.from_dict(node_add_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


