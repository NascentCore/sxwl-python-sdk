# coding: utf-8

"""
    SDK

    算想云对开发者提供的API

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sxwl_client.models.model import Model

class TestModel(unittest.TestCase):
    """Model unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Model:
        """Test Model
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Model`
        """
        model = Model()
        if include_optional:
            return Model(
                model_id = '',
                model_name = '',
                model_path = '',
                model_size = 56,
                model_is_public = True,
                model_template = '',
                model_meta = '',
                model_category = ''
            )
        else:
            return Model(
                model_id = '',
                model_name = '',
                model_size = 56,
                model_is_public = True,
                model_template = '',
                model_meta = '',
                model_category = '',
        )
        """

    def testModel(self):
        """Test Model"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
