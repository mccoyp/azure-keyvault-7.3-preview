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


class VirtualMachineScaleSetUpdateStorageProfile(Model):
    """Describes a virtual machine scale set storage profile.

    :param image_reference: The image reference.
    :type image_reference:
     ~azure.mgmt.compute.v2017_12_01.models.ImageReference
    :param os_disk: The OS disk.
    :type os_disk:
     ~azure.mgmt.compute.v2017_12_01.models.VirtualMachineScaleSetUpdateOSDisk
    :param data_disks: The data disks.
    :type data_disks:
     list[~azure.mgmt.compute.v2017_12_01.models.VirtualMachineScaleSetDataDisk]
    """

    _attribute_map = {
        'image_reference': {'key': 'imageReference', 'type': 'ImageReference'},
        'os_disk': {'key': 'osDisk', 'type': 'VirtualMachineScaleSetUpdateOSDisk'},
        'data_disks': {'key': 'dataDisks', 'type': '[VirtualMachineScaleSetDataDisk]'},
    }

    def __init__(self, **kwargs):
        super(VirtualMachineScaleSetUpdateStorageProfile, self).__init__(**kwargs)
        self.image_reference = kwargs.get('image_reference', None)
        self.os_disk = kwargs.get('os_disk', None)
        self.data_disks = kwargs.get('data_disks', None)
