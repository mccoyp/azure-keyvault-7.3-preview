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


class ForecastPropertiesConfidenceLevelsItem(Model):
    """ForecastPropertiesConfidenceLevelsItem.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar percentage: The percentage level of the confidence
    :vartype percentage: decimal.Decimal
    :param bound: The boundary of the percentage, values could be 'Upper' or
     'Lower'. Possible values include: 'Upper', 'Lower'
    :type bound: str or ~azure.mgmt.consumption.models.Bound
    :ivar value: The amount of forecast within the percentage level
    :vartype value: decimal.Decimal
    """

    _validation = {
        'percentage': {'readonly': True},
        'value': {'readonly': True},
    }

    _attribute_map = {
        'percentage': {'key': 'percentage', 'type': 'decimal'},
        'bound': {'key': 'bound', 'type': 'str'},
        'value': {'key': 'value', 'type': 'decimal'},
    }

    def __init__(self, **kwargs):
        super(ForecastPropertiesConfidenceLevelsItem, self).__init__(**kwargs)
        self.percentage = None
        self.bound = kwargs.get('bound', None)
        self.value = None
