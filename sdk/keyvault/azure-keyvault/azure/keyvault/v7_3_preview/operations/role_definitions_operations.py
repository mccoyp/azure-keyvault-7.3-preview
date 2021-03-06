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

from msrest.pipeline import ClientRawResponse

from .. import models


class RoleDefinitionsOperations(object):
    """RoleDefinitionsOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: Client API version. Constant value: "7.3-preview".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config
        self.api_version = "7.3-preview"

    def delete(
            self, vault_base_url, scope, role_definition_name, custom_headers=None, raw=False, **operation_config):
        """Deletes a custom role definition.

        :param vault_base_url: The vault name, for example
         https://myvault.vault.azure.net.
        :type vault_base_url: str
        :param scope: The scope of the role definition to delete. Managed HSM
         only supports '/'.
        :type scope: str
        :param role_definition_name: The name (GUID) of the role definition to
         delete.
        :type role_definition_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: RoleDefinition or ClientRawResponse if raw=true
        :rtype: ~rbac.models.RoleDefinition or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`KeyVaultErrorException<rbac.models.KeyVaultErrorException>`
        """
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'vaultBaseUrl': self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
            'scope': self._serialize.url("scope", scope, 'str', skip_quote=True),
            'roleDefinitionName': self._serialize.url("role_definition_name", role_definition_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.KeyVaultErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('RoleDefinition', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    delete.metadata = {'url': '/{scope}/providers/Microsoft.Authorization/roleDefinitions/{roleDefinitionName}'}

    def create_or_update(
            self, vault_base_url, scope, role_definition_name, parameters, custom_headers=None, raw=False, **operation_config):
        """Creates or updates a custom role definition.

        :param vault_base_url: The vault name, for example
         https://myvault.vault.azure.net.
        :type vault_base_url: str
        :param scope: The scope of the role definition to create or update.
         Managed HSM only supports '/'.
        :type scope: str
        :param role_definition_name: The name of the role definition to create
         or update. It can be any valid GUID.
        :type role_definition_name: str
        :param parameters: Parameters for the role definition.
        :type parameters: ~rbac.models.RoleDefinitionCreateParameters
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: RoleDefinition or ClientRawResponse if raw=true
        :rtype: ~rbac.models.RoleDefinition or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`KeyVaultErrorException<rbac.models.KeyVaultErrorException>`
        """
        # Construct URL
        url = self.create_or_update.metadata['url']
        path_format_arguments = {
            'vaultBaseUrl': self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
            'scope': self._serialize.url("scope", scope, 'str', skip_quote=True),
            'roleDefinitionName': self._serialize.url("role_definition_name", role_definition_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(parameters, 'RoleDefinitionCreateParameters')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise models.KeyVaultErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 201:
            deserialized = self._deserialize('RoleDefinition', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_or_update.metadata = {'url': '/{scope}/providers/Microsoft.Authorization/roleDefinitions/{roleDefinitionName}'}

    def get(
            self, vault_base_url, scope, role_definition_name, custom_headers=None, raw=False, **operation_config):
        """Get the specified role definition.

        :param vault_base_url: The vault name, for example
         https://myvault.vault.azure.net.
        :type vault_base_url: str
        :param scope: The scope of the role definition to get. Managed HSM
         only supports '/'.
        :type scope: str
        :param role_definition_name: The name of the role definition to get.
        :type role_definition_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: RoleDefinition or ClientRawResponse if raw=true
        :rtype: ~rbac.models.RoleDefinition or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`KeyVaultErrorException<rbac.models.KeyVaultErrorException>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'vaultBaseUrl': self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
            'scope': self._serialize.url("scope", scope, 'str', skip_quote=True),
            'roleDefinitionName': self._serialize.url("role_definition_name", role_definition_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.KeyVaultErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('RoleDefinition', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/{scope}/providers/Microsoft.Authorization/roleDefinitions/{roleDefinitionName}'}

    def list(
            self, vault_base_url, scope, filter=None, custom_headers=None, raw=False, **operation_config):
        """Get all role definitions that are applicable at scope and above.

        :param vault_base_url: The vault name, for example
         https://myvault.vault.azure.net.
        :type vault_base_url: str
        :param scope: The scope of the role definition.
        :type scope: str
        :param filter: The filter to apply on the operation. Use
         atScopeAndBelow filter to search below the given scope as well.
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: RoleDefinitionListResult or ClientRawResponse if raw=true
        :rtype: ~rbac.models.RoleDefinitionListResult or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`KeyVaultErrorException<rbac.models.KeyVaultErrorException>`
        """
        # Construct URL
        url = self.list.metadata['url']
        path_format_arguments = {
            'vaultBaseUrl': self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
            'scope': self._serialize.url("scope", scope, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if filter is not None:
            query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.KeyVaultErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('RoleDefinitionListResult', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list.metadata = {'url': '/{scope}/providers/Microsoft.Authorization/roleDefinitions'}
