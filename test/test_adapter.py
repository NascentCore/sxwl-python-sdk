# coding: utf-8

"""
    调度器服务

    调度器服务的接口定义

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.adapter import Adapter

class TestAdapter(unittest.TestCase):
    """Adapter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Adapter:
        """Test Adapter
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Adapter`
        """
        model = Adapter()
        if include_optional:
            return Adapter(
                adapter_id = '',
                adapter_name = '',
                adapter_path = '',
                adapter_size = 56,
                adapter_is_public = True
            )
        else:
            return Adapter(
                adapter_id = '',
                adapter_name = '',
                adapter_size = 56,
                adapter_is_public = True,
        )
        """

    def testAdapter(self):
        """Test Adapter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
