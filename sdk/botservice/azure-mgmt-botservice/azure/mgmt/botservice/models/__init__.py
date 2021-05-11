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

try:
    from .sku_py3 import Sku
    from .resource_py3 import Resource
    from .bot_properties_py3 import BotProperties
    from .bot_py3 import Bot
    from .channel_py3 import Channel
    from .bot_channel_py3 import BotChannel
    from .facebook_page_py3 import FacebookPage
    from .facebook_channel_properties_py3 import FacebookChannelProperties
    from .facebook_channel_py3 import FacebookChannel
    from .email_channel_properties_py3 import EmailChannelProperties
    from .email_channel_py3 import EmailChannel
    from .ms_teams_channel_properties_py3 import MsTeamsChannelProperties
    from .ms_teams_channel_py3 import MsTeamsChannel
    from .skype_channel_properties_py3 import SkypeChannelProperties
    from .skype_channel_py3 import SkypeChannel
    from .kik_channel_properties_py3 import KikChannelProperties
    from .kik_channel_py3 import KikChannel
    from .web_chat_site_py3 import WebChatSite
    from .web_chat_channel_properties_py3 import WebChatChannelProperties
    from .web_chat_channel_py3 import WebChatChannel
    from .direct_line_site_py3 import DirectLineSite
    from .direct_line_channel_properties_py3 import DirectLineChannelProperties
    from .direct_line_channel_py3 import DirectLineChannel
    from .telegram_channel_properties_py3 import TelegramChannelProperties
    from .telegram_channel_py3 import TelegramChannel
    from .sms_channel_properties_py3 import SmsChannelProperties
    from .sms_channel_py3 import SmsChannel
    from .slack_channel_properties_py3 import SlackChannelProperties
    from .slack_channel_py3 import SlackChannel
    from .connection_item_name_py3 import ConnectionItemName
    from .connection_setting_parameter_py3 import ConnectionSettingParameter
    from .connection_setting_properties_py3 import ConnectionSettingProperties
    from .connection_setting_py3 import ConnectionSetting
    from .service_provider_parameter_py3 import ServiceProviderParameter
    from .service_provider_properties_py3 import ServiceProviderProperties
    from .service_provider_py3 import ServiceProvider
    from .service_provider_response_list_py3 import ServiceProviderResponseList
    from .error_body_py3 import ErrorBody
    from .error_py3 import Error, ErrorException
    from .operation_display_info_py3 import OperationDisplayInfo
    from .operation_entity_py3 import OperationEntity
    from .check_name_availability_request_body_py3 import CheckNameAvailabilityRequestBody
    from .check_name_availability_response_body_py3 import CheckNameAvailabilityResponseBody
    from .enterprise_channel_check_name_availability_request_py3 import EnterpriseChannelCheckNameAvailabilityRequest
    from .enterprise_channel_check_name_availability_response_py3 import EnterpriseChannelCheckNameAvailabilityResponse
    from .enterprise_channel_node_py3 import EnterpriseChannelNode
    from .enterprise_channel_properties_py3 import EnterpriseChannelProperties
    from .enterprise_channel_py3 import EnterpriseChannel
