# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SkuProperty(Model):
    """SkuProperty.

    :param name: An invariant to describe the feature.
    :type name: str
    :param value: An invariant if the feature is measured by quantity.
    :type value: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SkuProperty, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.value = kwargs.get('value', None)
