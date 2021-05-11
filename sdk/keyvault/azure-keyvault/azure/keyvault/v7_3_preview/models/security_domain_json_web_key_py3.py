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


class SecurityDomainJsonWebKey(Model):
    """SecurityDomainJsonWebKey.

    All required parameters must be populated in order to send to Azure.

    :param kid: Required. Key identifier.
    :type kid: str
    :param kty: Required. JsonWebKey Key Type (kty), as defined in
     https://tools.ietf.org/html/draft-ietf-jose-json-web-algorithms-40. For
     Security Domain this value must be RSA.
    :type kty: str
    :param key_ops: Required.
    :type key_ops: list[str]
    :param n: Required. RSA modulus.
    :type n: str
    :param e: Required. RSA public exponent.
    :type e: str
    :param x5c: Required. X509 certificate chain parameter
    :type x5c: list[str]
    :param use: Public Key Use Parameter. This is optional and if present must
     be enc.
    :type use: str
    :param x5t: X509 certificate SHA1 thumbprint. This is optional.
    :type x5t: str
    :param x5t_s256: Required. X509 certificate SHA256 thumbprint.
    :type x5t_s256: str
    :param alg: Required. Algorithm intended for use with the key.
    :type alg: str
    """

    _validation = {
        'kid': {'required': True},
        'kty': {'required': True},
        'key_ops': {'required': True},
        'n': {'required': True},
        'e': {'required': True},
        'x5c': {'required': True},
        'x5t_s256': {'required': True},
        'alg': {'required': True},
    }

    _attribute_map = {
        'kid': {'key': 'kid', 'type': 'str'},
        'kty': {'key': 'kty', 'type': 'str'},
        'key_ops': {'key': 'key_ops', 'type': '[str]'},
        'n': {'key': 'n', 'type': 'str'},
        'e': {'key': 'e', 'type': 'str'},
        'x5c': {'key': 'x5c', 'type': '[str]'},
        'use': {'key': 'use', 'type': 'str'},
        'x5t': {'key': 'x5t', 'type': 'str'},
        'x5t_s256': {'key': 'x5t#S256', 'type': 'str'},
        'alg': {'key': 'alg', 'type': 'str'},
    }

    def __init__(self, *, kid: str, kty: str, key_ops, n: str, e: str, x5c, x5t_s256: str, alg: str, use: str=None, x5t: str=None, **kwargs) -> None:
        super(SecurityDomainJsonWebKey, self).__init__(**kwargs)
        self.kid = kid
        self.kty = kty
        self.key_ops = key_ops
        self.n = n
        self.e = e
        self.x5c = x5c
        self.use = use
        self.x5t = x5t
        self.x5t_s256 = x5t_s256
        self.alg = alg