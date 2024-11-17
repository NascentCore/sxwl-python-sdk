# QuotaResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**user_id** | **str** |  | [optional] 
**resource** | **str** |  | [optional] 
**quota** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.quota_resp import QuotaResp

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaResp from a JSON string
quota_resp_instance = QuotaResp.from_json(json)
# print the JSON string representation of the object
print(QuotaResp.to_json())

# convert the object into a dict
quota_resp_dict = quota_resp_instance.to_dict()
# create an instance of QuotaResp from a dict
quota_resp_from_dict = QuotaResp.from_dict(quota_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


