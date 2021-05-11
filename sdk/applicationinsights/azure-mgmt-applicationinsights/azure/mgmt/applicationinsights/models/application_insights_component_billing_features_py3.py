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


class ApplicationInsightsComponentBillingFeatures(Model):
    """An Application Insights component billing features.

    :param data_volume_cap: An Application Insights component daily data
     volume cap
    :type data_volume_cap:
     ~azure.mgmt.applicationinsights.models.ApplicationInsightsComponentDataVolumeCap
    :param current_billing_features: Current enabled pricing plan. When the
     component is in the Enterprise plan, this will list both 'Basic' and
     'Application Insights Enterprise'.
    :type current_billing_features: list[str]
    """

    _attribute_map = {
        'data_volume_cap': {'key': 'DataVolumeCap', 'type': 'ApplicationInsightsComponentDataVolumeCap'},
        'current_billing_features': {'key': 'CurrentBillingFeatures', 'type': '[str]'},
    }

    def __init__(self, *, data_volume_cap=None, current_billing_features=None, **kwargs) -> None:
        super(ApplicationInsightsComponentBillingFeatures, self).__init__(**kwargs)
        self.data_volume_cap = data_volume_cap
        self.current_billing_features = current_billing_features
