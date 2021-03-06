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


class RestoreOperation(Model):
    """Restore operation.

    :param status: Status of the restore operation.
    :type status: str
    :param status_details: The status details of restore operation.
    :type status_details: str
    :param error: Error encountered, if any, during the restore operation.
    :type error: ~backuprestore.models.Error
    :param job_id: Identifier for the restore operation.
    :type job_id: str
    :param start_time: The start time of the restore operation
    :type start_time: datetime
    :param end_time: The end time of the restore operation
    :type end_time: datetime
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'str'},
        'status_details': {'key': 'statusDetails', 'type': 'str'},
        'error': {'key': 'error', 'type': 'Error'},
        'job_id': {'key': 'jobId', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'unix-time'},
        'end_time': {'key': 'endTime', 'type': 'unix-time'},
    }

    def __init__(self, **kwargs):
        super(RestoreOperation, self).__init__(**kwargs)
        self.status = kwargs.get('status', None)
        self.status_details = kwargs.get('status_details', None)
        self.error = kwargs.get('error', None)
        self.job_id = kwargs.get('job_id', None)
        self.start_time = kwargs.get('start_time', None)
        self.end_time = kwargs.get('end_time', None)
