# coding: utf-8

"""
    调度器服务

    调度器服务的接口定义

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.cpod_status_req import CPODStatusReq

class TestCPODStatusReq(unittest.TestCase):
    """CPODStatusReq unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CPODStatusReq:
        """Test CPODStatusReq
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CPODStatusReq`
        """
        model = CPODStatusReq()
        if include_optional:
            return CPODStatusReq(
                job_status = [
                    openapi_client.models.job_status.JobStatus(
                        job_status = '', 
                        name = '', 
                        namespace = '', 
                        jobtype = '', )
                    ],
                inference_status = [
                    openapi_client.models.inference_status.InferenceStatus(
                        service_name = '', 
                        status = '', 
                        url = '', )
                    ],
                jupyter_status = [
                    openapi_client.models.jupyterlab_status.JupyterlabStatus(
                        job_name = '', 
                        status = '', 
                        url = '', )
                    ],
                app_job_status = [
                    openapi_client.models.app_job_status.AppJobStatus(
                        job_name = '', 
                        status = '', 
                        url = '', )
                    ],
                resource_info = openapi_client.models.resource_info.ResourceInfo(
                    gpu_summaries = [
                        openapi_client.models.gpu_summary.GPUSummary(
                            allocatable = 56, 
                            total = 56, 
                            prod = '', 
                            mem_size = 56, 
                            vendor = '', )
                        ], 
                    cpod_version = '', 
                    nodes = [
                        openapi_client.models.node_info.NodeInfo(
                            cpu_info = openapi_client.models.cpu_info.CPUInfo(
                                cores = 56, 
                                used = 56, 
                                usage = 56, ), 
                            linux_dist = '', 
                            gpu_info = openapi_client.models.gpu_info.GPUInfo(
                                cuda = '', 
                                prod = '', 
                                driver = '', 
                                vendor = '', 
                                mem_size = 56, 
                                status = '', ), 
                            gpu_total = 56, 
                            gpu_allocatable = 56, 
                            network_info = openapi_client.models.network_info.NetworkInfo(
                                throughput = 56, 
                                type = '', ), 
                            kernel_version = '', 
                            disk_info = openapi_client.models.disk_info.DiskInfo(
                                size = 56, 
                                usage = 56, ), 
                            name = '', 
                            mem_info = openapi_client.models.mem_info.MemInfo(
                                size = 56, 
                                used = 56, 
                                usage = 56, ), 
                            arch = '', 
                            status = '', )
                        ], 
                    cpod_id = '', 
                    caches = [
                        openapi_client.models.cache.Cache(
                            data_type = '', 
                            data_name = '', 
                            data_id = '', 
                            data_size = 56, 
                            template = '', 
                            data_source = '', 
                            is_public = True, 
                            user_id = '', 
                            finetune_gpu_count = 56, 
                            inference_gpu_count = 56, )
                        ], ),
                update_time = '',
                cpod_id = ''
            )
        else:
            return CPODStatusReq(
                job_status = [
                    openapi_client.models.job_status.JobStatus(
                        job_status = '', 
                        name = '', 
                        namespace = '', 
                        jobtype = '', )
                    ],
                inference_status = [
                    openapi_client.models.inference_status.InferenceStatus(
                        service_name = '', 
                        status = '', 
                        url = '', )
                    ],
                jupyter_status = [
                    openapi_client.models.jupyterlab_status.JupyterlabStatus(
                        job_name = '', 
                        status = '', 
                        url = '', )
                    ],
                app_job_status = [
                    openapi_client.models.app_job_status.AppJobStatus(
                        job_name = '', 
                        status = '', 
                        url = '', )
                    ],
                resource_info = openapi_client.models.resource_info.ResourceInfo(
                    gpu_summaries = [
                        openapi_client.models.gpu_summary.GPUSummary(
                            allocatable = 56, 
                            total = 56, 
                            prod = '', 
                            mem_size = 56, 
                            vendor = '', )
                        ], 
                    cpod_version = '', 
                    nodes = [
                        openapi_client.models.node_info.NodeInfo(
                            cpu_info = openapi_client.models.cpu_info.CPUInfo(
                                cores = 56, 
                                used = 56, 
                                usage = 56, ), 
                            linux_dist = '', 
                            gpu_info = openapi_client.models.gpu_info.GPUInfo(
                                cuda = '', 
                                prod = '', 
                                driver = '', 
                                vendor = '', 
                                mem_size = 56, 
                                status = '', ), 
                            gpu_total = 56, 
                            gpu_allocatable = 56, 
                            network_info = openapi_client.models.network_info.NetworkInfo(
                                throughput = 56, 
                                type = '', ), 
                            kernel_version = '', 
                            disk_info = openapi_client.models.disk_info.DiskInfo(
                                size = 56, 
                                usage = 56, ), 
                            name = '', 
                            mem_info = openapi_client.models.mem_info.MemInfo(
                                size = 56, 
                                used = 56, 
                                usage = 56, ), 
                            arch = '', 
                            status = '', )
                        ], 
                    cpod_id = '', 
                    caches = [
                        openapi_client.models.cache.Cache(
                            data_type = '', 
                            data_name = '', 
                            data_id = '', 
                            data_size = 56, 
                            template = '', 
                            data_source = '', 
                            is_public = True, 
                            user_id = '', 
                            finetune_gpu_count = 56, 
                            inference_gpu_count = 56, )
                        ], ),
                update_time = '',
                cpod_id = '',
        )
        """

    def testCPODStatusReq(self):
        """Test CPODStatusReq"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
