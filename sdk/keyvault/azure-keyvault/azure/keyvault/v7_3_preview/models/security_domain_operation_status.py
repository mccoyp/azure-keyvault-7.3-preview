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


class SecurityDomainOperationStatus(Model):
    """SecurityDomainOperationStatus.

    :param status: operation status. Possible values include: 'Success',
     'InProgress', 'Failed'
    :type status: str or ~securitydomain.models.OperationStatus
    :param status_details:
    :type status_details: str
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'OperationStatus'},
        'status_details': {'key': 'status_details', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SecurityDomainOperationStatus, self).__init__(**kwargs)
        self.status = kwargs.get('status', None)
        self.status_details = kwargs.get('status_details', None)
