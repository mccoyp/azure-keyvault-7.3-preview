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

from .sql_server_sql_mi_sync_task_input_py3 import SqlServerSqlMISyncTaskInput


class ValidateMigrationInputSqlServerSqlMISyncTaskInput(SqlServerSqlMISyncTaskInput):
    """Input for task that migrates SQL Server databases to Azure SQL Database
    Managed Instance online scenario.

    All required parameters must be populated in order to send to Azure.

    :param selected_databases: Required. Databases to migrate
    :type selected_databases:
     list[~azure.mgmt.datamigration.models.MigrateSqlServerSqlMIDatabaseInput]
    :param backup_file_share: Backup file share information for all selected
     databases.
    :type backup_file_share: ~azure.mgmt.datamigration.models.FileShare
    :param storage_resource_id: Required. Fully qualified resourceId of
     storage
    :type storage_resource_id: str
    :param source_connection_info: Required. Connection information for source
     SQL Server
    :type source_connection_info:
     ~azure.mgmt.datamigration.models.SqlConnectionInfo
    :param target_connection_info: Required. Connection information for Azure
     SQL Database Managed Instance
    :type target_connection_info:
     ~azure.mgmt.datamigration.models.MiSqlConnectionInfo
    :param azure_app: Required. Azure Active Directory Application the DMS
     instance will use to connect to the target instance of Azure SQL Database
     Managed Instance and the Azure Storage Account
    :type azure_app: ~azure.mgmt.datamigration.models.AzureActiveDirectoryApp
    """

    _validation = {
        'selected_databases': {'required': True},
        'storage_resource_id': {'required': True},
        'source_connection_info': {'required': True},
        'target_connection_info': {'required': True},
        'azure_app': {'required': True},
    }

    _attribute_map = {
        'selected_databases': {'key': 'selectedDatabases', 'type': '[MigrateSqlServerSqlMIDatabaseInput]'},
        'backup_file_share': {'key': 'backupFileShare', 'type': 'FileShare'},
        'storage_resource_id': {'key': 'storageResourceId', 'type': 'str'},
        'source_connection_info': {'key': 'sourceConnectionInfo', 'type': 'SqlConnectionInfo'},
        'target_connection_info': {'key': 'targetConnectionInfo', 'type': 'MiSqlConnectionInfo'},
        'azure_app': {'key': 'azureApp', 'type': 'AzureActiveDirectoryApp'},
    }

    def __init__(self, *, selected_databases, storage_resource_id: str, source_connection_info, target_connection_info, azure_app, backup_file_share=None, **kwargs) -> None:
        super(ValidateMigrationInputSqlServerSqlMISyncTaskInput, self).__init__(selected_databases=selected_databases, backup_file_share=backup_file_share, storage_resource_id=storage_resource_id, source_connection_info=source_connection_info, target_connection_info=target_connection_info, azure_app=azure_app, **kwargs)
