# Job


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ckpt_path** | **str** |  | 
**ckpt_vol** | **str** |  | 
**cpod_id** | **str** |  | 
**create_time** | **str** |  | 
**dataset_name** | **str** |  | [optional] 
**dataset_path** | **str** |  | [optional] 
**deleted** | **int** |  | 
**gpu_number** | **int** |  | 
**gpu_type** | **str** |  | 
**image_path** | **str** |  | 
**job_id** | **int** |  | 
**job_name** | **str** |  | 
**job_type** | **str** |  | 
**json_all** | **str** |  | 
**model_path** | **str** |  | 
**model_vol** | **str** |  | 
**obtain_status** | **int** |  | 
**pretrained_model_name** | **str** |  | [optional] 
**pretrained_model_path** | **str** |  | [optional] 
**run_command** | **str** |  | [optional] 
**stop_time** | **int** |  | 
**stop_type** | **int** |  | 
**update_time** | **str** |  | 
**user_id** | **str** |  | 
**work_status** | **int** |  | 
**status** | **str** |  | 
**tensor_url** | **str** |  | 

## Example

```python
from openapi_client.models.job import Job

# TODO update the JSON string below
json = "{}"
# create an instance of Job from a JSON string
job_instance = Job.from_json(json)
# print the JSON string representation of the object
print(Job.to_json())

# convert the object into a dict
job_dict = job_instance.to_dict()
# create an instance of Job from a dict
job_from_dict = Job.from_dict(job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


