# coding: utf-8

"""
    调度器服务

    调度器服务的接口定义

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.resource_task_update import ResourceTaskUpdate

class TestResourceTaskUpdate(unittest.TestCase):
    """ResourceTaskUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResourceTaskUpdate:
        """Test ResourceTaskUpdate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResourceTaskUpdate`
        """
        model = ResourceTaskUpdate()
        if include_optional:
            return ResourceTaskUpdate(
                resource_id = '',
                resource_type = '',
                source = '',
                size = 56,
                err = '',
                ok = True
            )
        else:
            return ResourceTaskUpdate(
                resource_id = '',
                resource_type = '',
                source = '',
                size = 56,
                err = '',
                ok = True,
        )
        """

    def testResourceTaskUpdate(self):
        """Test ResourceTaskUpdate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
