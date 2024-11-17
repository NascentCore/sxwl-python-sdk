# NodeInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_info** | [**CPUInfo**](CPUInfo.md) |  | 
**linux_dist** | **str** |  | 
**gpu_info** | [**GPUInfo**](GPUInfo.md) |  | 
**gpu_total** | **int** |  | 
**gpu_allocatable** | **int** |  | 
**network_info** | [**NetworkInfo**](NetworkInfo.md) |  | 
**kernel_version** | **str** |  | 
**disk_info** | [**DiskInfo**](DiskInfo.md) |  | 
**name** | **str** |  | 
**mem_info** | [**MemInfo**](MemInfo.md) |  | 
**arch** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from openapi_client.models.node_info import NodeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NodeInfo from a JSON string
node_info_instance = NodeInfo.from_json(json)
# print the JSON string representation of the object
print(NodeInfo.to_json())

# convert the object into a dict
node_info_dict = node_info_instance.to_dict()
# create an instance of NodeInfo from a dict
node_info_from_dict = NodeInfo.from_dict(node_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


