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

from .azure_workload_point_in_time_recovery_point_py3 import AzureWorkloadPointInTimeRecoveryPoint


class AzureWorkloadSAPHanaPointInTimeRecoveryPoint(AzureWorkloadPointInTimeRecoveryPoint):
    """Recovery point specific to PointInTime in SAPHana.

    All required parameters must be populated in order to send to Azure.

    :param object_type: Required. Constant filled by server.
    :type object_type: str
    :param recovery_point_time_in_utc: UTC time at which recovery point was
     created
    :type recovery_point_time_in_utc: datetime
    :param type: Type of restore point. Possible values include: 'Invalid',
     'Full', 'Log', 'Differential'
    :type type: str or
     ~azure.mgmt.recoveryservicesbackup.models.RestorePointType
    :param time_ranges: List of log ranges
    :type time_ranges:
     list[~azure.mgmt.recoveryservicesbackup.models.PointInTimeRange]
    """

    _validation = {
        'object_type': {'required': True},
    }

    _attribute_map = {
        'object_type': {'key': 'objectType', 'type': 'str'},
        'recovery_point_time_in_utc': {'key': 'recoveryPointTimeInUTC', 'type': 'iso-8601'},
        'type': {'key': 'type', 'type': 'str'},
        'time_ranges': {'key': 'timeRanges', 'type': '[PointInTimeRange]'},
    }

    def __init__(self, *, recovery_point_time_in_utc=None, type=None, time_ranges=None, **kwargs) -> None:
        super(AzureWorkloadSAPHanaPointInTimeRecoveryPoint, self).__init__(recovery_point_time_in_utc=recovery_point_time_in_utc, type=type, time_ranges=time_ranges, **kwargs)
        self.object_type = 'AzureWorkloadSAPHanaPointInTimeRecoveryPoint'
