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

from .copy_source_py3 import CopySource


class CassandraSource(CopySource):
    """A copy activity source for a Cassandra database.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param source_retry_count: Source retry count. Type: integer (or
     Expression with resultType integer).
    :type source_retry_count: object
    :param source_retry_wait: Source retry wait. Type: string (or Expression
     with resultType string), pattern:
     ((\\d+)\\.)?(\\d\\d):(60|([0-5][0-9])):(60|([0-5][0-9])).
    :type source_retry_wait: object
    :param type: Required. Constant filled by server.
    :type type: str
    :param query: Database query. Should be a SQL-92 query expression or
     Cassandra Query Language (CQL) command. Type: string (or Expression with
     resultType string).
    :type query: object
    :param consistency_level: The consistency level specifies how many
     Cassandra servers must respond to a read request before returning data to
     the client application. Cassandra checks the specified number of Cassandra
     servers for data to satisfy the read request. Must be one of
     cassandraSourceReadConsistencyLevels. The default value is 'ONE'. It is
     case-insensitive. Possible values include: 'ALL', 'EACH_QUORUM', 'QUORUM',
     'LOCAL_QUORUM', 'ONE', 'TWO', 'THREE', 'LOCAL_ONE', 'SERIAL',
     'LOCAL_SERIAL'
    :type consistency_level: str or
     ~azure.mgmt.datafactory.models.CassandraSourceReadConsistencyLevels
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'source_retry_count': {'key': 'sourceRetryCount', 'type': 'object'},
        'source_retry_wait': {'key': 'sourceRetryWait', 'type': 'object'},
        'type': {'key': 'type', 'type': 'str'},
        'query': {'key': 'query', 'type': 'object'},
        'consistency_level': {'key': 'consistencyLevel', 'type': 'str'},
    }

    def __init__(self, *, additional_properties=None, source_retry_count=None, source_retry_wait=None, query=None, consistency_level=None, **kwargs) -> None:
        super(CassandraSource, self).__init__(additional_properties=additional_properties, source_retry_count=source_retry_count, source_retry_wait=source_retry_wait, **kwargs)
        self.query = query
        self.consistency_level = consistency_level
        self.type = 'CassandraSource'
