# coding: utf-8

"""
    SDK

    算想云对开发者提供的API

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sxwl_client.models.adapter_by_name_req import AdapterByNameReq

class TestAdapterByNameReq(unittest.TestCase):
    """AdapterByNameReq unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdapterByNameReq:
        """Test AdapterByNameReq
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdapterByNameReq`
        """
        model = AdapterByNameReq()
        if include_optional:
            return AdapterByNameReq(
                adapter_name = ''
            )
        else:
            return AdapterByNameReq(
                adapter_name = '',
        )
        """

    def testAdapterByNameReq(self):
        """Test AdapterByNameReq"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
