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

from .log_analytics_input_base_py3 import LogAnalyticsInputBase


class RequestRateByIntervalInput(LogAnalyticsInputBase):
    """Api request input for LogAnalytics getRequestRateByInterval Api.

    All required parameters must be populated in order to send to Azure.

    :param blob_container_sas_uri: Required. SAS Uri of the logging blob
     container to which LogAnalytics Api writes output logs to.
    :type blob_container_sas_uri: str
    :param from_time: Required. From time of the query
    :type from_time: datetime
    :param to_time: Required. To time of the query
    :type to_time: datetime
    :param group_by_throttle_policy: Group query result by Throttle Policy
     applied.
    :type group_by_throttle_policy: bool
    :param group_by_operation_name: Group query result by Operation Name.
    :type group_by_operation_name: bool
    :param group_by_resource_name: Group query result by Resource Name.
    :type group_by_resource_name: bool
    :param interval_length: Required. Interval value in minutes used to create
     LogAnalytics call rate logs. Possible values include: 'ThreeMins',
     'FiveMins', 'ThirtyMins', 'SixtyMins'
    :type interval_length: str or
     ~azure.mgmt.compute.v2019_03_01.models.IntervalInMins
    """

    _validation = {
        'blob_container_sas_uri': {'required': True},
        'from_time': {'required': True},
        'to_time': {'required': True},
        'interval_length': {'required': True},
    }

    _attribute_map = {
        'blob_container_sas_uri': {'key': 'blobContainerSasUri', 'type': 'str'},
        'from_time': {'key': 'fromTime', 'type': 'iso-8601'},
        'to_time': {'key': 'toTime', 'type': 'iso-8601'},
        'group_by_throttle_policy': {'key': 'groupByThrottlePolicy', 'type': 'bool'},
        'group_by_operation_name': {'key': 'groupByOperationName', 'type': 'bool'},
        'group_by_resource_name': {'key': 'groupByResourceName', 'type': 'bool'},
        'interval_length': {'key': 'intervalLength', 'type': 'IntervalInMins'},
    }

    def __init__(self, *, blob_container_sas_uri: str, from_time, to_time, interval_length, group_by_throttle_policy: bool=None, group_by_operation_name: bool=None, group_by_resource_name: bool=None, **kwargs) -> None:
        super(RequestRateByIntervalInput, self).__init__(blob_container_sas_uri=blob_container_sas_uri, from_time=from_time, to_time=to_time, group_by_throttle_policy=group_by_throttle_policy, group_by_operation_name=group_by_operation_name, group_by_resource_name=group_by_resource_name, **kwargs)
        self.interval_length = interval_length
