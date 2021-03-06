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

from .resource_py3 import Resource


class UsageDetail(Resource):
    """An usage detail resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar billing_account_id: Billing Account identifier.
    :vartype billing_account_id: str
    :ivar billing_account_name: Billing Account Name.
    :vartype billing_account_name: str
    :ivar billing_period_start_date: The billing period start date.
    :vartype billing_period_start_date: datetime
    :ivar billing_period_end_date: The billing period end date.
    :vartype billing_period_end_date: datetime
    :ivar billing_profile_id: Billing Profile identifier.
    :vartype billing_profile_id: str
    :ivar billing_profile_name: Billing Profile Name.
    :vartype billing_profile_name: str
    :ivar account_owner_id: Account Owner Id.
    :vartype account_owner_id: str
    :ivar account_name: Account Name.
    :vartype account_name: str
    :ivar subscription_id: Subscription guid.
    :vartype subscription_id: str
    :ivar subscription_name: Subscription name.
    :vartype subscription_name: str
    :ivar date_property: Date for the usage record.
    :vartype date_property: datetime
    :ivar product: Product name for the consumed service or purchase. Not
     available for Marketplace.
    :vartype product: str
    :ivar part_number: Part Number of the service used. Can be used to join
     with the price sheet. Not available for marketplace.
    :vartype part_number: str
    :ivar meter_id: The meter id (GUID). Not available for marketplace. For
     reserved instance this represents the primary meter for which the
     reservation was purchased. For the actual VM Size for which the
     reservation is purchased see productOrderName.
    :vartype meter_id: str
    :ivar meter_details: The details about the meter. By default this is not
     populated, unless it's specified in $expand.
    :vartype meter_details:
     ~azure.mgmt.consumption.models.MeterDetailsResponse
    :ivar quantity: The usage quantity.
    :vartype quantity: decimal.Decimal
    :ivar effective_price: Effective Price that???s charged for the usage.
    :vartype effective_price: decimal.Decimal
    :ivar cost: The amount of cost before tax.
    :vartype cost: decimal.Decimal
    :ivar unit_price: Unit Price is the price applicable to you. (your EA or
     other contract price).
    :vartype unit_price: decimal.Decimal
    :ivar billing_currency: Billing Currency.
    :vartype billing_currency: str
    :ivar resource_location: Resource Location.
    :vartype resource_location: str
    :ivar consumed_service: Consumed service name. Name of the azure resource
     provider that emits the usage or was purchased. This value is not provided
     for marketplace usage.
    :vartype consumed_service: str
    :ivar resource_id: Azure resource manager resource identifier.
    :vartype resource_id: str
    :ivar resource_name: Resource Name.
    :vartype resource_name: str
    :ivar service_info1: Service Info 1.
    :vartype service_info1: str
    :ivar service_info2: Service Info 2.
    :vartype service_info2: str
    :ivar additional_info: Additional details of this usage item. By default
     this is not populated, unless it's specified in $expand. Use this field to
     get usage line item specific details such as the actual VM Size
     (ServiceType) or the ratio in which the reservation discount is applied.
    :vartype additional_info: str
    :ivar invoice_section: Invoice Section Name.
    :vartype invoice_section: str
    :ivar cost_center: The cost center of this department if it is a
     department and a cost center is provided.
    :vartype cost_center: str
    :ivar resource_group: Resource Group Name.
    :vartype resource_group: str
    :ivar reservation_id: ARM resource id of the reservation. Only applies to
     records relevant to reservations.
    :vartype reservation_id: str
    :ivar reservation_name: User provided display name of the reservation.
     Last known name for a particular day is populated in the daily data. Only
     applies to records relevant to reservations.
    :vartype reservation_name: str
    :ivar product_order_id: Product Order Id. For reservations this is the
     Reservation Order ID.
    :vartype product_order_id: str
    :ivar product_order_name: Product Order Name. For reservations this is the
     SKU that was purchased.
    :vartype product_order_name: str
    :ivar offer_id: Offer Id. Ex: MS-AZR-0017P, MS-AZR-0148P.
    :vartype offer_id: str
    :ivar is_azure_credit_eligible: Is Azure Credit Eligible.
    :vartype is_azure_credit_eligible: bool
    :ivar term: Term (in months). 1 month for monthly recurring purchase. 12
     months for a 1 year reservation. 36 months for a 3 year reservation.
    :vartype term: str
    :ivar publisher_name: Publisher Name.
    :vartype publisher_name: str
    :ivar publisher_type: Publisher Type.
    :vartype publisher_type: str
    :ivar plan_name: Plan Name.
    :vartype plan_name: str
    :ivar charge_type: Indicates a charge represents credits, usage, a
     Marketplace purchase, a reservation fee, or a refund.
    :vartype charge_type: str
    :ivar frequency: Indicates how frequently this charge will occur. OneTime
     for purchases which only happen once, Monthly for fees which recur every
     month, and UsageBased for charges based on how much a service is used.
    :vartype frequency: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'tags': {'readonly': True},
        'billing_account_id': {'readonly': True},
        'billing_account_name': {'readonly': True},
        'billing_period_start_date': {'readonly': True},
        'billing_period_end_date': {'readonly': True},
        'billing_profile_id': {'readonly': True},
        'billing_profile_name': {'readonly': True},
        'account_owner_id': {'readonly': True},
        'account_name': {'readonly': True},
        'subscription_id': {'readonly': True},
        'subscription_name': {'readonly': True},
        'date_property': {'readonly': True},
        'product': {'readonly': True},
        'part_number': {'readonly': True},
        'meter_id': {'readonly': True},
        'meter_details': {'readonly': True},
        'quantity': {'readonly': True},
        'effective_price': {'readonly': True},
        'cost': {'readonly': True},
        'unit_price': {'readonly': True},
        'billing_currency': {'readonly': True},
        'resource_location': {'readonly': True},
        'consumed_service': {'readonly': True},
        'resource_id': {'readonly': True},
        'resource_name': {'readonly': True},
        'service_info1': {'readonly': True},
        'service_info2': {'readonly': True},
        'additional_info': {'readonly': True},
        'invoice_section': {'readonly': True},
        'cost_center': {'readonly': True},
        'resource_group': {'readonly': True},
        'reservation_id': {'readonly': True},
        'reservation_name': {'readonly': True},
        'product_order_id': {'readonly': True},
        'product_order_name': {'readonly': True},
        'offer_id': {'readonly': True},
        'is_azure_credit_eligible': {'readonly': True},
        'term': {'readonly': True},
        'publisher_name': {'readonly': True},
        'publisher_type': {'readonly': True},
        'plan_name': {'readonly': True},
        'charge_type': {'readonly': True},
        'frequency': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'billing_account_id': {'key': 'properties.billingAccountId', 'type': 'str'},
        'billing_account_name': {'key': 'properties.billingAccountName', 'type': 'str'},
        'billing_period_start_date': {'key': 'properties.billingPeriodStartDate', 'type': 'iso-8601'},
        'billing_period_end_date': {'key': 'properties.billingPeriodEndDate', 'type': 'iso-8601'},
        'billing_profile_id': {'key': 'properties.billingProfileId', 'type': 'str'},
        'billing_profile_name': {'key': 'properties.billingProfileName', 'type': 'str'},
        'account_owner_id': {'key': 'properties.accountOwnerId', 'type': 'str'},
        'account_name': {'key': 'properties.accountName', 'type': 'str'},
        'subscription_id': {'key': 'properties.subscriptionId', 'type': 'str'},
        'subscription_name': {'key': 'properties.subscriptionName', 'type': 'str'},
        'date_property': {'key': 'properties.date', 'type': 'iso-8601'},
        'product': {'key': 'properties.product', 'type': 'str'},
        'part_number': {'key': 'properties.partNumber', 'type': 'str'},
        'meter_id': {'key': 'properties.meterId', 'type': 'str'},
        'meter_details': {'key': 'properties.meterDetails', 'type': 'MeterDetailsResponse'},
        'quantity': {'key': 'properties.quantity', 'type': 'decimal'},
        'effective_price': {'key': 'properties.effectivePrice', 'type': 'decimal'},
        'cost': {'key': 'properties.cost', 'type': 'decimal'},
        'unit_price': {'key': 'properties.unitPrice', 'type': 'decimal'},
        'billing_currency': {'key': 'properties.billingCurrency', 'type': 'str'},
        'resource_location': {'key': 'properties.resourceLocation', 'type': 'str'},
        'consumed_service': {'key': 'properties.consumedService', 'type': 'str'},
        'resource_id': {'key': 'properties.resourceId', 'type': 'str'},
        'resource_name': {'key': 'properties.resourceName', 'type': 'str'},
        'service_info1': {'key': 'properties.serviceInfo1', 'type': 'str'},
        'service_info2': {'key': 'properties.serviceInfo2', 'type': 'str'},
        'additional_info': {'key': 'properties.additionalInfo', 'type': 'str'},
        'invoice_section': {'key': 'properties.invoiceSection', 'type': 'str'},
        'cost_center': {'key': 'properties.costCenter', 'type': 'str'},
        'resource_group': {'key': 'properties.resourceGroup', 'type': 'str'},
        'reservation_id': {'key': 'properties.reservationId', 'type': 'str'},
        'reservation_name': {'key': 'properties.reservationName', 'type': 'str'},
        'product_order_id': {'key': 'properties.productOrderId', 'type': 'str'},
        'product_order_name': {'key': 'properties.productOrderName', 'type': 'str'},
        'offer_id': {'key': 'properties.offerId', 'type': 'str'},
        'is_azure_credit_eligible': {'key': 'properties.isAzureCreditEligible', 'type': 'bool'},
        'term': {'key': 'properties.term', 'type': 'str'},
        'publisher_name': {'key': 'properties.publisherName', 'type': 'str'},
        'publisher_type': {'key': 'properties.publisherType', 'type': 'str'},
        'plan_name': {'key': 'properties.planName', 'type': 'str'},
        'charge_type': {'key': 'properties.chargeType', 'type': 'str'},
        'frequency': {'key': 'properties.frequency', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(UsageDetail, self).__init__(**kwargs)
        self.billing_account_id = None
        self.billing_account_name = None
        self.billing_period_start_date = None
        self.billing_period_end_date = None
        self.billing_profile_id = None
        self.billing_profile_name = None
        self.account_owner_id = None
        self.account_name = None
        self.subscription_id = None
        self.subscription_name = None
        self.date_property = None
        self.product = None
        self.part_number = None
        self.meter_id = None
        self.meter_details = None
        self.quantity = None
        self.effective_price = None
        self.cost = None
        self.unit_price = None
        self.billing_currency = None
        self.resource_location = None
        self.consumed_service = None
        self.resource_id = None
        self.resource_name = None
        self.service_info1 = None
        self.service_info2 = None
        self.additional_info = None
        self.invoice_section = None
        self.cost_center = None
        self.resource_group = None
        self.reservation_id = None
        self.reservation_name = None
        self.product_order_id = None
        self.product_order_name = None
        self.offer_id = None
        self.is_azure_credit_eligible = None
        self.term = None
        self.publisher_name = None
        self.publisher_type = None
        self.plan_name = None
        self.charge_type = None
        self.frequency = None
