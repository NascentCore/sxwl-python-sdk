# coding: utf-8

"""
    SDK

    算想云对开发者提供的API

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sxwl_client.models.inference_status_req import InferenceStatusReq

class TestInferenceStatusReq(unittest.TestCase):
    """InferenceStatusReq unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InferenceStatusReq:
        """Test InferenceStatusReq
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InferenceStatusReq`
        """
        model = InferenceStatusReq()
        if include_optional:
            return InferenceStatusReq(
                service_name = ''
            )
        else:
            return InferenceStatusReq(
                service_name = '',
        )
        """

    def testInferenceStatusReq(self):
        """Test InferenceStatusReq"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
