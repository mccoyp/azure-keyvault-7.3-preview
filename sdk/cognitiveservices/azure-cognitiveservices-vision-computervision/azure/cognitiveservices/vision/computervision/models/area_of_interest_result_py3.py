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


class AreaOfInterestResult(Model):
    """Result of AreaOfInterest operation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar area_of_interest: A bounding box for an area of interest inside an
     image.
    :vartype area_of_interest:
     ~azure.cognitiveservices.vision.computervision.models.BoundingRect
    :param request_id: Id of the REST API request.
    :type request_id: str
    :param metadata:
    :type metadata:
     ~azure.cognitiveservices.vision.computervision.models.ImageMetadata
    """

    _validation = {
        'area_of_interest': {'readonly': True},
    }

    _attribute_map = {
        'area_of_interest': {'key': 'areaOfInterest', 'type': 'BoundingRect'},
        'request_id': {'key': 'requestId', 'type': 'str'},
        'metadata': {'key': 'metadata', 'type': 'ImageMetadata'},
    }

    def __init__(self, *, request_id: str=None, metadata=None, **kwargs) -> None:
        super(AreaOfInterestResult, self).__init__(**kwargs)
        self.area_of_interest = None
        self.request_id = request_id
        self.metadata = metadata
