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


class CapabilitiesCapabilities(Model):
    """The supported capabilities.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar max_memory_in_gb: The maximum allowed memory request in GB.
    :vartype max_memory_in_gb: float
    :ivar max_cpu: The maximum allowed CPU request in cores.
    :vartype max_cpu: float
    :ivar max_gpu_count: The maximum allowed GPU count.
    :vartype max_gpu_count: float
    """

    _validation = {
        'max_memory_in_gb': {'readonly': True},
        'max_cpu': {'readonly': True},
        'max_gpu_count': {'readonly': True},
    }

    _attribute_map = {
        'max_memory_in_gb': {'key': 'maxMemoryInGB', 'type': 'float'},
        'max_cpu': {'key': 'maxCpu', 'type': 'float'},
        'max_gpu_count': {'key': 'maxGpuCount', 'type': 'float'},
    }

    def __init__(self, **kwargs) -> None:
        super(CapabilitiesCapabilities, self).__init__(**kwargs)
        self.max_memory_in_gb = None
        self.max_cpu = None
        self.max_gpu_count = None
