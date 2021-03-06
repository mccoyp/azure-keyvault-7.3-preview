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


class PricingList(Model):
    """List of pricing configurations response.

    All required parameters must be populated in order to send to Azure.

    :param value: Required. List of pricing configurations
    :type value: list[~azure.mgmt.security.models.Pricing]
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Pricing]'},
    }

    def __init__(self, *, value, **kwargs) -> None:
        super(PricingList, self).__init__(**kwargs)
        self.value = value
