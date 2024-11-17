# QuotaUpdateReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**quota** | **int** |  | 

## Example

```python
from openapi_client.models.quota_update_req import QuotaUpdateReq

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaUpdateReq from a JSON string
quota_update_req_instance = QuotaUpdateReq.from_json(json)
# print the JSON string representation of the object
print(QuotaUpdateReq.to_json())

# convert the object into a dict
quota_update_req_dict = quota_update_req_instance.to_dict()
# create an instance of QuotaUpdateReq from a dict
quota_update_req_from_dict = QuotaUpdateReq.from_dict(quota_update_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


