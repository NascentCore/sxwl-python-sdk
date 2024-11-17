# coding: utf-8

"""
    调度器服务

    调度器服务的接口定义

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.cluster_node import ClusterNode

class TestClusterNode(unittest.TestCase):
    """ClusterNode unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClusterNode:
        """Test ClusterNode
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClusterNode`
        """
        model = ClusterNode()
        if include_optional:
            return ClusterNode(
                node_role = '',
                node_name = '',
                node_ip = '',
                ssh_port = 56,
                ssh_user = '',
                ssh_password = ''
            )
        else:
            return ClusterNode(
                node_role = '',
                node_name = '',
                node_ip = '',
                ssh_port = 56,
                ssh_user = '',
                ssh_password = '',
        )
        """

    def testClusterNode(self):
        """Test ClusterNode"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
