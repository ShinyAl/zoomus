"""Zoom.us REST API Python Client -- User component"""

from __future__ import absolute_import

from zoomus import util
from zoomus.components import base


class PhoneComponentV2(base.BaseComponent):
    def user_profile(self, **kwargs):
        util.require_keys(kwargs, ["user_id"])
        return self.get_request("/phone/users/{}".format(kwargs.get("user_id")), params=kwargs)

    def update_user_profile(self, **kwargs):
        util.require_keys(kwargs, ["user_id", "extension_number"])
        data = {"extension_number": kwargs.pop("extension_number")}
        return self.patch_request("/phone/users/{}".format(kwargs.get("user_id")), params=kwargs, data=data)

    def assign_phone_number(self, **kwargs):
        util.require_keys(kwargs, ["user_id", "phone_numbers"])
        data = {"phone_numbers": kwargs.pop("phone_numbers")}
        return self.post_request("/phone/users/{}/phone_numbers".format(kwargs.get("user_id")), params=kwargs, data=data)

    def unassign_phone_number(self, **kwargs):
        util.require_keys(kwargs, ["user_id", "phone_num_id"])
        return self.delete_request("/phone/users/{}/phone_numbers/{}".format(kwargs.get("user_id"), kwargs.get("phone_num_id")), params=kwargs)

    def assign_calling_plan(self, **kwargs):
        util.require_keys(kwargs, ["user_id", "calling_plans"])
        data = {"calling_plans": kwargs.pop("calling_plans")}
        return self.post_request("/phone/users/{}/calling_plans".format(kwargs.get("user_id")), params=kwargs, data=data)

    def unassign_calling_plan(self, **kwargs):
        util.require_keys(kwargs, ["user_id", "type"])
        return self.delete_request("/phone/users/{}/calling_plans/{}".format(kwargs.get("user_id"), kwargs.get("type")), params=kwargs)


