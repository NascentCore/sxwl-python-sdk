# JobCreateReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpod_id** | **str** |  | [optional] 
**gpu_number** | **int** |  | 
**gpu_type** | **str** |  | 
**ckpt_path** | **str** |  | 
**ckpt_vol** | **int** |  | 
**model_path** | **str** |  | 
**model_vol** | **int** |  | 
**image_path** | **str** |  | 
**job_type** | **str** |  | 
**stop_type** | **int** |  | [optional] 
**stop_time** | **int** |  | [optional] 
**model_id** | **str** |  模型ID | [optional] 
**model_name** | **str** |  模型名字, owner/model | [optional] 
**model_path** | **str** |  模型的绑定路径 | [optional] 
**model_size** | **int** |  模型体积，单位字节 | [optional] 
**model_is_public** | **bool** |  是否公共模型 | [optional] 
**model_template** | **str** |  模型的推理模版 | [optional] 
**model_meta** | **str** |  元信息 | [optional] 
**model_category** | **str** |  模型分类 | [optional] 
**dataset_id** | **str** |  数据集ID | [optional] 
**dataset_name** | **str** |  数据集名字, owner/dataset | [optional] 
**dataset_path** | **str** |  数据集的绑定路径 | [optional] 
**dataset_size** | **int** |  数据集体积，单位字节 | [optional] 
**dataset_is_public** | **bool** |  是否公共数据集 | [optional] 
**trained_model_name** | **str** |  | [optional] 
**run_command** | **str** |  | [optional] 
**callback_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.job_create_req import JobCreateReq

# TODO update the JSON string below
json = "{}"
# create an instance of JobCreateReq from a JSON string
job_create_req_instance = JobCreateReq.from_json(json)
# print the JSON string representation of the object
print(JobCreateReq.to_json())

# convert the object into a dict
job_create_req_dict = job_create_req_instance.to_dict()
# create an instance of JobCreateReq from a dict
job_create_req_from_dict = JobCreateReq.from_dict(job_create_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


