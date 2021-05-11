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


class PartnerInfo(Model):
    """Partner server information for the failover group.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. Resource identifier of the partner server.
    :type id: str
    :ivar location: Geo location of the partner server.
    :vartype location: str
    :ivar replication_role: Replication role of the partner server. Possible
     values include: 'Primary', 'Secondary'
    :vartype replication_role: str or
     ~azure.mgmt.sql.models.FailoverGroupReplicationRole
    """

    _validation = {
        'id': {'required': True},
        'location': {'readonly': True},
        'replication_role': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'replication_role': {'key': 'replicationRole', 'type': 'str'},
    }

    def __init__(self, *, id: str, **kwargs) -> None:
        super(PartnerInfo, self).__init__(**kwargs)
        self.id = id
        self.location = None
        self.replication_role = None
