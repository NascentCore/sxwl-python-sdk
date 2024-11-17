# coding: utf-8

"""
    调度器服务

    调度器服务的接口定义

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.gpu_type_resp import GPUTypeResp

class TestGPUTypeResp(unittest.TestCase):
    """GPUTypeResp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GPUTypeResp:
        """Test GPUTypeResp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GPUTypeResp`
        """
        model = GPUTypeResp()
        if include_optional:
            return GPUTypeResp(
                amount = 1.337,
                gpu_prod = '',
                gpu_allocatable = 56
            )
        else:
            return GPUTypeResp(
                amount = 1.337,
                gpu_prod = '',
                gpu_allocatable = 56,
        )
        """

    def testGPUTypeResp(self):
        """Test GPUTypeResp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
