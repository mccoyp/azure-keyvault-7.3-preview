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


class ClusterHealthPolicy(Model):
    """Defines a health policy used to evaluate the health of the cluster or of a
    cluster node.
    .

    :param max_percent_unhealthy_nodes: The maximum allowed percentage of
     unhealthy nodes before reporting an error. For example, to allow 10% of
     nodes to be unhealthy, this value would be 10.
     The percentage represents the maximum tolerated percentage of nodes that
     can be unhealthy before the cluster is considered in error.
     If the percentage is respected but there is at least one unhealthy node,
     the health is evaluated as Warning.
     The percentage is calculated by dividing the number of unhealthy nodes
     over the total number of nodes in the cluster.
     The computation rounds up to tolerate one failure on small numbers of
     nodes. Default percentage is zero.
     In large clusters, some nodes will always be down or out for repairs, so
     this percentage should be configured to tolerate that.
     . Default value: 0 .
    :type max_percent_unhealthy_nodes: int
    :param max_percent_unhealthy_applications: The maximum allowed percentage
     of unhealthy applications before reporting an error. For example, to allow
     10% of applications to be unhealthy, this value would be 10.
     The percentage represents the maximum tolerated percentage of applications
     that can be unhealthy before the cluster is considered in error.
     If the percentage is respected but there is at least one unhealthy
     application, the health is evaluated as Warning.
     This is calculated by dividing the number of unhealthy applications over
     the total number of application instances in the cluster, excluding
     applications of application types that are included in the
     ApplicationTypeHealthPolicyMap.
     The computation rounds up to tolerate one failure on small numbers of
     applications. Default percentage is zero.
     . Default value: 0 .
    :type max_percent_unhealthy_applications: int
    :param application_health_policies: Defines the application health policy
     map used to evaluate the health of an application or one of its children
     entities.
    :type application_health_policies: dict[str,
     ~azure.mgmt.servicefabric.models.ApplicationHealthPolicy]
    """

    _validation = {
        'max_percent_unhealthy_nodes': {'maximum': 100, 'minimum': 0},
        'max_percent_unhealthy_applications': {'maximum': 100, 'minimum': 0},
    }

    _attribute_map = {
        'max_percent_unhealthy_nodes': {'key': 'maxPercentUnhealthyNodes', 'type': 'int'},
        'max_percent_unhealthy_applications': {'key': 'maxPercentUnhealthyApplications', 'type': 'int'},
        'application_health_policies': {'key': 'applicationHealthPolicies', 'type': '{ApplicationHealthPolicy}'},
    }

    def __init__(self, *, max_percent_unhealthy_nodes: int=0, max_percent_unhealthy_applications: int=0, application_health_policies=None, **kwargs) -> None:
        super(ClusterHealthPolicy, self).__init__(**kwargs)
        self.max_percent_unhealthy_nodes = max_percent_unhealthy_nodes
        self.max_percent_unhealthy_applications = max_percent_unhealthy_applications
        self.application_health_policies = application_health_policies
