# QuotaAddReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**resource** | **str** |  | [optional] 
**quota** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.quota_add_req import QuotaAddReq

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaAddReq from a JSON string
quota_add_req_instance = QuotaAddReq.from_json(json)
# print the JSON string representation of the object
print(QuotaAddReq.to_json())

# convert the object into a dict
quota_add_req_dict = quota_add_req_instance.to_dict()
# create an instance of QuotaAddReq from a dict
quota_add_req_from_dict = QuotaAddReq.from_dict(quota_add_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


