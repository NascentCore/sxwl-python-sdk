# coding: utf-8

"""
    调度器服务

    调度器服务的接口定义

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.job_call_back_req import JobCallBackReq

class TestJobCallBackReq(unittest.TestCase):
    """JobCallBackReq unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JobCallBackReq:
        """Test JobCallBackReq
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JobCallBackReq`
        """
        model = JobCallBackReq()
        if include_optional:
            return JobCallBackReq(
                status = '',
                url = '',
                job_id = ''
            )
        else:
            return JobCallBackReq(
                status = '',
                url = '',
                job_id = '',
        )
        """

    def testJobCallBackReq(self):
        """Test JobCallBackReq"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
