# coding: utf-8

"""
    调度器服务

    调度器服务的接口定义

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.billing_list_resp import BillingListResp

class TestBillingListResp(unittest.TestCase):
    """BillingListResp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BillingListResp:
        """Test BillingListResp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BillingListResp`
        """
        model = BillingListResp()
        if include_optional:
            return BillingListResp(
                data = [
                    openapi_client.models.user_billing.UserBilling(
                        billing_id = '', 
                        user_id = '', 
                        amount = 1.337, 
                        billing_status = 56, 
                        job_id = '', 
                        job_type = '', 
                        billing_time = '', 
                        payment_time = '', 
                        description = '', )
                    ]
            )
        else:
            return BillingListResp(
                data = [
                    openapi_client.models.user_billing.UserBilling(
                        billing_id = '', 
                        user_id = '', 
                        amount = 1.337, 
                        billing_status = 56, 
                        job_id = '', 
                        job_type = '', 
                        billing_time = '', 
                        payment_time = '', 
                        description = '', )
                    ],
        )
        """

    def testBillingListResp(self):
        """Test BillingListResp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
