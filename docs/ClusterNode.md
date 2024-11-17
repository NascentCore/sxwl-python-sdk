# ClusterNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_role** | **str** |  | 
**node_name** | **str** |  | 
**node_ip** | **str** |  | 
**ssh_port** | **int** |  | 
**ssh_user** | **str** |  | 
**ssh_password** | **str** |  | 

## Example

```python
from openapi_client.models.cluster_node import ClusterNode

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterNode from a JSON string
cluster_node_instance = ClusterNode.from_json(json)
# print the JSON string representation of the object
print(ClusterNode.to_json())

# convert the object into a dict
cluster_node_dict = cluster_node_instance.to_dict()
# create an instance of ClusterNode from a dict
cluster_node_from_dict = ClusterNode.from_dict(cluster_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


