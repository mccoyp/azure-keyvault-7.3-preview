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


class DeletedKeyListResult(Model):
    """A list of keys that have been deleted in this vault.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar value: A response message containing a list of deleted keys in the
     vault along with a link to the next page of deleted keys
    :vartype value: list[~keys.models.DeletedKeyItem]
    :ivar next_link: The URL to get the next set of deleted keys.
    :vartype next_link: str
    """

    _validation = {
        'value': {'readonly': True},
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[DeletedKeyItem]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(DeletedKeyListResult, self).__init__(**kwargs)
        self.value = None
        self.next_link = None
