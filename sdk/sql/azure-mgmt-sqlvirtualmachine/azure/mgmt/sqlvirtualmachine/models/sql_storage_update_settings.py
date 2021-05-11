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


class SqlStorageUpdateSettings(Model):
    """Set disk storage settings for SQL Server.

    :param disk_count: Virtual machine disk count.
    :type disk_count: int
    :param starting_device_id: Device id of the first disk to be updated.
    :type starting_device_id: int
    :param disk_configuration_type: Disk configuration to apply to SQL Server.
     Possible values include: 'NEW', 'EXTEND', 'ADD'
    :type disk_configuration_type: str or
     ~azure.mgmt.sqlvirtualmachine.models.DiskConfigurationType
    """

    _attribute_map = {
        'disk_count': {'key': 'diskCount', 'type': 'int'},
        'starting_device_id': {'key': 'startingDeviceId', 'type': 'int'},
        'disk_configuration_type': {'key': 'diskConfigurationType', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SqlStorageUpdateSettings, self).__init__(**kwargs)
        self.disk_count = kwargs.get('disk_count', None)
        self.starting_device_id = kwargs.get('starting_device_id', None)
        self.disk_configuration_type = kwargs.get('disk_configuration_type', None)
