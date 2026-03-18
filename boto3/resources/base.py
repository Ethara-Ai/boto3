# Copyright 2014 Amazon.com, Inc. or its affiliates. All Rights Reserved.
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

import logging

import boto3

logger = logging.getLogger(__name__)


class ResourceMeta:
    """
    An object containing metadata about a resource.
    """

    def __init__(
        self,
        service_name,
        identifiers=None,
        client=None,
        data=None,
        resource_model=None,
    ):
        #: (``string``) The service name, e.g. 's3'
        pass

    def __repr__(self):
        pass

    def __eq__(self, other):
        # Two metas are equal if their components are all equal
        pass

    def copy(self):
        """
        Create a copy of this metadata object.
        """
        pass


class ServiceResource:
    """
    A base class for resources.

    :type client: botocore.client
    :param client: A low-level Botocore client instance
    """

    meta = None
    """
    Stores metadata about this resource instance, such as the
    ``service_name``, the low-level ``client`` and any cached ``data``
    from when the instance was hydrated. For example::

        # Get a low-level client from a resource instance
        client = resource.meta.client
        response = client.operation(Param='foo')

        # Print the resource instance's service short name
        print(resource.meta.service_name)

    See :py:class:`ResourceMeta` for more information.
    """

    def __init__(self, *args, **kwargs):
        # Always work on a copy of meta, otherwise we would affect other
        # instances of the same subclass.
        pass

    def __repr__(self):
        pass

    def __eq__(self, other):
        # Should be instances of the same resource class
        pass

    def __hash__(self):
        pass
