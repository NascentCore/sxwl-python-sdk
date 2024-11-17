# openapi_client.SchedulerApiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**finetune_handler**](SchedulerApiApi.md#finetune_handler) | **POST** /api/job/finetune | 
[**inference_deploy_handler**](SchedulerApiApi.md#inference_deploy_handler) | **POST** /api/job/inference | 
[**job_create_handler**](SchedulerApiApi.md#job_create_handler) | **POST** /api/job/training | 


# **finetune_handler**
> FinetuneResp finetune_handler(sx_user_id, body)



### Example


```python
import openapi_client
from openapi_client.models.finetune_req import FinetuneReq
from openapi_client.models.finetune_resp import FinetuneResp
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SchedulerApiApi(api_client)
    sx_user_id = 'sx_user_id_example' # str | 
    body = openapi_client.FinetuneReq() # FinetuneReq | 

    try:
        api_response = api_instance.finetune_handler(sx_user_id, body)
        print("The response of SchedulerApiApi->finetune_handler:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulerApiApi->finetune_handler: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sx_user_id** | **str**|  | 
 **body** | [**FinetuneReq**](FinetuneReq.md)|  | 

### Return type

[**FinetuneResp**](FinetuneResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inference_deploy_handler**
> InferenceDeployResp inference_deploy_handler(sx_user_id, body)



### Example


```python
import openapi_client
from openapi_client.models.inference_deploy_req import InferenceDeployReq
from openapi_client.models.inference_deploy_resp import InferenceDeployResp
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SchedulerApiApi(api_client)
    sx_user_id = 'sx_user_id_example' # str | 
    body = openapi_client.InferenceDeployReq() # InferenceDeployReq | 

    try:
        api_response = api_instance.inference_deploy_handler(sx_user_id, body)
        print("The response of SchedulerApiApi->inference_deploy_handler:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulerApiApi->inference_deploy_handler: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sx_user_id** | **str**|  | 
 **body** | [**InferenceDeployReq**](InferenceDeployReq.md)|  | 

### Return type

[**InferenceDeployResp**](InferenceDeployResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_create_handler**
> JobCreateResp job_create_handler(sx_user_id, body)



### Example


```python
import openapi_client
from openapi_client.models.job_create_req import JobCreateReq
from openapi_client.models.job_create_resp import JobCreateResp
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SchedulerApiApi(api_client)
    sx_user_id = 'sx_user_id_example' # str | 
    body = openapi_client.JobCreateReq() # JobCreateReq | 

    try:
        api_response = api_instance.job_create_handler(sx_user_id, body)
        print("The response of SchedulerApiApi->job_create_handler:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulerApiApi->job_create_handler: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sx_user_id** | **str**|  | 
 **body** | [**JobCreateReq**](JobCreateReq.md)|  | 

### Return type

[**JobCreateResp**](JobCreateResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

