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


class QuotaCounterValueContract(Model):
    """Quota counter value details.

    :param calls_count: Number of times Counter was called.
    :type calls_count: int
    :param kb_transferred: Data Transferred in KiloBytes.
    :type kb_transferred: float
    """

    _attribute_map = {
        'calls_count': {'key': 'value.callsCount', 'type': 'int'},
        'kb_transferred': {'key': 'value.kbTransferred', 'type': 'float'},
    }

    def __init__(self, *, calls_count: int=None, kb_transferred: float=None, **kwargs) -> None:
        super(QuotaCounterValueContract, self).__init__(**kwargs)
        self.calls_count = calls_count
        self.kb_transferred = kb_transferred
