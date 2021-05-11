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


class RoleDefinitionCreateParameters(Model):
    """Role definition creation parameters.

    All required parameters must be populated in order to send to Azure.

    :param properties: Required. Role definition properties.
    :type properties: ~rbac.models.RoleDefinitionProperties
    """

    _validation = {
        'properties': {'required': True},
    }

    _attribute_map = {
        'properties': {'key': 'properties', 'type': 'RoleDefinitionProperties'},
    }

    def __init__(self, **kwargs):
        super(RoleDefinitionCreateParameters, self).__init__(**kwargs)
        self.properties = kwargs.get('properties', None)