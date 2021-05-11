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
from msrest.exceptions import HttpOperationError


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class DataSource(Model):
    """Data source object contains configuration to collect telemetry and one or
    more sinks to send that telemetry data to.

    All required parameters must be populated in order to send to Azure.

    :param kind: Required. Datasource kind. Possible values include:
     'PerformanceCounter', 'ETWProviders', 'WindowsEventLogs'
    :type kind: str or ~azure.mgmt.monitor.v2018_06_01_preview.models.enum
    :param configuration: Required.
    :type configuration:
     ~azure.mgmt.monitor.v2018_06_01_preview.models.DataSourceConfiguration
    :param sinks: Required.
    :type sinks:
     list[~azure.mgmt.monitor.v2018_06_01_preview.models.SinkConfiguration]
    """

    _validation = {
        'kind': {'required': True},
        'configuration': {'required': True},
        'sinks': {'required': True},
    }

    _attribute_map = {
        'kind': {'key': 'kind', 'type': 'str'},
        'configuration': {'key': 'configuration', 'type': 'DataSourceConfiguration'},
        'sinks': {'key': 'sinks', 'type': '[SinkConfiguration]'},
    }

    def __init__(self, *, kind, configuration, sinks, **kwargs) -> None:
        super(DataSource, self).__init__(**kwargs)
        self.kind = kind
        self.configuration = configuration
        self.sinks = sinks


class DataSourceConfiguration(Model):
    """DataSourceConfiguration.

    :param providers: ETW providers configuration
    :type providers:
     list[~azure.mgmt.monitor.v2018_06_01_preview.models.EtwProviderConfiguration]
    :param perf_counters: Performance counter configuration
    :type perf_counters:
     list[~azure.mgmt.monitor.v2018_06_01_preview.models.PerformanceCounterConfiguration]
    :param event_logs: Windows event logs configuration.
    :type event_logs:
     list[~azure.mgmt.monitor.v2018_06_01_preview.models.EventLogConfiguration]
    """

    _attribute_map = {
        'providers': {'key': 'providers', 'type': '[EtwProviderConfiguration]'},
        'perf_counters': {'key': 'perfCounters', 'type': '[PerformanceCounterConfiguration]'},
        'event_logs': {'key': 'eventLogs', 'type': '[EventLogConfiguration]'},
    }

    def __init__(self, *, providers=None, perf_counters=None, event_logs=None, **kwargs) -> None:
        super(DataSourceConfiguration, self).__init__(**kwargs)
        self.providers = providers
        self.perf_counters = perf_counters
        self.event_logs = event_logs


class ErrorResponse(Model):
    """Describes the format of Error response.

    :param code: Error code
    :type code: str
    :param message: Error message indicating why the operation failed.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, *, code: str=None, message: str=None, **kwargs) -> None:
        super(ErrorResponse, self).__init__(**kwargs)
        self.code = code
        self.message = message


class ErrorResponseException(HttpOperationError):
    """Server responsed with exception of type: 'ErrorResponse'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorResponseException, self).__init__(deserialize, response, 'ErrorResponse', *args)


class EtwEventConfiguration(Model):
    """EtwEventConfiguration.

    All required parameters must be populated in order to send to Azure.

    :param name: Required.
    :type name: str
    :param id: Required.
    :type id: int
    :param filter:
    :type filter: str
    """

    _validation = {
        'name': {'required': True},
        'id': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'filter': {'key': 'filter', 'type': 'str'},
    }

    def __init__(self, *, name: str, id: int, filter: str=None, **kwargs) -> None:
        super(EtwEventConfiguration, self).__init__(**kwargs)
        self.name = name
        self.id = id
        self.filter = filter


class EtwProviderConfiguration(Model):
    """EtwProviderConfiguration.

    All required parameters must be populated in order to send to Azure.

    :param id: Required.
    :type id: str
    :param events: Required.
    :type events:
     list[~azure.mgmt.monitor.v2018_06_01_preview.models.EtwEventConfiguration]
    """

    _validation = {
        'id': {'required': True},
        'events': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'events': {'key': 'events', 'type': '[EtwEventConfiguration]'},
    }

    def __init__(self, *, id: str, events, **kwargs) -> None:
        super(EtwProviderConfiguration, self).__init__(**kwargs)
        self.id = id
        self.events = events


class EventLogConfiguration(Model):
    """EventLogConfiguration.

    All required parameters must be populated in order to send to Azure.

    :param log_name: Required.
    :type log_name: str
    :param filter:
    :type filter: str
    """

    _validation = {
        'log_name': {'required': True},
    }

    _attribute_map = {
        'log_name': {'key': 'logName', 'type': 'str'},
        'filter': {'key': 'filter', 'type': 'str'},
    }

    def __init__(self, *, log_name: str, filter: str=None, **kwargs) -> None:
        super(EventLogConfiguration, self).__init__(**kwargs)
        self.log_name = log_name
        self.filter = filter


