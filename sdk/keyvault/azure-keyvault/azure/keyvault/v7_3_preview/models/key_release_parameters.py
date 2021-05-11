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


class KeyReleaseParameters(Model):
    """The release key parameters.

    All required parameters must be populated in order to send to Azure.

    :param target: Required. The attestation assertion for the target of the
     key release.
    :type target: str
    :param nonce: A client provided nonce for freshness.
    :type nonce: str
    :param enc: The encryption algorithm to use to protected the exported key
     material. Possible values include: 'CKM_RSA_AES_KEY_WRAP',
     'RSA_AES_KEY_WRAP_256', 'RSA_AES_KEY_WRAP_384'
    :type enc: str or ~keys.models.KeyEncryptionAlgorithm
    """

    _validation = {
        'target': {'required': True, 'min_length': 1},
        'enc': {'min_length': 1},
    }

    _attribute_map = {
        'target': {'key': 'target', 'type': 'str'},
        'nonce': {'key': 'nonce', 'type': 'str'},
        'enc': {'key': 'enc', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(KeyReleaseParameters, self).__init__(**kwargs)
        self.target = kwargs.get('target', None)
        self.nonce = kwargs.get('nonce', None)
        self.enc = kwargs.get('enc', None)
