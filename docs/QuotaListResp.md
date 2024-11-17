# QuotaListResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[QuotaResp]**](QuotaResp.md) |  | 

## Example

```python
from openapi_client.models.quota_list_resp import QuotaListResp

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaListResp from a JSON string
quota_list_resp_instance = QuotaListResp.from_json(json)
# print the JSON string representation of the object
print(QuotaListResp.to_json())

# convert the object into a dict
quota_list_resp_dict = quota_list_resp_instance.to_dict()
# create an instance of QuotaListResp from a dict
quota_list_resp_from_dict = QuotaListResp.from_dict(quota_list_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


