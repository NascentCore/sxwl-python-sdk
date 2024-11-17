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
from typing import Optional, Set
from typing_extensions import Self

class Adapter(BaseModel):
    """
    Adapter
    """ # noqa: E501
    adapter_id: StrictStr = Field(description=" 适配器ID")
    adapter_name: StrictStr = Field(description=" 适配器名字, owner/adapter")
    adapter_path: Optional[StrictStr] = Field(default=None, description=" 适配器的绑定路径")
    adapter_size: StrictInt = Field(description=" 适配器体积，单位字节")
    adapter_is_public: StrictBool = Field(description=" 是否公共适配器")
    __properties: ClassVar[List[str]] = ["adapter_id", "adapter_name", "adapter_path", "adapter_size", "adapter_is_public"]

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
        """Create an instance of Adapter from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Adapter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "adapter_id": obj.get("adapter_id"),
            "adapter_name": obj.get("adapter_name"),
            "adapter_path": obj.get("adapter_path"),
            "adapter_size": obj.get("adapter_size"),
            "adapter_is_public": obj.get("adapter_is_public")
        })
        return _obj

