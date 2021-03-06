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


class Cluster(Resource):
    """The cluster resource
    .

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource identifier.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :param location: Required. Azure resource location.
    :type location: str
    :param tags: Azure resource tags.
    :type tags: dict[str, str]
    :ivar etag: Azure resource etag.
    :vartype etag: str
    :param add_on_features: The list of add-on features to enable in the
     cluster.
    :type add_on_features: list[str]
    :ivar available_cluster_versions: The Service Fabric runtime versions
     available for this cluster.
    :vartype available_cluster_versions:
     list[~azure.mgmt.servicefabric.models.ClusterVersionDetails]
    :param azure_active_directory: The AAD authentication settings of the
     cluster.
    :type azure_active_directory:
     ~azure.mgmt.servicefabric.models.AzureActiveDirectory
    :param certificate: The certificate to use for securing the cluster. The
     certificate provided will be used for node to node security within the
     cluster, SSL certificate for cluster management endpoint and default admin
     client.
    :type certificate: ~azure.mgmt.servicefabric.models.CertificateDescription
    :param certificate_common_names: Describes a list of server certificates
     referenced by common name that are used to secure the cluster.
    :type certificate_common_names:
     ~azure.mgmt.servicefabric.models.ServerCertificateCommonNames
    :param client_certificate_common_names: The list of client certificates
     referenced by common name that are allowed to manage the cluster.
    :type client_certificate_common_names:
     list[~azure.mgmt.servicefabric.models.ClientCertificateCommonName]
    :param client_certificate_thumbprints: The list of client certificates
     referenced by thumbprint that are allowed to manage the cluster.
    :type client_certificate_thumbprints:
     list[~azure.mgmt.servicefabric.models.ClientCertificateThumbprint]
    :param cluster_code_version: The Service Fabric runtime version of the
     cluster. This property can only by set the user when **upgradeMode** is
     set to 'Manual'. To get list of available Service Fabric versions for new
     clusters use [ClusterVersion API](./ClusterVersion.md). To get the list of
     available version for existing clusters use **availableClusterVersions**.
    :type cluster_code_version: str
    :ivar cluster_endpoint: The Azure Resource Provider endpoint. A system
     service in the cluster connects to this  endpoint.
    :vartype cluster_endpoint: str
    :ivar cluster_id: A service generated unique identifier for the cluster
     resource.
    :vartype cluster_id: str
    :ivar cluster_state: The current state of the cluster.
     - WaitingForNodes - Indicates that the cluster resource is created and the
     resource provider is waiting for Service Fabric VM extension to boot up
     and report to it.
     - Deploying - Indicates that the Service Fabric runtime is being installed
     on the VMs. Cluster resource will be in this state until the cluster boots
     up and system services are up.
     - BaselineUpgrade - Indicates that the cluster is upgrading to establishes
     the cluster version. This upgrade is automatically initiated when the
     cluster boots up for the first time.
     - UpdatingUserConfiguration - Indicates that the cluster is being upgraded
     with the user provided configuration.
     - UpdatingUserCertificate - Indicates that the cluster is being upgraded
     with the user provided certificate.
     - UpdatingInfrastructure - Indicates that the cluster is being upgraded
     with the latest Service Fabric runtime version. This happens only when the
     **upgradeMode** is set to 'Automatic'.
     - EnforcingClusterVersion - Indicates that cluster is on a different
     version than expected and the cluster is being upgraded to the expected
     version.
     - UpgradeServiceUnreachable - Indicates that the system service in the
     cluster is no longer polling the Resource Provider. Clusters in this state
     cannot be managed by the Resource Provider.
     - AutoScale - Indicates that the ReliabilityLevel of the cluster is being
     adjusted.
     - Ready - Indicates that the cluster is in a stable state.
     . Possible values include: 'WaitingForNodes', 'Deploying',
     'BaselineUpgrade', 'UpdatingUserConfiguration', 'UpdatingUserCertificate',
     'UpdatingInfrastructure', 'EnforcingClusterVersion',
     'UpgradeServiceUnreachable', 'AutoScale', 'Ready'
    :vartype cluster_state: str or ~azure.mgmt.servicefabric.models.enum
    :param diagnostics_storage_account_config: The storage account information
     for storing Service Fabric diagnostic logs.
    :type diagnostics_storage_account_config:
     ~azure.mgmt.servicefabric.models.DiagnosticsStorageAccountConfig
    :param event_store_service_enabled: Indicates if the event store service
     is enabled.
    :type event_store_service_enabled: bool
    :param fabric_settings: The list of custom fabric settings to configure
     the cluster.
    :type fabric_settings:
     list[~azure.mgmt.servicefabric.models.SettingsSectionDescription]
    :param management_endpoint: Required. The http management endpoint of the
     cluster.
    :type management_endpoint: str
    :param node_types: Required. The list of node types in the cluster.
    :type node_types:
     list[~azure.mgmt.servicefabric.models.NodeTypeDescription]
    :ivar provisioning_state: The provisioning state of the cluster resource.
     Possible values include: 'Updating', 'Succeeded', 'Failed', 'Canceled'
    :vartype provisioning_state: str or
     ~azure.mgmt.servicefabric.models.ProvisioningState
    :param reliability_level: The reliability level sets the replica set size
     of system services. Learn about
     [ReliabilityLevel](https://docs.microsoft.com/en-us/azure/service-fabric/service-fabric-cluster-capacity).
     - None - Run the System services with a target replica set count of 1.
     This should only be used for test clusters.
     - Bronze - Run the System services with a target replica set count of 3.
     This should only be used for test clusters.
     - Silver - Run the System services with a target replica set count of 5.
     - Gold - Run the System services with a target replica set count of 7.
     - Platinum - Run the System services with a target replica set count of 9.
     . Possible values include: 'None', 'Bronze', 'Silver', 'Gold', 'Platinum'
    :type reliability_level: str or ~azure.mgmt.servicefabric.models.enum
    :param reverse_proxy_certificate: The server certificate used by reverse
     proxy.
    :type reverse_proxy_certificate:
     ~azure.mgmt.servicefabric.models.CertificateDescription
    :param reverse_proxy_certificate_common_names: Describes a list of server
     certificates referenced by common name that are used to secure the
     cluster.
    :type reverse_proxy_certificate_common_names:
     ~azure.mgmt.servicefabric.models.ServerCertificateCommonNames
    :param upgrade_description: The policy to use when upgrading the cluster.
    :type upgrade_description:
     ~azure.mgmt.servicefabric.models.ClusterUpgradePolicy
    :param upgrade_mode: The upgrade mode of the cluster when new Service
     Fabric runtime version is available.
     - Automatic - The cluster will be automatically upgraded to the latest
     Service Fabric runtime version as soon as it is available.
     - Manual - The cluster will not be automatically upgraded to the latest
     Service Fabric runtime version. The cluster is upgraded by setting the
     **clusterCodeVersion** property in the cluster resource.
     . Possible values include: 'Automatic', 'Manual'
    :type upgrade_mode: str or ~azure.mgmt.servicefabric.models.enum
    :param vm_image: The VM image VMSS has been configured with. Generic names
     such as Windows or Linux can be used.
    :type vm_image: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'etag': {'readonly': True},
        'available_cluster_versions': {'readonly': True},
        'cluster_endpoint': {'readonly': True},
        'cluster_id': {'readonly': True},
        'cluster_state': {'readonly': True},
        'management_endpoint': {'required': True},
        'node_types': {'required': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'etag': {'key': 'etag', 'type': 'str'},
        'add_on_features': {'key': 'properties.addOnFeatures', 'type': '[str]'},
        'available_cluster_versions': {'key': 'properties.availableClusterVersions', 'type': '[ClusterVersionDetails]'},
        'azure_active_directory': {'key': 'properties.azureActiveDirectory', 'type': 'AzureActiveDirectory'},
        'certificate': {'key': 'properties.certificate', 'type': 'CertificateDescription'},
        'certificate_common_names': {'key': 'properties.certificateCommonNames', 'type': 'ServerCertificateCommonNames'},
        'client_certificate_common_names': {'key': 'properties.clientCertificateCommonNames', 'type': '[ClientCertificateCommonName]'},
        'client_certificate_thumbprints': {'key': 'properties.clientCertificateThumbprints', 'type': '[ClientCertificateThumbprint]'},
        'cluster_code_version': {'key': 'properties.clusterCodeVersion', 'type': 'str'},
        'cluster_endpoint': {'key': 'properties.clusterEndpoint', 'type': 'str'},
        'cluster_id': {'key': 'properties.clusterId', 'type': 'str'},
        'cluster_state': {'key': 'properties.clusterState', 'type': 'str'},
        'diagnostics_storage_account_config': {'key': 'properties.diagnosticsStorageAccountConfig', 'type': 'DiagnosticsStorageAccountConfig'},
        'event_store_service_enabled': {'key': 'properties.eventStoreServiceEnabled', 'type': 'bool'},
        'fabric_settings': {'key': 'properties.fabricSettings', 'type': '[SettingsSectionDescription]'},
        'management_endpoint': {'key': 'properties.managementEndpoint', 'type': 'str'},
        'node_types': {'key': 'properties.nodeTypes', 'type': '[NodeTypeDescription]'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'reliability_level': {'key': 'properties.reliabilityLevel', 'type': 'str'},
        'reverse_proxy_certificate': {'key': 'properties.reverseProxyCertificate', 'type': 'CertificateDescription'},
        'reverse_proxy_certificate_common_names': {'key': 'properties.reverseProxyCertificateCommonNames', 'type': 'ServerCertificateCommonNames'},
        'upgrade_description': {'key': 'properties.upgradeDescription', 'type': 'ClusterUpgradePolicy'},
        'upgrade_mode': {'key': 'properties.upgradeMode', 'type': 'str'},
        'vm_image': {'key': 'properties.vmImage', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Cluster, self).__init__(**kwargs)
        self.add_on_features = kwargs.get('add_on_features', None)
        self.available_cluster_versions = None
        self.azure_active_directory = kwargs.get('azure_active_directory', None)
        self.certificate = kwargs.get('certificate', None)
        self.certificate_common_names = kwargs.get('certificate_common_names', None)
        self.client_certificate_common_names = kwargs.get('client_certificate_common_names', None)
        self.client_certificate_thumbprints = kwargs.get('client_certificate_thumbprints', None)
        self.cluster_code_version = kwargs.get('cluster_code_version', None)
        self.cluster_endpoint = None
        self.cluster_id = None
        self.cluster_state = None
        self.diagnostics_storage_account_config = kwargs.get('diagnostics_storage_account_config', None)
        self.event_store_service_enabled = kwargs.get('event_store_service_enabled', None)
        self.fabric_settings = kwargs.get('fabric_settings', None)
        self.management_endpoint = kwargs.get('management_endpoint', None)
        self.node_types = kwargs.get('node_types', None)
        self.provisioning_state = None
        self.reliability_level = kwargs.get('reliability_level', None)
        self.reverse_proxy_certificate = kwargs.get('reverse_proxy_certificate', None)
        self.reverse_proxy_certificate_common_names = kwargs.get('reverse_proxy_certificate_common_names', None)
        self.upgrade_description = kwargs.get('upgrade_description', None)
        self.upgrade_mode = kwargs.get('upgrade_mode', None)
        self.vm_image = kwargs.get('vm_image', None)