class Resource(Model):
    """An azure resource object.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar name: Azure resource name
    :vartype name: str
    :ivar type: Azure resource type
    :vartype type: str
    :param location: Required. Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, *, location: str, tags=None, **kwargs) -> None:
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = location
        self.tags = tags


class GuestDiagnosticSettingsAssociationResource(Resource):
    """Virtual machine guest diagnostic settings resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar name: Azure resource name
    :vartype name: str
    :ivar type: Azure resource type
    :vartype type: str
    :param location: Required. Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param guest_diagnostic_settings_name: Required. The guest diagnostic
     settings name.
    :type guest_diagnostic_settings_name: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'guest_diagnostic_settings_name': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'guest_diagnostic_settings_name': {'key': 'properties.guestDiagnosticSettingsName', 'type': 'str'},
    }

    def __init__(self, *, location: str, guest_diagnostic_settings_name: str, tags=None, **kwargs) -> None:
        super(GuestDiagnosticSettingsAssociationResource, self).__init__(location=location, tags=tags, **kwargs)
        self.guest_diagnostic_settings_name = guest_diagnostic_settings_name


class GuestDiagnosticSettingsAssociationResourcePatch(Model):
    """Guest diagnostic setting resource for patch operations.

    All required parameters must be populated in order to send to Azure.

    :param tags: Resource tags
    :type tags: dict[str, str]
    :param guest_diagnostic_settings_name: Required. The guest diagnostic
     settings name.
    :type guest_diagnostic_settings_name: str
    """

    _validation = {
        'guest_diagnostic_settings_name': {'required': True},
    }

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'guest_diagnostic_settings_name': {'key': 'properties.guestDiagnosticSettingsName', 'type': 'str'},
    }

    def __init__(self, *, guest_diagnostic_settings_name: str, tags=None, **kwargs) -> None:
        super(GuestDiagnosticSettingsAssociationResourcePatch, self).__init__(**kwargs)
        self.tags = tags
        self.guest_diagnostic_settings_name = guest_diagnostic_settings_name


class GuestDiagnosticSettingsPatchResource(Model):
    """An diagnostic settings object for the body of patch operations.

    :param tags: Resource tags
    :type tags: dict[str, str]
    :param os_type: Operating system type for the configuration. Possible
     values include: 'Windows', 'Linux'
    :type os_type: str or ~azure.mgmt.monitor.v2018_06_01_preview.models.enum
    :param data_sources: the array of data source object which are configured
     to collect and send data
    :type data_sources:
     list[~azure.mgmt.monitor.v2018_06_01_preview.models.DataSource]
    :param proxy_setting:
    :type proxy_setting: str
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'os_type': {'key': 'properties.osType', 'type': 'str'},
        'data_sources': {'key': 'properties.dataSources', 'type': '[DataSource]'},
        'proxy_setting': {'key': 'properties.proxySetting', 'type': 'str'},
    }

    def __init__(self, *, tags=None, os_type=None, data_sources=None, proxy_setting: str=None, **kwargs) -> None:
        super(GuestDiagnosticSettingsPatchResource, self).__init__(**kwargs)
        self.tags = tags
        self.os_type = os_type
        self.data_sources = data_sources
        self.proxy_setting = proxy_setting


class GuestDiagnosticSettingsResource(Resource):
    """Virtual machine guest diagnostics settings resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar name: Azure resource name
    :vartype name: str
    :ivar type: Azure resource type
    :vartype type: str
    :param location: Required. Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param os_type: Operating system type for the configuration. Possible
     values include: 'Windows', 'Linux'
    :type os_type: str or ~azure.mgmt.monitor.v2018_06_01_preview.models.enum
    :param data_sources: the array of data source object which are configured
     to collect and send data
    :type data_sources:
     list[~azure.mgmt.monitor.v2018_06_01_preview.models.DataSource]
    :param proxy_setting:
    :type proxy_setting: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'os_type': {'key': 'properties.osType', 'type': 'str'},
        'data_sources': {'key': 'properties.dataSources', 'type': '[DataSource]'},
        'proxy_setting': {'key': 'properties.proxySetting', 'type': 'str'},
    }

    def __init__(self, *, location: str, tags=None, os_type=None, data_sources=None, proxy_setting: str=None, **kwargs) -> None:
        super(GuestDiagnosticSettingsResource, self).__init__(location=location, tags=tags, **kwargs)
        self.os_type = os_type
        self.data_sources = data_sources
        self.proxy_setting = proxy_setting


class PerformanceCounterConfiguration(Model):
    """PerformanceCounterConfiguration.

    All required parameters must be populated in order to send to Azure.

    :param name: Required.
    :type name: str
    :param sampling_period: Required.
    :type sampling_period: str
    :param instance:
    :type instance: str
    """

    _validation = {
        'name': {'required': True},
        'sampling_period': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'sampling_period': {'key': 'samplingPeriod', 'type': 'str'},
        'instance': {'key': 'instance', 'type': 'str'},
    }

    def __init__(self, *, name: str, sampling_period: str, instance: str=None, **kwargs) -> None:
        super(PerformanceCounterConfiguration, self).__init__(**kwargs)
        self.name = name
        self.sampling_period = sampling_period
        self.instance = instance


class SinkConfiguration(Model):
    """SinkConfiguration.

    All required parameters must be populated in order to send to Azure.

    :param kind: Required. Possible values include: 'EventHub',
     'ApplicationInsights', 'LogAnalytics'
    :type kind: str or ~azure.mgmt.monitor.v2018_06_01_preview.models.enum
    """

    _validation = {
        'kind': {'required': True},
    }

    _attribute_map = {
        'kind': {'key': 'kind', 'type': 'str'},
    }

    def __init__(self, *, kind, **kwargs) -> None:
        super(SinkConfiguration, self).__init__(**kwargs)
        self.kind = kind
