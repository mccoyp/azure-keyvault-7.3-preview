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


class ClusterUpgradePolicy(Model):
    """Describes the policy used when upgrading the cluster.

    All required parameters must be populated in order to send to Azure.

    :param force_restart: If true, then processes are forcefully restarted
     during upgrade even when the code version has not changed (the upgrade
     only changes configuration or data).
    :type force_restart: bool
    :param upgrade_replica_set_check_timeout: Required. The maximum amount of
     time to block processing of an upgrade domain and prevent loss of
     availability when there are unexpected issues. When this timeout expires,
     processing of the upgrade domain will proceed regardless of availability
     loss issues. The timeout is reset at the start of each upgrade domain. The
     timeout can be in either hh:mm:ss or in d.hh:mm:ss.ms format.
    :type upgrade_replica_set_check_timeout: str
    :param health_check_wait_duration: Required. The length of time to wait
     after completing an upgrade domain before performing health checks. The
     duration can be in either hh:mm:ss or in d.hh:mm:ss.ms format.
    :type health_check_wait_duration: str
    :param health_check_stable_duration: Required. The amount of time that the
     application or cluster must remain healthy before the upgrade proceeds to
     the next upgrade domain. The duration can be in either hh:mm:ss or in
     d.hh:mm:ss.ms format.
    :type health_check_stable_duration: str
    :param health_check_retry_timeout: Required. The amount of time to retry
     health evaluation when the application or cluster is unhealthy before the
     upgrade rolls back. The timeout can be in either hh:mm:ss or in
     d.hh:mm:ss.ms format.
    :type health_check_retry_timeout: str
    :param upgrade_timeout: Required. The amount of time the overall upgrade
     has to complete before the upgrade rolls back. The timeout can be in
     either hh:mm:ss or in d.hh:mm:ss.ms format.
    :type upgrade_timeout: str
    :param upgrade_domain_timeout: Required. The amount of time each upgrade
     domain has to complete before the upgrade rolls back. The timeout can be
     in either hh:mm:ss or in d.hh:mm:ss.ms format.
    :type upgrade_domain_timeout: str
    :param health_policy: Required. The cluster health policy used when
     upgrading the cluster.
    :type health_policy: ~azure.mgmt.servicefabric.models.ClusterHealthPolicy
    :param delta_health_policy: The cluster delta health policy used when
     upgrading the cluster.
    :type delta_health_policy:
     ~azure.mgmt.servicefabric.models.ClusterUpgradeDeltaHealthPolicy
    """

    _validation = {
        'upgrade_replica_set_check_timeout': {'required': True},
        'health_check_wait_duration': {'required': True},
        'health_check_stable_duration': {'required': True},
        'health_check_retry_timeout': {'required': True},
        'upgrade_timeout': {'required': True},
        'upgrade_domain_timeout': {'required': True},
        'health_policy': {'required': True},
    }

    _attribute_map = {
        'force_restart': {'key': 'forceRestart', 'type': 'bool'},
        'upgrade_replica_set_check_timeout': {'key': 'upgradeReplicaSetCheckTimeout', 'type': 'str'},
        'health_check_wait_duration': {'key': 'healthCheckWaitDuration', 'type': 'str'},
        'health_check_stable_duration': {'key': 'healthCheckStableDuration', 'type': 'str'},
        'health_check_retry_timeout': {'key': 'healthCheckRetryTimeout', 'type': 'str'},
        'upgrade_timeout': {'key': 'upgradeTimeout', 'type': 'str'},
        'upgrade_domain_timeout': {'key': 'upgradeDomainTimeout', 'type': 'str'},
        'health_policy': {'key': 'healthPolicy', 'type': 'ClusterHealthPolicy'},
        'delta_health_policy': {'key': 'deltaHealthPolicy', 'type': 'ClusterUpgradeDeltaHealthPolicy'},
    }

    def __init__(self, *, upgrade_replica_set_check_timeout: str, health_check_wait_duration: str, health_check_stable_duration: str, health_check_retry_timeout: str, upgrade_timeout: str, upgrade_domain_timeout: str, health_policy, force_restart: bool=None, delta_health_policy=None, **kwargs) -> None:
        super(ClusterUpgradePolicy, self).__init__(**kwargs)
        self.force_restart = force_restart
        self.upgrade_replica_set_check_timeout = upgrade_replica_set_check_timeout
        self.health_check_wait_duration = health_check_wait_duration
        self.health_check_stable_duration = health_check_stable_duration
        self.health_check_retry_timeout = health_check_retry_timeout
        self.upgrade_timeout = upgrade_timeout
        self.upgrade_domain_timeout = upgrade_domain_timeout
        self.health_policy = health_policy
        self.delta_health_policy = delta_health_policy
