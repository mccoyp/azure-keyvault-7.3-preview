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


class GremlinGraphCreateUpdateParameters(Model):
    """Parameters to create and update Cosmos DB Gremlin graph.

    All required parameters must be populated in order to send to Azure.

    :param resource: Required. The standard JSON format of a Gremlin graph
    :type resource: ~azure.mgmt.cosmosdb.models.GremlinGraphResource
    :param options: Required. A key-value pair of options to be applied for
     the request. This corresponds to the headers sent with the request.
    :type options: dict[str, str]
    """

    _validation = {
        'resource': {'required': True},
        'options': {'required': True},
    }

    _attribute_map = {
        'resource': {'key': 'properties.resource', 'type': 'GremlinGraphResource'},
        'options': {'key': 'properties.options', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(GremlinGraphCreateUpdateParameters, self).__init__(**kwargs)
        self.resource = kwargs.get('resource', None)
        self.options = kwargs.get('options', None)