except (SyntaxError, ImportError):
    from .sku import Sku
    from .resource import Resource
    from .bot_properties import BotProperties
    from .bot import Bot
    from .channel import Channel
    from .bot_channel import BotChannel
    from .facebook_page import FacebookPage
    from .facebook_channel_properties import FacebookChannelProperties
    from .facebook_channel import FacebookChannel
    from .email_channel_properties import EmailChannelProperties
    from .email_channel import EmailChannel
    from .ms_teams_channel_properties import MsTeamsChannelProperties
    from .ms_teams_channel import MsTeamsChannel
    from .skype_channel_properties import SkypeChannelProperties
    from .skype_channel import SkypeChannel
    from .kik_channel_properties import KikChannelProperties
    from .kik_channel import KikChannel
    from .web_chat_site import WebChatSite
    from .web_chat_channel_properties import WebChatChannelProperties
    from .web_chat_channel import WebChatChannel
    from .direct_line_site import DirectLineSite
    from .direct_line_channel_properties import DirectLineChannelProperties
    from .direct_line_channel import DirectLineChannel
    from .telegram_channel_properties import TelegramChannelProperties
    from .telegram_channel import TelegramChannel
    from .sms_channel_properties import SmsChannelProperties
    from .sms_channel import SmsChannel
    from .slack_channel_properties import SlackChannelProperties
    from .slack_channel import SlackChannel
    from .connection_item_name import ConnectionItemName
    from .connection_setting_parameter import ConnectionSettingParameter
    from .connection_setting_properties import ConnectionSettingProperties
    from .connection_setting import ConnectionSetting
    from .service_provider_parameter import ServiceProviderParameter
    from .service_provider_properties import ServiceProviderProperties
    from .service_provider import ServiceProvider
    from .service_provider_response_list import ServiceProviderResponseList
    from .error_body import ErrorBody
    from .error import Error, ErrorException
    from .operation_display_info import OperationDisplayInfo
    from .operation_entity import OperationEntity
    from .check_name_availability_request_body import CheckNameAvailabilityRequestBody
    from .check_name_availability_response_body import CheckNameAvailabilityResponseBody
    from .enterprise_channel_check_name_availability_request import EnterpriseChannelCheckNameAvailabilityRequest
    from .enterprise_channel_check_name_availability_response import EnterpriseChannelCheckNameAvailabilityResponse
    from .enterprise_channel_node import EnterpriseChannelNode
    from .enterprise_channel_properties import EnterpriseChannelProperties
    from .enterprise_channel import EnterpriseChannel
from .bot_paged import BotPaged
from .bot_channel_paged import BotChannelPaged
from .operation_entity_paged import OperationEntityPaged
from .connection_setting_paged import ConnectionSettingPaged
from .enterprise_channel_paged import EnterpriseChannelPaged
from .azure_bot_service_enums import (
    SkuName,
    SkuTier,
    Kind,
    EnterpriseChannelState,
    EnterpriseChannelNodeState,
    ChannelName,
)

__all__ = [
    'Sku',
    'Resource',
    'BotProperties',
    'Bot',
    'Channel',
    'BotChannel',
    'FacebookPage',
    'FacebookChannelProperties',
    'FacebookChannel',
    'EmailChannelProperties',
    'EmailChannel',
    'MsTeamsChannelProperties',
    'MsTeamsChannel',
    'SkypeChannelProperties',
    'SkypeChannel',
    'KikChannelProperties',
    'KikChannel',
    'WebChatSite',
    'WebChatChannelProperties',
    'WebChatChannel',
    'DirectLineSite',
    'DirectLineChannelProperties',
    'DirectLineChannel',
    'TelegramChannelProperties',
    'TelegramChannel',
    'SmsChannelProperties',
    'SmsChannel',
    'SlackChannelProperties',
    'SlackChannel',
    'ConnectionItemName',
    'ConnectionSettingParameter',
    'ConnectionSettingProperties',
    'ConnectionSetting',
    'ServiceProviderParameter',
    'ServiceProviderProperties',
    'ServiceProvider',
    'ServiceProviderResponseList',
    'ErrorBody',
    'Error', 'ErrorException',
    'OperationDisplayInfo',
    'OperationEntity',
    'CheckNameAvailabilityRequestBody',
    'CheckNameAvailabilityResponseBody',
    'EnterpriseChannelCheckNameAvailabilityRequest',
    'EnterpriseChannelCheckNameAvailabilityResponse',
    'EnterpriseChannelNode',
    'EnterpriseChannelProperties',
    'EnterpriseChannel',
    'BotPaged',
    'BotChannelPaged',
    'OperationEntityPaged',
    'ConnectionSettingPaged',
    'EnterpriseChannelPaged',
    'SkuName',
    'SkuTier',
    'Kind',
    'EnterpriseChannelState',
    'EnterpriseChannelNodeState',
    'ChannelName',
]
