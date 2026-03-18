# Copyright 2015 Amazon.com, Inc. or its affiliates. All Rights Reserved.
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
import sys
import os
import errno
import socket
import warnings

from boto3.exceptions import PythonDeprecationWarning

from s3transfer.manager import TransferConfig

# In python3, socket.error is OSError, which is too general
# for what we want (i.e FileNotFoundError is a subclass of OSError).
# In py3 all the socket related errors are in a newly created
# ConnectionError
SOCKET_ERROR = ConnectionError

_APPEND_MODE_CHAR = 'a'

import collections.abc as collections_abc


TRANSFER_CONFIG_SUPPORTS_CRT = hasattr(TransferConfig, 'UNSET_DEFAULT')


if sys.platform.startswith('win'):
    def rename_file(current_filename, new_filename):
        pass
else:
    rename_file = os.rename


def filter_python_deprecation_warnings():
    """
    Invoking this filter acknowledges your runtime will soon be deprecated
    at which time you will stop receiving all updates to your client.
    """
    pass


def _warn_deprecated_python():
    """Use this template for future deprecation campaigns as needed."""
    pass


def is_append_mode(fileobj):
    pass
