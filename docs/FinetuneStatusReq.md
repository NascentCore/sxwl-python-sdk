# FinetuneStatusReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | 

## Example

```python
from sxwl_client.models.finetune_status_req import FinetuneStatusReq

# TODO update the JSON string below
json = "{}"
# create an instance of FinetuneStatusReq from a JSON string
finetune_status_req_instance = FinetuneStatusReq.from_json(json)
# print the JSON string representation of the object
print(FinetuneStatusReq.to_json())

# convert the object into a dict
finetune_status_req_dict = finetune_status_req_instance.to_dict()
# create an instance of FinetuneStatusReq from a dict
finetune_status_req_from_dict = FinetuneStatusReq.from_dict(finetune_status_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


