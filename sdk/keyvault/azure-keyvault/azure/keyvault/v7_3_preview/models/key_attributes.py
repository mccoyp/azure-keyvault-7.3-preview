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

from .attributes import Attributes


class KeyAttributes(Attributes):
    """The attributes of a key managed by the key vault service.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param enabled: Determines whether the object is enabled.
    :type enabled: bool
    :param not_before: Not before date in UTC.
    :type not_before: datetime
    :param expires: Expiry date in UTC.
    :type expires: datetime
    :ivar created: Creation time in UTC.
    :vartype created: datetime
    :ivar updated: Last updated time in UTC.
    :vartype updated: datetime
    :ivar recoverable_days: softDelete data retention days. Value should be
     >=7 and <=90 when softDelete enabled, otherwise 0.
    :vartype recoverable_days: int
    :ivar recovery_level: Reflects the deletion recovery level currently in
     effect for keys in the current vault. If it contains 'Purgeable' the key
     can be permanently deleted by a privileged user; otherwise, only the
     system can purge the key, at the end of the retention interval. Possible
     values include: 'Purgeable', 'Recoverable+Purgeable', 'Recoverable',
     'Recoverable+ProtectedSubscription', 'CustomizedRecoverable+Purgeable',
     'CustomizedRecoverable', 'CustomizedRecoverable+ProtectedSubscription'
    :vartype recovery_level: str or ~keys.models.DeletionRecoveryLevel
    :param exportable: Indicates if the private key can be exported.
    :type exportable: bool
    """

    _validation = {
        'created': {'readonly': True},
        'updated': {'readonly': True},
        'recoverable_days': {'readonly': True},
        'recovery_level': {'readonly': True},
    }

    _attribute_map = {
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'not_before': {'key': 'nbf', 'type': 'unix-time'},
        'expires': {'key': 'exp', 'type': 'unix-time'},
        'created': {'key': 'created', 'type': 'unix-time'},
        'updated': {'key': 'updated', 'type': 'unix-time'},
        'recoverable_days': {'key': 'recoverableDays', 'type': 'int'},
        'recovery_level': {'key': 'recoveryLevel', 'type': 'str'},
        'exportable': {'key': 'exportable', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(KeyAttributes, self).__init__(**kwargs)
        self.recoverable_days = None
        self.recovery_level = None
        self.exportable = kwargs.get('exportable', None)