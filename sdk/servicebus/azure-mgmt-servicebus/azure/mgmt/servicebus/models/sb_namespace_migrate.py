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


class SBNamespaceMigrate(Model):
    """Namespace Migrate Object.

    All required parameters must be populated in order to send to Azure.

    :param target_namespace_type: Required. Type of namespaces. Possible
     values include: 'Messaging', 'NotificationHub', 'Mixed', 'EventHub',
     'Relay'
    :type target_namespace_type: str or
     ~azure.mgmt.servicebus.models.NameSpaceType
    """

    _validation = {
        'target_namespace_type': {'required': True},
    }

    _attribute_map = {
        'target_namespace_type': {'key': 'targetNamespaceType', 'type': 'NameSpaceType'},
    }

    def __init__(self, **kwargs):
        super(SBNamespaceMigrate, self).__init__(**kwargs)
        self.target_namespace_type = kwargs.get('target_namespace_type', None)
