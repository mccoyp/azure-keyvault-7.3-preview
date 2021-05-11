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


class QueryDataset(Model):
    """The definition of data present in the query.

    :param granularity: The granularity of rows in the query. Possible values
     include: 'Daily', 'Hourly'
    :type granularity: str or
     ~azure.mgmt.costmanagement.models.GranularityType
    :param configuration: Has configuration information for the data in the
     export. The configuration will be ignored if aggregation and grouping are
     provided.
    :type configuration:
     ~azure.mgmt.costmanagement.models.QueryDatasetConfiguration
    :param aggregation: Dictionary of aggregation expression to use in the
     query. The key of each item in the dictionary is the alias for the
     aggregated column. Query can have up to 2 aggregation clauses.
    :type aggregation: dict[str,
     ~azure.mgmt.costmanagement.models.QueryAggregation]
    :param grouping: Array of group by expression to use in the query. Query
     can have up to 2 group by clauses.
    :type grouping: list[~azure.mgmt.costmanagement.models.QueryGrouping]
    :param sorting: Array of sorting by columns in query.
    :type sorting:
     list[~azure.mgmt.costmanagement.models.QuerySortingConfiguration]
    :param filter: Has filter expression to use in the query.
    :type filter: ~azure.mgmt.costmanagement.models.QueryFilter
    """

    _validation = {
        'grouping': {'max_items': 2},
    }

    _attribute_map = {
        'granularity': {'key': 'granularity', 'type': 'str'},
        'configuration': {'key': 'configuration', 'type': 'QueryDatasetConfiguration'},
        'aggregation': {'key': 'aggregation', 'type': '{QueryAggregation}'},
        'grouping': {'key': 'grouping', 'type': '[QueryGrouping]'},
        'sorting': {'key': 'sorting', 'type': '[QuerySortingConfiguration]'},
        'filter': {'key': 'filter', 'type': 'QueryFilter'},
    }

    def __init__(self, **kwargs):
        super(QueryDataset, self).__init__(**kwargs)
        self.granularity = kwargs.get('granularity', None)
        self.configuration = kwargs.get('configuration', None)
        self.aggregation = kwargs.get('aggregation', None)
        self.grouping = kwargs.get('grouping', None)
        self.sorting = kwargs.get('sorting', None)
        self.filter = kwargs.get('filter', None)
