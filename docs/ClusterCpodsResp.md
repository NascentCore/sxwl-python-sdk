# ClusterCpodsResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CpodInfo]**](CpodInfo.md) |  | 

## Example

```python
from openapi_client.models.cluster_cpods_resp import ClusterCpodsResp

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCpodsResp from a JSON string
cluster_cpods_resp_instance = ClusterCpodsResp.from_json(json)
# print the JSON string representation of the object
print(ClusterCpodsResp.to_json())

# convert the object into a dict
cluster_cpods_resp_dict = cluster_cpods_resp_instance.to_dict()
# create an instance of ClusterCpodsResp from a dict
cluster_cpods_resp_from_dict = ClusterCpodsResp.from_dict(cluster_cpods_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


