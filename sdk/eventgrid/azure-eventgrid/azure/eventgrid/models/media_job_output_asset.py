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

from .media_job_output import MediaJobOutput


class MediaJobOutputAsset(MediaJobOutput):
    """The event data for a Job output asset.

    All required parameters must be populated in order to send to Azure.

    :param error: Gets the Job output error.
    :type error: ~azure.eventgrid.models.MediaJobError
    :param label: Gets the Job output label.
    :type label: str
    :param progress: Required. Gets the Job output progress.
    :type progress: long
    :param state: Required. Gets the Job output state. Possible values
     include: 'Canceled', 'Canceling', 'Error', 'Finished', 'Processing',
     'Queued', 'Scheduled'
    :type state: str or ~azure.eventgrid.models.MediaJobState
    :param odatatype: Required. Constant filled by server.
    :type odatatype: str
    :param asset_name: Gets the Job output asset name.
    :type asset_name: str
    """

    _validation = {
        'progress': {'required': True},
        'state': {'required': True},
        'odatatype': {'required': True},
    }

    _attribute_map = {
        'error': {'key': 'error', 'type': 'MediaJobError'},
        'label': {'key': 'label', 'type': 'str'},
        'progress': {'key': 'progress', 'type': 'long'},
        'state': {'key': 'state', 'type': 'MediaJobState'},
        'odatatype': {'key': '@odata\\.type', 'type': 'str'},
        'asset_name': {'key': 'assetName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(MediaJobOutputAsset, self).__init__(**kwargs)
        self.asset_name = kwargs.get('asset_name', None)
        self.odatatype = '#Microsoft.Media.JobOutputAsset'
