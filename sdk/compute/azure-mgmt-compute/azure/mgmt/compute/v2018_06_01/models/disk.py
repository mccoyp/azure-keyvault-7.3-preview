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

from .resource import Resource


class Disk(Resource):
    """Disk resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Required. Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :ivar managed_by: A relative URI containing the ID of the VM that has the
     disk attached.
    :vartype managed_by: str
    :param sku:
    :type sku: ~azure.mgmt.compute.v2018_06_01.models.DiskSku
    :param zones: The Logical zone list for Disk.
    :type zones: list[str]
    :ivar time_created: The time when the disk was created.
    :vartype time_created: datetime
    :param os_type: The Operating System type. Possible values include:
     'Windows', 'Linux'
    :type os_type: str or
     ~azure.mgmt.compute.v2018_06_01.models.OperatingSystemTypes
    :param creation_data: Required. Disk source information. CreationData
     information cannot be changed after the disk has been created.
    :type creation_data: ~azure.mgmt.compute.v2018_06_01.models.CreationData
    :param disk_size_gb: If creationData.createOption is Empty, this field is
     mandatory and it indicates the size of the VHD to create. If this field is
     present for updates or creation with other options, it indicates a resize.
     Resizes are only allowed if the disk is not attached to a running VM, and
     can only increase the disk's size.
    :type disk_size_gb: int
    :param encryption_settings: Encryption settings for disk or snapshot
    :type encryption_settings:
     ~azure.mgmt.compute.v2018_06_01.models.EncryptionSettings
    :ivar provisioning_state: The disk provisioning state.
    :vartype provisioning_state: str
    :param disk_iops_read_write: The number of IOPS allowed for this disk;
     only settable for UltraSSD disks. One operation can transfer between 4k
     and 256k bytes. For a description of the range of values you can set, see
     [Ultra SSD Managed Disk
     Offerings](https://docs.microsoft.com/azure/virtual-machines/windows/disks-ultra-ssd#ultra-ssd-managed-disk-offerings).
    :type disk_iops_read_write: long
    :param disk_mbps_read_write: The bandwidth allowed for this disk; only
     settable for UltraSSD disks. MBps means millions of bytes per second - MB
     here uses the ISO notation, of powers of 10. For a description of the
     range of values you can set, see [Ultra SSD Managed Disk
     Offerings](https://docs.microsoft.com/azure/virtual-machines/windows/disks-ultra-ssd#ultra-ssd-managed-disk-offerings).
    :type disk_mbps_read_write: int
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'managed_by': {'readonly': True},
        'time_created': {'readonly': True},
        'creation_data': {'required': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'managed_by': {'key': 'managedBy', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'DiskSku'},
        'zones': {'key': 'zones', 'type': '[str]'},
        'time_created': {'key': 'properties.timeCreated', 'type': 'iso-8601'},
        'os_type': {'key': 'properties.osType', 'type': 'OperatingSystemTypes'},
        'creation_data': {'key': 'properties.creationData', 'type': 'CreationData'},
        'disk_size_gb': {'key': 'properties.diskSizeGB', 'type': 'int'},
        'encryption_settings': {'key': 'properties.encryptionSettings', 'type': 'EncryptionSettings'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'disk_iops_read_write': {'key': 'properties.diskIOPSReadWrite', 'type': 'long'},
        'disk_mbps_read_write': {'key': 'properties.diskMBpsReadWrite', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(Disk, self).__init__(**kwargs)
        self.managed_by = None
        self.sku = kwargs.get('sku', None)
        self.zones = kwargs.get('zones', None)
        self.time_created = None
        self.os_type = kwargs.get('os_type', None)
        self.creation_data = kwargs.get('creation_data', None)
        self.disk_size_gb = kwargs.get('disk_size_gb', None)
        self.encryption_settings = kwargs.get('encryption_settings', None)
        self.provisioning_state = None
        self.disk_iops_read_write = kwargs.get('disk_iops_read_write', None)
        self.disk_mbps_read_write = kwargs.get('disk_mbps_read_write', None)
