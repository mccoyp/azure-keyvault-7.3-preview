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


class ContainerServiceCustomProfile(Model):
    """Properties to configure a custom container service cluster.

    All required parameters must be populated in order to send to Azure.

    :param orchestrator: Required. The name of the custom orchestrator to use.
    :type orchestrator: str
    """

    _validation = {
        'orchestrator': {'required': True},
    }

    _attribute_map = {
        'orchestrator': {'key': 'orchestrator', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ContainerServiceCustomProfile, self).__init__(**kwargs)
        self.orchestrator = kwargs.get('orchestrator', None)
