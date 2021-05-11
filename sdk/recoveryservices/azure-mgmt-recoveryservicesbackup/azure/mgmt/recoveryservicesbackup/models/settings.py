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


class Settings(Model):
    """Common settings field for backup management.

    :param time_zone: TimeZone optional input as string. For example: TimeZone
     = "Pacific Standard Time".
    :type time_zone: str
    :param issqlcompression: SQL compression flag
    :type issqlcompression: bool
    :param is_compression: Workload compression flag. This has been added so
     that 'isSqlCompression'
     will be deprecated once clients upgrade to consider this flag.
    :type is_compression: bool
    """

    _attribute_map = {
        'time_zone': {'key': 'timeZone', 'type': 'str'},
        'issqlcompression': {'key': 'issqlcompression', 'type': 'bool'},
        'is_compression': {'key': 'isCompression', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(Settings, self).__init__(**kwargs)
        self.time_zone = kwargs.get('time_zone', None)
        self.issqlcompression = kwargs.get('issqlcompression', None)
        self.is_compression = kwargs.get('is_compression', None)
