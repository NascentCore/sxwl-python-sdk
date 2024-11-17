# coding: utf-8

"""
    SDK

    算想云对开发者提供的API

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from sxwl_client.models.hyperparameters import Hyperparameters
from typing import Optional, Set
from typing_extensions import Self

class FinetuneReq(BaseModel):
    """
    FinetuneReq
    """ # noqa: E501
    model_id: Optional[StrictStr] = Field(default=None, description=" 模型ID")
    model_name: Optional[StrictStr] = Field(default=None, description=" 模型名字, owner/model")
    model_path: Optional[StrictStr] = Field(default=None, description=" 模型的绑定路径")
    model_size: Optional[StrictInt] = Field(default=None, description=" 模型体积，单位字节")
    model_is_public: Optional[StrictBool] = Field(default=None, description=" 是否公共模型")
    model_template: Optional[StrictStr] = Field(default=None, description=" 模型的推理模版")
    model_meta: Optional[StrictStr] = Field(default=None, description=" 元信息")
    model_category: Optional[StrictStr] = Field(default=None, description=" 模型分类")
    dataset_id: Optional[StrictStr] = Field(default=None, description=" 数据集ID")
    dataset_name: Optional[StrictStr] = Field(default=None, description=" 数据集名字, owner/dataset")
    dataset_path: Optional[StrictStr] = Field(default=None, description=" 数据集的绑定路径")
    dataset_size: Optional[StrictInt] = Field(default=None, description=" 数据集体积，单位字节")
    dataset_is_public: Optional[StrictBool] = Field(default=None, description=" 是否公共数据集")
    cpod_id: Optional[StrictStr] = None
    gpu_model: Optional[StrictStr] = None
    gpu_count: Optional[StrictInt] = None
    trained_model_name: Optional[StrictStr] = Field(default=None, alias="trainedModelName")
    hyperparameters: Hyperparameters
    model_saved_type: StrictStr
    finetune_type: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["model_id", "model_name", "model_path", "model_size", "model_is_public", "model_template", "model_meta", "model_category", "dataset_id", "dataset_name", "dataset_path", "dataset_size", "dataset_is_public", "cpod_id", "gpu_model", "gpu_count", "trainedModelName", "hyperparameters", "model_saved_type", "finetune_type"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of FinetuneReq from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of hyperparameters
        if self.hyperparameters:
            _dict['hyperparameters'] = self.hyperparameters.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FinetuneReq from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "model_id": obj.get("model_id"),
            "model_name": obj.get("model_name"),
            "model_path": obj.get("model_path"),
            "model_size": obj.get("model_size"),
            "model_is_public": obj.get("model_is_public"),
            "model_template": obj.get("model_template"),
            "model_meta": obj.get("model_meta"),
            "model_category": obj.get("model_category"),
            "dataset_id": obj.get("dataset_id"),
            "dataset_name": obj.get("dataset_name"),
            "dataset_path": obj.get("dataset_path"),
            "dataset_size": obj.get("dataset_size"),
            "dataset_is_public": obj.get("dataset_is_public"),
            "cpod_id": obj.get("cpod_id"),
            "gpu_model": obj.get("gpu_model"),
            "gpu_count": obj.get("gpu_count"),
            "trainedModelName": obj.get("trainedModelName"),
            "hyperparameters": Hyperparameters.from_dict(obj["hyperparameters"]) if obj.get("hyperparameters") is not None else None,
            "model_saved_type": obj.get("model_saved_type"),
            "finetune_type": obj.get("finetune_type")
        })
        return _obj

