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

from .service_principal_base import ServicePrincipalBase


class ServicePrincipalUpdateParameters(ServicePrincipalBase):
    """Request parameters for update an existing service principal.

    :param account_enabled: whether or not the service principal account is
     enabled
    :type account_enabled: bool
    :param app_role_assignment_required: Specifies whether an
     AppRoleAssignment to a user or group is required before Azure AD will
     issue a user or access token to the application.
    :type app_role_assignment_required: bool
    :param key_credentials: The collection of key credentials associated with
     the service principal.
    :type key_credentials: list[~azure.graphrbac.models.KeyCredential]
    :param password_credentials: The collection of password credentials
     associated with the service principal.
    :type password_credentials:
     list[~azure.graphrbac.models.PasswordCredential]
    :param service_principal_type: the type of the service principal
    :type service_principal_type: str
    :param tags: Optional list of tags that you can apply to your service
     principals. Not nullable.
    :type tags: list[str]
    """

    _attribute_map = {
        'account_enabled': {'key': 'accountEnabled', 'type': 'bool'},
        'app_role_assignment_required': {'key': 'appRoleAssignmentRequired', 'type': 'bool'},
        'key_credentials': {'key': 'keyCredentials', 'type': '[KeyCredential]'},
        'password_credentials': {'key': 'passwordCredentials', 'type': '[PasswordCredential]'},
        'service_principal_type': {'key': 'servicePrincipalType', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(ServicePrincipalUpdateParameters, self).__init__(**kwargs)
