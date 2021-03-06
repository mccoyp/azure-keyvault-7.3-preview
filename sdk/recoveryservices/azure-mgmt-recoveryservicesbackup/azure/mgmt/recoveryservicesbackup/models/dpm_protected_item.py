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

from .protected_item import ProtectedItem


class DPMProtectedItem(ProtectedItem):
    """Additional information on Backup engine specific backup item.

    All required parameters must be populated in order to send to Azure.

    :param backup_management_type: Type of backup management for the backed up
     item. Possible values include: 'Invalid', 'AzureIaasVM', 'MAB', 'DPM',
     'AzureBackupServer', 'AzureSql', 'AzureStorage', 'AzureWorkload',
     'DefaultBackup'
    :type backup_management_type: str or
     ~azure.mgmt.recoveryservicesbackup.models.BackupManagementType
    :param workload_type: Type of workload this item represents. Possible
     values include: 'Invalid', 'VM', 'FileFolder', 'AzureSqlDb', 'SQLDB',
     'Exchange', 'Sharepoint', 'VMwareVM', 'SystemState', 'Client',
     'GenericDataSource', 'SQLDataBase', 'AzureFileShare', 'SAPHanaDatabase',
     'SAPAseDatabase'
    :type workload_type: str or
     ~azure.mgmt.recoveryservicesbackup.models.DataSourceType
    :param container_name: Unique name of container
    :type container_name: str
    :param source_resource_id: ARM ID of the resource to be backed up.
    :type source_resource_id: str
    :param policy_id: ID of the backup policy with which this item is backed
     up.
    :type policy_id: str
    :param last_recovery_point: Timestamp when the last (latest) backup copy
     was created for this backup item.
    :type last_recovery_point: datetime
    :param backup_set_name: Name of the backup set the backup item belongs to
    :type backup_set_name: str
    :param create_mode: Create mode to indicate recovery of existing soft
     deleted data source or creation of new data source. Possible values
     include: 'Invalid', 'Default', 'Recover'
    :type create_mode: str or
     ~azure.mgmt.recoveryservicesbackup.models.CreateMode
    :param protected_item_type: Required. Constant filled by server.
    :type protected_item_type: str
    :param friendly_name: Friendly name of the managed item
    :type friendly_name: str
    :param backup_engine_name: Backup Management server protecting this backup
     item
    :type backup_engine_name: str
    :param protection_state: Protection state of the backup engine. Possible
     values include: 'Invalid', 'IRPending', 'Protected', 'ProtectionError',
     'ProtectionStopped', 'ProtectionPaused'
    :type protection_state: str or
     ~azure.mgmt.recoveryservicesbackup.models.ProtectedItemState
    :param is_scheduled_for_deferred_delete: To check if backup item is
     scheduled for deferred delete
    :type is_scheduled_for_deferred_delete: bool
    :param extended_info: Extended info of the backup item.
    :type extended_info:
     ~azure.mgmt.recoveryservicesbackup.models.DPMProtectedItemExtendedInfo
    """

    _validation = {
        'protected_item_type': {'required': True},
    }

    _attribute_map = {
        'backup_management_type': {'key': 'backupManagementType', 'type': 'str'},
        'workload_type': {'key': 'workloadType', 'type': 'str'},
        'container_name': {'key': 'containerName', 'type': 'str'},
        'source_resource_id': {'key': 'sourceResourceId', 'type': 'str'},
        'policy_id': {'key': 'policyId', 'type': 'str'},
        'last_recovery_point': {'key': 'lastRecoveryPoint', 'type': 'iso-8601'},
        'backup_set_name': {'key': 'backupSetName', 'type': 'str'},
        'create_mode': {'key': 'createMode', 'type': 'str'},
        'protected_item_type': {'key': 'protectedItemType', 'type': 'str'},
        'friendly_name': {'key': 'friendlyName', 'type': 'str'},
        'backup_engine_name': {'key': 'backupEngineName', 'type': 'str'},
        'protection_state': {'key': 'protectionState', 'type': 'str'},
        'is_scheduled_for_deferred_delete': {'key': 'isScheduledForDeferredDelete', 'type': 'bool'},
        'extended_info': {'key': 'extendedInfo', 'type': 'DPMProtectedItemExtendedInfo'},
    }

    def __init__(self, **kwargs):
        super(DPMProtectedItem, self).__init__(**kwargs)
        self.friendly_name = kwargs.get('friendly_name', None)
        self.backup_engine_name = kwargs.get('backup_engine_name', None)
        self.protection_state = kwargs.get('protection_state', None)
        self.is_scheduled_for_deferred_delete = kwargs.get('is_scheduled_for_deferred_delete', None)
        self.extended_info = kwargs.get('extended_info', None)
        self.protected_item_type = 'DPMProtectedItem'
