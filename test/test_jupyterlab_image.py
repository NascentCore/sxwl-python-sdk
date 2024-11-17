# coding: utf-8

"""
    调度器服务

    调度器服务的接口定义

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.jupyterlab_image import JupyterlabImage

class TestJupyterlabImage(unittest.TestCase):
    """JupyterlabImage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JupyterlabImage:
        """Test JupyterlabImage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JupyterlabImage`
        """
        model = JupyterlabImage()
        if include_optional:
            return JupyterlabImage(
                created_at = '',
                full_name = '',
                image_name = '',
                updated_at = ''
            )
        else:
            return JupyterlabImage(
                created_at = '',
                full_name = '',
                image_name = '',
                updated_at = '',
        )
        """

    def testJupyterlabImage(self):
        """Test JupyterlabImage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
