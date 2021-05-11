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


class MetricsResultsItem(Model):
    """MetricsResultsItem.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. The specified ID for this metric.
    :type id: str
    :param status: Required. The HTTP status code of this metric query.
    :type status: int
    :param body: Required. The results of this metric query.
    :type body: ~azure.applicationinsights.models.MetricsResult
    """

    _validation = {
        'id': {'required': True},
        'status': {'required': True},
        'body': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'status': {'key': 'status', 'type': 'int'},
        'body': {'key': 'body', 'type': 'MetricsResult'},
    }

    def __init__(self, **kwargs):
        super(MetricsResultsItem, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.status = kwargs.get('status', None)
        self.body = kwargs.get('body', None)
