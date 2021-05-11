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

from .tracked_resource_py3 import TrackedResource


class Domain(TrackedResource):
    """EventGrid Domain.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified identifier of the resource.
    :vartype id: str
    :ivar name: Name of the resource.
    :vartype name: str
    :ivar type: Type of the resource.
    :vartype type: str
    :param location: Required. Location of the resource.
    :type location: str
    :param tags: Tags of the resource.
    :type tags: dict[str, str]
    :ivar provisioning_state: Provisioning state of the domain. Possible
     values include: 'Creating', 'Updating', 'Deleting', 'Succeeded',
     'Canceled', 'Failed'
    :vartype provisioning_state: str or
     ~azure.mgmt.eventgrid.models.DomainProvisioningState
    :ivar endpoint: Endpoint for the domain.
    :vartype endpoint: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'provisioning_state': {'readonly': True},
        'endpoint': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'endpoint': {'key': 'properties.endpoint', 'type': 'str'},
    }

    def __init__(self, *, location: str, tags=None, **kwargs) -> None:
        super(Domain, self).__init__(location=location, tags=tags, **kwargs)
        self.provisioning_state = None
        self.endpoint = None
