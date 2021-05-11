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

from .certificate_bundle_py3 import CertificateBundle


class DeletedCertificateBundle(CertificateBundle):
    """A Deleted Certificate consisting of its previous id, attributes and its
    tags, as well as information on when it will be purged.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The certificate id.
    :vartype id: str
    :ivar kid: The key id.
    :vartype kid: str
    :ivar sid: The secret id.
    :vartype sid: str
    :ivar x509_thumbprint: Thumbprint of the certificate.
    :vartype x509_thumbprint: bytes
    :ivar policy: The management policy.
    :vartype policy: ~certificates.models.CertificatePolicy
    :param cer: CER contents of x509 certificate.
    :type cer: bytearray
    :param content_type: The content type of the secret. eg.
     'application/x-pem-file' or 'application/x-pkcs12',
    :type content_type: str
    :param attributes: The certificate attributes.
    :type attributes: ~certificates.models.CertificateAttributes
    :param tags: Application specific metadata in the form of key-value pairs
    :type tags: dict[str, str]
    :param recovery_id: The url of the recovery object, used to identify and
     recover the deleted certificate.
    :type recovery_id: str
    :ivar scheduled_purge_date: The time when the certificate is scheduled to
     be purged, in UTC
    :vartype scheduled_purge_date: datetime
    :ivar deleted_date: The time when the certificate was deleted, in UTC
    :vartype deleted_date: datetime
    """

    _validation = {
        'id': {'readonly': True},
        'kid': {'readonly': True},
        'sid': {'readonly': True},
        'x509_thumbprint': {'readonly': True},
        'policy': {'readonly': True},
        'scheduled_purge_date': {'readonly': True},
        'deleted_date': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'kid': {'key': 'kid', 'type': 'str'},
        'sid': {'key': 'sid', 'type': 'str'},
        'x509_thumbprint': {'key': 'x5t', 'type': 'base64'},
        'policy': {'key': 'policy', 'type': 'CertificatePolicy'},
        'cer': {'key': 'cer', 'type': 'bytearray'},
        'content_type': {'key': 'contentType', 'type': 'str'},
        'attributes': {'key': 'attributes', 'type': 'CertificateAttributes'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'recovery_id': {'key': 'recoveryId', 'type': 'str'},
        'scheduled_purge_date': {'key': 'scheduledPurgeDate', 'type': 'unix-time'},
        'deleted_date': {'key': 'deletedDate', 'type': 'unix-time'},
    }

    def __init__(self, *, cer: bytearray=None, content_type: str=None, attributes=None, tags=None, recovery_id: str=None, **kwargs) -> None:
        super(DeletedCertificateBundle, self).__init__(cer=cer, content_type=content_type, attributes=attributes, tags=tags, **kwargs)
        self.recovery_id = recovery_id
        self.scheduled_purge_date = None
        self.deleted_date = None
