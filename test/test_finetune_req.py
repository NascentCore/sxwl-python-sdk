# coding: utf-8

"""
    SDK

    算想云对开发者提供的API

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.finetune_req import FinetuneReq

class TestFinetuneReq(unittest.TestCase):
    """FinetuneReq unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FinetuneReq:
        """Test FinetuneReq
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FinetuneReq`
        """
        model = FinetuneReq()
        if include_optional:
            return FinetuneReq(
                model_id = '',
                model_name = '',
                model_path = '',
                model_size = 56,
                model_is_public = True,
                model_template = '',
                model_meta = '',
                model_category = '',
                dataset_id = '',
                dataset_name = '',
                dataset_path = '',
                dataset_size = 56,
                dataset_is_public = True,
                cpod_id = '',
                gpu_model = '',
                gpu_count = 56,
                trained_model_name = '',
                hyperparameters = None,
                config = None,
                model_saved_type = '',
                finetune_type = ''
            )
        else:
            return FinetuneReq(
                model_saved_type = '',
        )
        """

    def testFinetuneReq(self):
        """Test FinetuneReq"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
