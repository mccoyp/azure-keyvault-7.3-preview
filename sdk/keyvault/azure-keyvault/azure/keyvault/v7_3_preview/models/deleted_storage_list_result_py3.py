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


class DeletedStorageListResult(Model):
    """The deleted storage account list result.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar value: A response message containing a list of the deleted storage
     accounts in the vault along with a link to the next page of deleted
     storage accounts
    :vartype value: list[~storage.models.DeletedStorageAccountItem]
    :ivar next_link: The URL to get the next set of deleted storage accounts.
    :vartype next_link: str
    """

    _validation = {
        'value': {'readonly': True},
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[DeletedStorageAccountItem]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(DeletedStorageListResult, self).__init__(**kwargs)
        self.value = None
        self.next_link = None
