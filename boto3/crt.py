# Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# https://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
"""
This file contains private functionality for interacting with the AWS
Common Runtime library (awscrt) in boto3.

All code contained within this file is for internal usage within this
project and is not intended for external consumption. All interfaces
contained within are subject to abrupt breaking changes.
"""

import logging
import threading

import botocore.exceptions
from botocore.session import Session
from s3transfer.crt import (
    BotocoreCRTCredentialsWrapper,
    BotocoreCRTRequestSerializer,
    CRTTransferManager,
    acquire_crt_s3_process_lock,
    create_s3_crt_client,
)

from boto3.compat import TRANSFER_CONFIG_SUPPORTS_CRT
from boto3.exceptions import InvalidCrtTransferConfigError
from boto3.s3.constants import CRT_TRANSFER_CLIENT

logger = logging.getLogger(__name__)

# Singletons for CRT-backed transfers
CRT_S3_CLIENT = None
BOTOCORE_CRT_SERIALIZER = None

CLIENT_CREATION_LOCK = threading.Lock()
PROCESS_LOCK_NAME = 'boto3'


_ALLOWED_CRT_TRANSFER_CONFIG_OPTIONS = {
    'multipart_threshold',
    'max_concurrency',
    'max_request_concurrency',
    'multipart_chunksize',
    'preferred_transfer_client',
}


def _create_crt_client(session, config, region_name, cred_provider):
    """Create a CRT S3 Client for file transfer.

    Instantiating many of these may lead to degraded performance or
    system resource exhaustion.
    """
    pass


def _create_crt_request_serializer(session, region_name):
    pass


def _create_crt_s3_client(
    session, config, region_name, credentials, lock, **kwargs
):
    """Create boto3 wrapper class to manage crt lock reference and S3 client."""
    pass


def _initialize_crt_transfer_primatives(client, config):
    pass


def get_crt_s3_client(client, config):
    pass


class CRTS3Client:
    """
    This wrapper keeps track of our underlying CRT client, the lock used to
    acquire it and the region we've used to instantiate the client.

    Due to limitations in the existing CRT interfaces, we can only make calls
    in a single region and does not support redirects. We track the region to
    ensure we don't use the CRT client when a successful request cannot be made.
    """

    def __init__(self, crt_client, process_lock, region, cred_provider):
        self.crt_client = crt_client
        self.process_lock = process_lock
        self.region = region
        self.cred_provider = cred_provider


def is_crt_compatible_request(client, crt_s3_client):
    """
    Boto3 client must use same signing region and credentials
    as the CRT_S3_CLIENT singleton. Otherwise fallback to classic.
    """
    pass


def compare_identity(boto3_creds, crt_s3_creds):
    pass


def _validate_crt_transfer_config(config):
    pass


def create_crt_transfer_manager(client, config):
    """Create a CRTTransferManager for optimized data transfer."""
    pass
