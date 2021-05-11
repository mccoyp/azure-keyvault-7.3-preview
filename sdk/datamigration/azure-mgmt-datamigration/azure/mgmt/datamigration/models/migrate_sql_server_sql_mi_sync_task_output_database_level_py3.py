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

from .migrate_sql_server_sql_mi_sync_task_output_py3 import MigrateSqlServerSqlMISyncTaskOutput


class MigrateSqlServerSqlMISyncTaskOutputDatabaseLevel(MigrateSqlServerSqlMISyncTaskOutput):
    """MigrateSqlServerSqlMISyncTaskOutputDatabaseLevel.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Result identifier
    :vartype id: str
    :param result_type: Required. Constant filled by server.
    :type result_type: str
    :ivar source_database_name: Name of the database
    :vartype source_database_name: str
    :ivar migration_state: Current state of database. Possible values include:
     'UNDEFINED', 'INITIAL', 'FULL_BACKUP_UPLOAD_START', 'LOG_SHIPPING_START',
     'UPLOAD_LOG_FILES_START', 'CUTOVER_START', 'POST_CUTOVER_COMPLETE',
     'COMPLETED', 'CANCELLED', 'FAILED'
    :vartype migration_state: str or
     ~azure.mgmt.datamigration.models.DatabaseMigrationState
    :ivar started_on: Database migration start time
    :vartype started_on: datetime
    :ivar ended_on: Database migration end time
    :vartype ended_on: datetime
    :ivar full_backup_set_info: Details of full backup set
    :vartype full_backup_set_info:
     ~azure.mgmt.datamigration.models.BackupSetInfo
    :ivar last_restored_backup_set_info: Last applied backup set information
    :vartype last_restored_backup_set_info:
     ~azure.mgmt.datamigration.models.BackupSetInfo
    :ivar active_backup_sets: Backup sets that are currently active (Either
     being uploaded or getting restored)
    :vartype active_backup_sets:
     list[~azure.mgmt.datamigration.models.BackupSetInfo]
    :ivar container_name: Name of container created in the Azure Storage
     account where backups are copied to
    :vartype container_name: str
    :ivar error_prefix: prefix string to use for querying errors for this
     database
    :vartype error_prefix: str
    :ivar is_full_backup_restored: Whether full backup has been applied to the
     target database or not
    :vartype is_full_backup_restored: bool
    :ivar exceptions_and_warnings: Migration exceptions and warnings
    :vartype exceptions_and_warnings:
     list[~azure.mgmt.datamigration.models.ReportableException]
    """

    _validation = {
        'id': {'readonly': True},
        'result_type': {'required': True},
        'source_database_name': {'readonly': True},
        'migration_state': {'readonly': True},
        'started_on': {'readonly': True},
        'ended_on': {'readonly': True},
        'full_backup_set_info': {'readonly': True},
        'last_restored_backup_set_info': {'readonly': True},
        'active_backup_sets': {'readonly': True},
        'container_name': {'readonly': True},
        'error_prefix': {'readonly': True},
        'is_full_backup_restored': {'readonly': True},
        'exceptions_and_warnings': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'result_type': {'key': 'resultType', 'type': 'str'},
        'source_database_name': {'key': 'sourceDatabaseName', 'type': 'str'},
        'migration_state': {'key': 'migrationState', 'type': 'str'},
        'started_on': {'key': 'startedOn', 'type': 'iso-8601'},
        'ended_on': {'key': 'endedOn', 'type': 'iso-8601'},
        'full_backup_set_info': {'key': 'fullBackupSetInfo', 'type': 'BackupSetInfo'},
        'last_restored_backup_set_info': {'key': 'lastRestoredBackupSetInfo', 'type': 'BackupSetInfo'},
        'active_backup_sets': {'key': 'activeBackupSets', 'type': '[BackupSetInfo]'},
        'container_name': {'key': 'containerName', 'type': 'str'},
        'error_prefix': {'key': 'errorPrefix', 'type': 'str'},
        'is_full_backup_restored': {'key': 'isFullBackupRestored', 'type': 'bool'},
        'exceptions_and_warnings': {'key': 'exceptionsAndWarnings', 'type': '[ReportableException]'},
    }

    def __init__(self, **kwargs) -> None:
        super(MigrateSqlServerSqlMISyncTaskOutputDatabaseLevel, self).__init__(**kwargs)
        self.source_database_name = None
        self.migration_state = None
        self.started_on = None
        self.ended_on = None
        self.full_backup_set_info = None
        self.last_restored_backup_set_info = None
        self.active_backup_sets = None
        self.container_name = None
        self.error_prefix = None
        self.is_full_backup_restored = None
        self.exceptions_and_warnings = None
        self.result_type = 'DatabaseLevelOutput'
