# coding: utf-8

"""
    调度器服务

    调度器服务的接口定义

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.user_list_resp import UserListResp

class TestUserListResp(unittest.TestCase):
    """UserListResp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserListResp:
        """Test UserListResp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserListResp`
        """
        model = UserListResp()
        if include_optional:
            return UserListResp(
                data = [
                    openapi_client.models.user.User(
                        user_id = '', 
                        user_name = '', )
                    ]
            )
        else:
            return UserListResp(
                data = [
                    openapi_client.models.user.User(
                        user_id = '', 
                        user_name = '', )
                    ],
        )
        """

    def testUserListResp(self):
        """Test UserListResp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
