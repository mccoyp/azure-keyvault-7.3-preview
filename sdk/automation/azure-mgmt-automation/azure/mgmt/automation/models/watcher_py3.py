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

from .tracked_resource_py3 import TrackedResource


class Watcher(TrackedResource):
    """Definition of the watcher type.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: The Azure Region where the resource lives
    :type location: str
    :param execution_frequency_in_seconds: Gets or sets the frequency at which
     the watcher is invoked.
    :type execution_frequency_in_seconds: long
    :param script_name: Gets or sets the name of the script the watcher is
     attached to, i.e. the name of an existing runbook.
    :type script_name: str
    :param script_parameters: Gets or sets the parameters of the script.
    :type script_parameters: dict[str, str]
    :param script_run_on: Gets or sets the name of the hybrid worker group the
     watcher will run on.
    :type script_run_on: str
    :ivar status: Gets the current status of the watcher.
    :vartype status: str
    :ivar creation_time: Gets or sets the creation time.
    :vartype creation_time: datetime
    :ivar last_modified_time: Gets or sets the last modified time.
    :vartype last_modified_time: datetime
    :ivar last_modified_by: Details of the user who last modified the watcher.
    :vartype last_modified_by: str
    :param description: Gets or sets the description.
    :type description: str
    :param etag: Gets or sets the etag of the resource.
    :type etag: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'status': {'readonly': True},
        'creation_time': {'readonly': True},
        'last_modified_time': {'readonly': True},
        'last_modified_by': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'execution_frequency_in_seconds': {'key': 'properties.executionFrequencyInSeconds', 'type': 'long'},
        'script_name': {'key': 'properties.scriptName', 'type': 'str'},
        'script_parameters': {'key': 'properties.scriptParameters', 'type': '{str}'},
        'script_run_on': {'key': 'properties.scriptRunOn', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'creation_time': {'key': 'properties.creationTime', 'type': 'iso-8601'},
        'last_modified_time': {'key': 'properties.lastModifiedTime', 'type': 'iso-8601'},
        'last_modified_by': {'key': 'properties.lastModifiedBy', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, *, tags=None, location: str=None, execution_frequency_in_seconds: int=None, script_name: str=None, script_parameters=None, script_run_on: str=None, description: str=None, etag: str=None, **kwargs) -> None:
        super(Watcher, self).__init__(tags=tags, location=location, **kwargs)
        self.execution_frequency_in_seconds = execution_frequency_in_seconds
        self.script_name = script_name
        self.script_parameters = script_parameters
        self.script_run_on = script_run_on
        self.status = None
        self.creation_time = None
        self.last_modified_time = None
        self.last_modified_by = None
        self.description = description
        self.etag = etag
