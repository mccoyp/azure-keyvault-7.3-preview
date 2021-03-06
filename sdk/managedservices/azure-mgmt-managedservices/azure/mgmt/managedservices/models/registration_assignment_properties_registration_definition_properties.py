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


class RegistrationAssignmentPropertiesRegistrationDefinitionProperties(Model):
    """Properties of registration definition inside registration assignment.

    :param description: Description of the registration definition.
    :type description: str
    :param authorizations: Authorization tuple containing principal id of the
     user/security group or service principal and id of the build-in role.
    :type authorizations:
     list[~azure.mgmt.managedservices.models.Authorization]
    :param registration_definition_name: Name of the registration definition.
    :type registration_definition_name: str
    :param provisioning_state: Current state of the registration definition.
     Possible values include: 'NotSpecified', 'Accepted', 'Running', 'Ready',
     'Creating', 'Created', 'Deleting', 'Deleted', 'Canceled', 'Failed',
     'Succeeded', 'Updating'
    :type provisioning_state: str or
     ~azure.mgmt.managedservices.models.ProvisioningState
    :param managee_tenant_id: Id of the home tenant.
    :type managee_tenant_id: str
    :param managee_tenant_name: Name of the home tenant.
    :type managee_tenant_name: str
    :param managed_by_tenant_id: Id of the managedBy tenant.
    :type managed_by_tenant_id: str
    :param managed_by_tenant_name: Name of the managedBy tenant.
    :type managed_by_tenant_name: str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'authorizations': {'key': 'authorizations', 'type': '[Authorization]'},
        'registration_definition_name': {'key': 'registrationDefinitionName', 'type': 'str'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'ProvisioningState'},
        'managee_tenant_id': {'key': 'manageeTenantId', 'type': 'str'},
        'managee_tenant_name': {'key': 'manageeTenantName', 'type': 'str'},
        'managed_by_tenant_id': {'key': 'managedByTenantId', 'type': 'str'},
        'managed_by_tenant_name': {'key': 'managedByTenantName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(RegistrationAssignmentPropertiesRegistrationDefinitionProperties, self).__init__(**kwargs)
        self.description = kwargs.get('description', None)
        self.authorizations = kwargs.get('authorizations', None)
        self.registration_definition_name = kwargs.get('registration_definition_name', None)
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.managee_tenant_id = kwargs.get('managee_tenant_id', None)
        self.managee_tenant_name = kwargs.get('managee_tenant_name', None)
        self.managed_by_tenant_id = kwargs.get('managed_by_tenant_id', None)
        self.managed_by_tenant_name = kwargs.get('managed_by_tenant_name', None)
