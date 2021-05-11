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

from .azure_workload_sql_restore_request_py3 import AzureWorkloadSQLRestoreRequest


class AzureWorkloadSQLPointInTimeRestoreRequest(AzureWorkloadSQLRestoreRequest):
    """AzureWorkload SQL -specific restore. Specifically for PointInTime/Log
    restore.

    All required parameters must be populated in order to send to Azure.

    :param object_type: Required. Constant filled by server.
    :type object_type: str
    :param recovery_type: OLR/ALR, RestoreDisks is invalid option. Possible
     values include: 'Invalid', 'OriginalLocation', 'AlternateLocation',
     'RestoreDisks'
    :type recovery_type: str or
     ~azure.mgmt.recoveryservicesbackup.models.RecoveryType
    :param source_resource_id: Fully qualified ARM ID of the VM on which
     workload that was running is being recovered.
    :type source_resource_id: str
    :param property_bag: Workload specific property bag.
    :type property_bag: dict[str, str]
    :param target_info: Details of target database
    :type target_info:
     ~azure.mgmt.recoveryservicesbackup.models.TargetRestoreInfo
    :param should_use_alternate_target_location: Default option set to true.
     If this is set to false, alternate data directory must be provided
    :type should_use_alternate_target_location: bool
    :param is_non_recoverable: SQL specific property where user can chose to
     set no-recovery when restore operation is tried
    :type is_non_recoverable: bool
    :param alternate_directory_paths: Data directory details
    :type alternate_directory_paths:
     list[~azure.mgmt.recoveryservicesbackup.models.SQLDataDirectoryMapping]
    :param point_in_time: PointInTime value
    :type point_in_time: datetime
    """

    _validation = {
        'object_type': {'required': True},
    }

    _attribute_map = {
        'object_type': {'key': 'objectType', 'type': 'str'},
        'recovery_type': {'key': 'recoveryType', 'type': 'str'},
        'source_resource_id': {'key': 'sourceResourceId', 'type': 'str'},
        'property_bag': {'key': 'propertyBag', 'type': '{str}'},
        'target_info': {'key': 'targetInfo', 'type': 'TargetRestoreInfo'},
        'should_use_alternate_target_location': {'key': 'shouldUseAlternateTargetLocation', 'type': 'bool'},
        'is_non_recoverable': {'key': 'isNonRecoverable', 'type': 'bool'},
        'alternate_directory_paths': {'key': 'alternateDirectoryPaths', 'type': '[SQLDataDirectoryMapping]'},
        'point_in_time': {'key': 'pointInTime', 'type': 'iso-8601'},
    }

    def __init__(self, *, recovery_type=None, source_resource_id: str=None, property_bag=None, target_info=None, should_use_alternate_target_location: bool=None, is_non_recoverable: bool=None, alternate_directory_paths=None, point_in_time=None, **kwargs) -> None:
        super(AzureWorkloadSQLPointInTimeRestoreRequest, self).__init__(recovery_type=recovery_type, source_resource_id=source_resource_id, property_bag=property_bag, target_info=target_info, should_use_alternate_target_location=should_use_alternate_target_location, is_non_recoverable=is_non_recoverable, alternate_directory_paths=alternate_directory_paths, **kwargs)
        self.point_in_time = point_in_time
        self.object_type = 'AzureWorkloadSQLPointInTimeRestoreRequest'
