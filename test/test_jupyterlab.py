# coding: utf-8

"""
    调度器服务

    调度器服务的接口定义

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.jupyterlab import Jupyterlab

class TestJupyterlab(unittest.TestCase):
    """Jupyterlab unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Jupyterlab:
        """Test Jupyterlab
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Jupyterlab`
        """
        model = Jupyterlab()
        if include_optional:
            return Jupyterlab(
                id = 56,
                job_name = '',
                instance_name = '',
                cpu_count = 56,
                memory = 56,
                cpod_id = '',
                gpu_count = 56,
                gpu_product = '',
                data_volume_size = 56,
                resource = openapi_client.models.jupyter_resource.JupyterResource(
                    models = [
                        openapi_client.models.model.Model(
                            model_id = '', 
                            model_name = '', 
                            model_path = '', 
                            model_size = 56, 
                            model_is_public = True, 
                            model_template = '', 
                            model_meta = '', 
                            model_category = '', )
                        ], 
                    datasets = [
                        openapi_client.models.dataset.Dataset(
                            dataset_id = '', 
                            dataset_name = '', 
                            dataset_path = '', 
                            dataset_size = 56, 
                            dataset_is_public = True, )
                        ], 
                    adapters = [
                        openapi_client.models.adapter.Adapter(
                            adapter_id = '', 
                            adapter_name = '', 
                            adapter_path = '', 
                            adapter_size = 56, 
                            adapter_is_public = True, )
                        ], ),
                url = '',
                user_id = '',
                status = ''
            )
        else:
            return Jupyterlab(
                instance_name = '',
                cpu_count = 56,
                memory = 56,
                data_volume_size = 56,
                resource = openapi_client.models.jupyter_resource.JupyterResource(
                    models = [
                        openapi_client.models.model.Model(
                            model_id = '', 
                            model_name = '', 
                            model_path = '', 
                            model_size = 56, 
                            model_is_public = True, 
                            model_template = '', 
                            model_meta = '', 
                            model_category = '', )
                        ], 
                    datasets = [
                        openapi_client.models.dataset.Dataset(
                            dataset_id = '', 
                            dataset_name = '', 
                            dataset_path = '', 
                            dataset_size = 56, 
                            dataset_is_public = True, )
                        ], 
                    adapters = [
                        openapi_client.models.adapter.Adapter(
                            adapter_id = '', 
                            adapter_name = '', 
                            adapter_path = '', 
                            adapter_size = 56, 
                            adapter_is_public = True, )
                        ], ),
        )
        """

    def testJupyterlab(self):
        """Test Jupyterlab"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
