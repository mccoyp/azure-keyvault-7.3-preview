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

from .proxy_resource_py3 import ProxyResource


class AvailabilityGroupListener(ProxyResource):
    """A SQL Server availability group listener.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar provisioning_state: Provisioning state to track the async operation
     status.
    :vartype provisioning_state: str
    :param availability_group_name: Name of the availability group.
    :type availability_group_name: str
    :param load_balancer_configurations: List of load balancer configurations
     for an availability group listener.
    :type load_balancer_configurations:
     list[~azure.mgmt.sqlvirtualmachine.models.LoadBalancerConfiguration]
    :param create_default_availability_group_if_not_exist: Create a default
     availability group if it does not exist.
    :type create_default_availability_group_if_not_exist: bool
    :param port: Listener port.
    :type port: int
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'availability_group_name': {'key': 'properties.availabilityGroupName', 'type': 'str'},
        'load_balancer_configurations': {'key': 'properties.loadBalancerConfigurations', 'type': '[LoadBalancerConfiguration]'},
        'create_default_availability_group_if_not_exist': {'key': 'properties.createDefaultAvailabilityGroupIfNotExist', 'type': 'bool'},
        'port': {'key': 'properties.port', 'type': 'int'},
    }

    def __init__(self, *, availability_group_name: str=None, load_balancer_configurations=None, create_default_availability_group_if_not_exist: bool=None, port: int=None, **kwargs) -> None:
        super(AvailabilityGroupListener, self).__init__(**kwargs)
        self.provisioning_state = None
        self.availability_group_name = availability_group_name
        self.load_balancer_configurations = load_balancer_configurations
        self.create_default_availability_group_if_not_exist = create_default_availability_group_if_not_exist
        self.port = port
