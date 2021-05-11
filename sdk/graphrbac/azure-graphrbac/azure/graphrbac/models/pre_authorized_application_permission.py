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


class PreAuthorizedApplicationPermission(Model):
    """Contains information about the pre-authorized permissions.

    :param direct_access_grant: Indicates whether the permission set is
     DirectAccess or impersonation.
    :type direct_access_grant: bool
    :param access_grants: The list of permissions.
    :type access_grants: list[str]
    """

    _attribute_map = {
        'direct_access_grant': {'key': 'directAccessGrant', 'type': 'bool'},
        'access_grants': {'key': 'accessGrants', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(PreAuthorizedApplicationPermission, self).__init__(**kwargs)
        self.direct_access_grant = kwargs.get('direct_access_grant', None)
        self.access_grants = kwargs.get('access_grants', None)
