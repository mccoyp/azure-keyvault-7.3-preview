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


class ConnectToSourceSqlServerTaskInput(Model):
    """Input for the task that validates connection to SQL Server and also
    validates source server requirements.

    All required parameters must be populated in order to send to Azure.

    :param source_connection_info: Required. Connection information for Source
     SQL Server
    :type source_connection_info:
     ~azure.mgmt.datamigration.models.SqlConnectionInfo
    :param check_permissions_group: Permission group for validations. Possible
     values include: 'Default', 'MigrationFromSqlServerToAzureDB',
     'MigrationFromSqlServerToAzureMI', 'MigrationFromMySQLToAzureDBForMySQL'
    :type check_permissions_group: str or
     ~azure.mgmt.datamigration.models.ServerLevelPermissionsGroup
    :param collect_logins: Flag for whether to collect logins from source
     server. Default value: False .
    :type collect_logins: bool
    :param collect_agent_jobs: Flag for whether to collect agent jobs from
     source server. Default value: False .
    :type collect_agent_jobs: bool
    :param collect_tde_certificate_info: Flag for whether to collect TDE
     Certificate names from source server. Default value: False .
    :type collect_tde_certificate_info: bool
    """

    _validation = {
        'source_connection_info': {'required': True},
    }

    _attribute_map = {
        'source_connection_info': {'key': 'sourceConnectionInfo', 'type': 'SqlConnectionInfo'},
        'check_permissions_group': {'key': 'checkPermissionsGroup', 'type': 'ServerLevelPermissionsGroup'},
        'collect_logins': {'key': 'collectLogins', 'type': 'bool'},
        'collect_agent_jobs': {'key': 'collectAgentJobs', 'type': 'bool'},
        'collect_tde_certificate_info': {'key': 'collectTdeCertificateInfo', 'type': 'bool'},
    }

    def __init__(self, *, source_connection_info, check_permissions_group=None, collect_logins: bool=False, collect_agent_jobs: bool=False, collect_tde_certificate_info: bool=False, **kwargs) -> None:
        super(ConnectToSourceSqlServerTaskInput, self).__init__(**kwargs)
        self.source_connection_info = source_connection_info
        self.check_permissions_group = check_permissions_group
        self.collect_logins = collect_logins
        self.collect_agent_jobs = collect_agent_jobs
        self.collect_tde_certificate_info = collect_tde_certificate_info
