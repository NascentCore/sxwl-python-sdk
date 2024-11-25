# sxwl_client.SchedulerApiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adapter_by_name**](SchedulerApiApi.md#adapter_by_name) | **GET** /api/resource/adapter/name | 
[**dataset_by_name**](SchedulerApiApi.md#dataset_by_name) | **GET** /api/resource/dataset/name | 
[**finetune**](SchedulerApiApi.md#finetune) | **POST** /api/job/finetune | 
[**finetune_status**](SchedulerApiApi.md#finetune_status) | **GET** /api/job/finetune/status | 
[**gpu_job_status**](SchedulerApiApi.md#gpu_job_status) | **GET** /api/job/gpu/status | 
[**gpu_job_stop**](SchedulerApiApi.md#gpu_job_stop) | **POST** /api/job/gpu/stop | 
[**inference_deploy**](SchedulerApiApi.md#inference_deploy) | **POST** /api/job/inference | 
[**inference_status**](SchedulerApiApi.md#inference_status) | **GET** /api/job/inference/status | 
[**inference_stop**](SchedulerApiApi.md#inference_stop) | **POST** /api/job/inference/stop | 
[**job_create**](SchedulerApiApi.md#job_create) | **POST** /api/job/training | 
[**model_by_name**](SchedulerApiApi.md#model_by_name) | **GET** /api/resource/model/name | 


# **adapter_by_name**
> Adapter adapter_by_name(adapter_name)



### Example


```python
import sxwl_client
from sxwl_client.models.adapter import Adapter
from sxwl_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sxwl_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with sxwl_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sxwl_client.SchedulerApiApi(api_client)
    adapter_name = 'adapter_name_example' # str | 

    try:
        api_response = api_instance.adapter_by_name(adapter_name)
        print("The response of SchedulerApiApi->adapter_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulerApiApi->adapter_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adapter_name** | **str**|  | 

### Return type

[**Adapter**](Adapter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dataset_by_name**
> Dataset dataset_by_name(dataset_name)



### Example


```python
import sxwl_client
from sxwl_client.models.dataset import Dataset
from sxwl_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sxwl_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with sxwl_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sxwl_client.SchedulerApiApi(api_client)
    dataset_name = 'dataset_name_example' # str | 

    try:
        api_response = api_instance.dataset_by_name(dataset_name)
        print("The response of SchedulerApiApi->dataset_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulerApiApi->dataset_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_name** | **str**|  | 

### Return type

[**Dataset**](Dataset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **finetune**
> FinetuneResp finetune(sx_user_id, body)



### Example


```python
import sxwl_client
from sxwl_client.models.finetune_req import FinetuneReq
from sxwl_client.models.finetune_resp import FinetuneResp
from sxwl_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sxwl_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with sxwl_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sxwl_client.SchedulerApiApi(api_client)
    sx_user_id = 'sx_user_id_example' # str | 
    body = sxwl_client.FinetuneReq() # FinetuneReq | 

    try:
        api_response = api_instance.finetune(sx_user_id, body)
        print("The response of SchedulerApiApi->finetune:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulerApiApi->finetune: %s\n" % e)
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

# **finetune_status**
> FinetuneStatusResp finetune_status(sx_user_id, job_id)



### Example


```python
import sxwl_client
from sxwl_client.models.finetune_status_resp import FinetuneStatusResp
from sxwl_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sxwl_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with sxwl_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sxwl_client.SchedulerApiApi(api_client)
    sx_user_id = 'sx_user_id_example' # str | 
    job_id = 'job_id_example' # str | 

    try:
        api_response = api_instance.finetune_status(sx_user_id, job_id)
        print("The response of SchedulerApiApi->finetune_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulerApiApi->finetune_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sx_user_id** | **str**|  | 
 **job_id** | **str**|  | 

### Return type

[**FinetuneStatusResp**](FinetuneStatusResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gpu_job_status**
> GPUJobStatusResp gpu_job_status(sx_user_id, job_id)



### Example


```python
import sxwl_client
from sxwl_client.models.gpu_job_status_resp import GPUJobStatusResp
from sxwl_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sxwl_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with sxwl_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sxwl_client.SchedulerApiApi(api_client)
    sx_user_id = 'sx_user_id_example' # str | 
    job_id = 'job_id_example' # str | 

    try:
        api_response = api_instance.gpu_job_status(sx_user_id, job_id)
        print("The response of SchedulerApiApi->gpu_job_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulerApiApi->gpu_job_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sx_user_id** | **str**|  | 
 **job_id** | **str**|  | 

### Return type

[**GPUJobStatusResp**](GPUJobStatusResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gpu_job_stop**
> BaseResp gpu_job_stop(job_id)



### Example


```python
import sxwl_client
from sxwl_client.models.base_resp import BaseResp
from sxwl_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sxwl_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with sxwl_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sxwl_client.SchedulerApiApi(api_client)
    job_id = 'job_id_example' # str | 

    try:
        api_response = api_instance.gpu_job_stop(job_id)
        print("The response of SchedulerApiApi->gpu_job_stop:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulerApiApi->gpu_job_stop: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 

### Return type

[**BaseResp**](BaseResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inference_deploy**
> InferenceDeployResp inference_deploy(sx_user_id, body)



### Example


```python
import sxwl_client
from sxwl_client.models.inference_deploy_req import InferenceDeployReq
from sxwl_client.models.inference_deploy_resp import InferenceDeployResp
from sxwl_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sxwl_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with sxwl_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sxwl_client.SchedulerApiApi(api_client)
    sx_user_id = 'sx_user_id_example' # str | 
    body = sxwl_client.InferenceDeployReq() # InferenceDeployReq | 

    try:
        api_response = api_instance.inference_deploy(sx_user_id, body)
        print("The response of SchedulerApiApi->inference_deploy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulerApiApi->inference_deploy: %s\n" % e)
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

# **inference_status**
> InferenceStatusResp inference_status(sx_user_id, service_name)



### Example


```python
import sxwl_client
from sxwl_client.models.inference_status_resp import InferenceStatusResp
from sxwl_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sxwl_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with sxwl_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sxwl_client.SchedulerApiApi(api_client)
    sx_user_id = 'sx_user_id_example' # str | 
    service_name = 'service_name_example' # str | 

    try:
        api_response = api_instance.inference_status(sx_user_id, service_name)
        print("The response of SchedulerApiApi->inference_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulerApiApi->inference_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sx_user_id** | **str**|  | 
 **service_name** | **str**|  | 

### Return type

[**InferenceStatusResp**](InferenceStatusResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inference_stop**
> BaseResp inference_stop(service_name)



### Example


```python
import sxwl_client
from sxwl_client.models.base_resp import BaseResp
from sxwl_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sxwl_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with sxwl_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sxwl_client.SchedulerApiApi(api_client)
    service_name = 'service_name_example' # str | 

    try:
        api_response = api_instance.inference_stop(service_name)
        print("The response of SchedulerApiApi->inference_stop:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulerApiApi->inference_stop: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**|  | 

### Return type

[**BaseResp**](BaseResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_create**
> JobCreateResp job_create(sx_user_id, body)



### Example


```python
import sxwl_client
from sxwl_client.models.job_create_req import JobCreateReq
from sxwl_client.models.job_create_resp import JobCreateResp
from sxwl_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sxwl_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with sxwl_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sxwl_client.SchedulerApiApi(api_client)
    sx_user_id = 'sx_user_id_example' # str | 
    body = sxwl_client.JobCreateReq() # JobCreateReq | 

    try:
        api_response = api_instance.job_create(sx_user_id, body)
        print("The response of SchedulerApiApi->job_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulerApiApi->job_create: %s\n" % e)
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

# **model_by_name**
> Model model_by_name(model_name)



### Example


```python
import sxwl_client
from sxwl_client.models.model import Model
from sxwl_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sxwl_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with sxwl_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sxwl_client.SchedulerApiApi(api_client)
    model_name = 'model_name_example' # str | 

    try:
        api_response = api_instance.model_by_name(model_name)
        print("The response of SchedulerApiApi->model_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulerApiApi->model_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_name** | **str**|  | 

### Return type

[**Model**](Model.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

