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


class ContainerGroupDiagnostics(Model):
    """Container group diagnostic information.

    :param log_analytics: Container group log analytics information.
    :type log_analytics: ~azure.mgmt.containerinstance.models.LogAnalytics
    """

    _attribute_map = {
        'log_analytics': {'key': 'logAnalytics', 'type': 'LogAnalytics'},
    }

    def __init__(self, *, log_analytics=None, **kwargs) -> None:
        super(ContainerGroupDiagnostics, self).__init__(**kwargs)
        self.log_analytics = log_analytics
