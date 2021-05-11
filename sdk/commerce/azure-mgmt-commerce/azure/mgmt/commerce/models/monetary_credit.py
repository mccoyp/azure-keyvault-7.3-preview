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

from .offer_term_info import OfferTermInfo


class MonetaryCredit(OfferTermInfo):
    """Indicates that this is a monetary credit offer.

    :param effective_date: Indicates the date from which the offer term is
     effective.
    :type effective_date: datetime
    :param name: Constant filled by server.
    :type name: str
    :param credit: The amount of credit provided under the terms of the given
     offer level.
    :type credit: decimal.Decimal
    :param excluded_meter_ids: An array of meter ids that are excluded from
     the given offer terms.
    :type excluded_meter_ids: list[str]
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'effective_date': {'key': 'EffectiveDate', 'type': 'iso-8601'},
        'name': {'key': 'Name', 'type': 'str'},
        'credit': {'key': 'Credit', 'type': 'decimal'},
        'excluded_meter_ids': {'key': 'ExcludedMeterIds', 'type': '[str]'},
    }

    def __init__(self, effective_date=None, credit=None, excluded_meter_ids=None):
        super(MonetaryCredit, self).__init__(effective_date=effective_date)
        self.credit = credit
        self.excluded_meter_ids = excluded_meter_ids
        self.name = 'Monetary Credit'
