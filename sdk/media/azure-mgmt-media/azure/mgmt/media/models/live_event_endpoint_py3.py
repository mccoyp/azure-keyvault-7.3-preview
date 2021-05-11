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


class LiveEventEndpoint(Model):
    """The Live Event endpoint.

    :param protocol: The endpoint protocol.
    :type protocol: str
    :param url: The endpoint URL.
    :type url: str
    """

    _attribute_map = {
        'protocol': {'key': 'protocol', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
    }

    def __init__(self, *, protocol: str=None, url: str=None, **kwargs) -> None:
        super(LiveEventEndpoint, self).__init__(**kwargs)
        self.protocol = protocol
        self.url = url
