# coding: utf-8

"""
    调度器服务

    调度器服务的接口定义

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.wrap_user import WrapUser

class TestWrapUser(unittest.TestCase):
    """WrapUser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WrapUser:
        """Test WrapUser
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WrapUser`
        """
        model = WrapUser()
        if include_optional:
            return WrapUser(
                user = openapi_client.models.user_info.UserInfo(
                    company_id = '', 
                    create_by = '', 
                    create_time = '', 
                    email = '', 
                    enabled = True, 
                    id = 56, 
                    user_id = '', 
                    is_admin = True, 
                    update_by = '', 
                    update_time = '', 
                    user_type = 56, 
                    username = '', )
            )
        else:
            return WrapUser(
                user = openapi_client.models.user_info.UserInfo(
                    company_id = '', 
                    create_by = '', 
                    create_time = '', 
                    email = '', 
                    enabled = True, 
                    id = 56, 
                    user_id = '', 
                    is_admin = True, 
                    update_by = '', 
                    update_time = '', 
                    user_type = 56, 
                    username = '', ),
        )
        """

    def testWrapUser(self):
        """Test WrapUser"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
