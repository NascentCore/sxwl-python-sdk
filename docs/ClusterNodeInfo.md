# ClusterNodeInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gpu_count** | **int** |  | 
**gpu_product** | **str** |  | 
**name** | **str** |  | 
**role** | **List[str]** |  | 

## Example

```python
from openapi_client.models.cluster_node_info import ClusterNodeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterNodeInfo from a JSON string
cluster_node_info_instance = ClusterNodeInfo.from_json(json)
# print the JSON string representation of the object
print(ClusterNodeInfo.to_json())

# convert the object into a dict
cluster_node_info_dict = cluster_node_info_instance.to_dict()
# create an instance of ClusterNodeInfo from a dict
cluster_node_info_from_dict = ClusterNodeInfo.from_dict(cluster_node_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


