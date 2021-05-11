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


class ReportRecordContract(Model):
    """Report data.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param name: Name depending on report endpoint specifies product, API,
     operation or developer name.
    :type name: str
    :param timestamp: Start of aggregation period. The date conforms to the
     following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601
     standard.
    :type timestamp: datetime
    :param interval: Length of aggregation period.  Interval must be multiple
     of 15 minutes and may not be zero. The value should be in ISO 8601 format
     (http://en.wikipedia.org/wiki/ISO_8601#Durations).
    :type interval: str
    :param country: Country to which this record data is related.
    :type country: str
    :param region: Country region to which this record data is related.
    :type region: str
    :param zip: Zip code to which this record data is related.
    :type zip: str
    :ivar user_id: User identifier path. /users/{userId}
    :vartype user_id: str
    :ivar product_id: Product identifier path. /products/{productId}
    :vartype product_id: str
    :param api_id: API identifier path. /apis/{apiId}
    :type api_id: str
    :param operation_id: Operation identifier path.
     /apis/{apiId}/operations/{operationId}
    :type operation_id: str
    :param api_region: API region identifier.
    :type api_region: str
    :param subscription_id: Subscription identifier path.
     /subscriptions/{subscriptionId}
    :type subscription_id: str
    :param call_count_success: Number of successful calls. This includes calls
     returning HttpStatusCode <= 301 and HttpStatusCode.NotModified and
     HttpStatusCode.TemporaryRedirect
    :type call_count_success: int
    :param call_count_blocked: Number of calls blocked due to invalid
     credentials. This includes calls returning HttpStatusCode.Unauthorized and
     HttpStatusCode.Forbidden and HttpStatusCode.TooManyRequests
    :type call_count_blocked: int
    :param call_count_failed: Number of calls failed due to proxy or backend
     errors. This includes calls returning HttpStatusCode.BadRequest(400) and
     any Code between HttpStatusCode.InternalServerError (500) and 600
    :type call_count_failed: int
    :param call_count_other: Number of other calls.
    :type call_count_other: int
    :param call_count_total: Total number of calls.
    :type call_count_total: int
    :param bandwidth: Bandwidth consumed.
    :type bandwidth: long
    :param cache_hit_count: Number of times when content was served from cache
     policy.
    :type cache_hit_count: int
    :param cache_miss_count: Number of times content was fetched from backend.
    :type cache_miss_count: int
    :param api_time_avg: Average time it took to process request.
    :type api_time_avg: float
    :param api_time_min: Minimum time it took to process request.
    :type api_time_min: float
    :param api_time_max: Maximum time it took to process request.
    :type api_time_max: float
    :param service_time_avg: Average time it took to process request on
     backend.
    :type service_time_avg: float
    :param service_time_min: Minimum time it took to process request on
     backend.
    :type service_time_min: float
    :param service_time_max: Maximum time it took to process request on
     backend.
    :type service_time_max: float
    """

    _validation = {
        'user_id': {'readonly': True},
        'product_id': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'timestamp': {'key': 'timestamp', 'type': 'iso-8601'},
        'interval': {'key': 'interval', 'type': 'str'},
        'country': {'key': 'country', 'type': 'str'},
        'region': {'key': 'region', 'type': 'str'},
        'zip': {'key': 'zip', 'type': 'str'},
        'user_id': {'key': 'userId', 'type': 'str'},
        'product_id': {'key': 'productId', 'type': 'str'},
        'api_id': {'key': 'apiId', 'type': 'str'},
        'operation_id': {'key': 'operationId', 'type': 'str'},
        'api_region': {'key': 'apiRegion', 'type': 'str'},
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'},
        'call_count_success': {'key': 'callCountSuccess', 'type': 'int'},
        'call_count_blocked': {'key': 'callCountBlocked', 'type': 'int'},
        'call_count_failed': {'key': 'callCountFailed', 'type': 'int'},
        'call_count_other': {'key': 'callCountOther', 'type': 'int'},
        'call_count_total': {'key': 'callCountTotal', 'type': 'int'},
        'bandwidth': {'key': 'bandwidth', 'type': 'long'},
        'cache_hit_count': {'key': 'cacheHitCount', 'type': 'int'},
        'cache_miss_count': {'key': 'cacheMissCount', 'type': 'int'},
        'api_time_avg': {'key': 'apiTimeAvg', 'type': 'float'},
        'api_time_min': {'key': 'apiTimeMin', 'type': 'float'},
        'api_time_max': {'key': 'apiTimeMax', 'type': 'float'},
        'service_time_avg': {'key': 'serviceTimeAvg', 'type': 'float'},
        'service_time_min': {'key': 'serviceTimeMin', 'type': 'float'},
        'service_time_max': {'key': 'serviceTimeMax', 'type': 'float'},
    }

    def __init__(self, **kwargs):
        super(ReportRecordContract, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.timestamp = kwargs.get('timestamp', None)
        self.interval = kwargs.get('interval', None)
        self.country = kwargs.get('country', None)
        self.region = kwargs.get('region', None)
        self.zip = kwargs.get('zip', None)
        self.user_id = None
        self.product_id = None
        self.api_id = kwargs.get('api_id', None)
        self.operation_id = kwargs.get('operation_id', None)
        self.api_region = kwargs.get('api_region', None)
        self.subscription_id = kwargs.get('subscription_id', None)
        self.call_count_success = kwargs.get('call_count_success', None)
        self.call_count_blocked = kwargs.get('call_count_blocked', None)
        self.call_count_failed = kwargs.get('call_count_failed', None)
        self.call_count_other = kwargs.get('call_count_other', None)
        self.call_count_total = kwargs.get('call_count_total', None)
        self.bandwidth = kwargs.get('bandwidth', None)
        self.cache_hit_count = kwargs.get('cache_hit_count', None)
        self.cache_miss_count = kwargs.get('cache_miss_count', None)
        self.api_time_avg = kwargs.get('api_time_avg', None)
        self.api_time_min = kwargs.get('api_time_min', None)
        self.api_time_max = kwargs.get('api_time_max', None)
        self.service_time_avg = kwargs.get('service_time_avg', None)
        self.service_time_min = kwargs.get('service_time_min', None)
        self.service_time_max = kwargs.get('service_time_max', None)
