# sxwl-client
算想云对开发者提供的API

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1
- Package version: 1.0.0
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import sxwl_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import sxwl_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import sxwl_client
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
    except ApiException as e:
        print("Exception when calling SchedulerApiApi->finetune: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*SchedulerApiApi* | [**finetune**](docs/SchedulerApiApi.md#finetune) | **POST** /api/job/finetune | 
*SchedulerApiApi* | [**inference_deploy**](docs/SchedulerApiApi.md#inference_deploy) | **POST** /api/job/inference | 
*SchedulerApiApi* | [**job_create**](docs/SchedulerApiApi.md#job_create) | **POST** /api/job/training | 


## Documentation For Models

 - [Adapter](docs/Adapter.md)
 - [AdapterOptional](docs/AdapterOptional.md)
 - [BaseResp](docs/BaseResp.md)
 - [Dataset](docs/Dataset.md)
 - [DatasetOptional](docs/DatasetOptional.md)
 - [FinetuneReq](docs/FinetuneReq.md)
 - [FinetuneResp](docs/FinetuneResp.md)
 - [Hyperparameters](docs/Hyperparameters.md)
 - [InferenceDeployReq](docs/InferenceDeployReq.md)
 - [InferenceDeployResp](docs/InferenceDeployResp.md)
 - [JobCallBackReq](docs/JobCallBackReq.md)
 - [JobCreateReq](docs/JobCreateReq.md)
 - [JobCreateResp](docs/JobCreateResp.md)
 - [Model](docs/Model.md)
 - [ModelOptional](docs/ModelOptional.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="apiKey"></a>
### apiKey

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author




