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

import copy
import os

import botocore.session
from botocore.client import Config
from botocore.exceptions import (
    DataNotFoundError,
    NoCredentialsError,
    UnknownServiceError,
)

import boto3
import boto3.utils
from boto3.exceptions import ResourceNotExistsError, UnknownAPIVersionError

from .resources.factory import ResourceFactory


class Session:
    """
    A session stores configuration state and allows you to create service
    clients and resources.

    :type aws_access_key_id: string
    :param aws_access_key_id: AWS access key ID
    :type aws_secret_access_key: string
    :param aws_secret_access_key: AWS secret access key
    :type aws_session_token: string
    :param aws_session_token: AWS temporary session token
    :type region_name: string
    :param region_name: Default region when creating new connections
    :type botocore_session: botocore.session.Session
    :param botocore_session: Use this Botocore session instead of creating
                             a new default one.
    :type profile_name: string
    :param profile_name: The name of a profile to use. If not given, then
                         the default profile is used.
    :type aws_account_id: string
    :param aws_account_id: AWS account ID
    """

    def __init__(
        self,
        aws_access_key_id=None,
        aws_secret_access_key=None,
        aws_session_token=None,
        region_name=None,
        botocore_session=None,
        profile_name=None,
        aws_account_id=None,
    ):
        pass

    def __repr__(self):
        pass

    @property
    def profile_name(self):
        """
        The **read-only** profile name.
        """
        pass

    @property
    def region_name(self):
        """
        The **read-only** region name.
        """
        pass

    @property
    def events(self):
        """
        The event emitter for a session
        """
        pass

    @property
    def available_profiles(self):
        """
        The profiles available to the session credentials
        """
        pass

    def _setup_loader(self):
        """
        Setup loader paths so that we can load resources.
        """
        pass

    def get_available_services(self):
        """
        Get a list of available services that can be loaded as low-level
        clients via :py:meth:`Session.client`.

        :rtype: list
        :return: List of service names
        """
        pass

    def get_available_resources(self):
        """
        Get a list of available services that can be loaded as resource
        clients via :py:meth:`Session.resource`.

        :rtype: list
        :return: List of service names
        """
        pass

    def get_available_partitions(self):
        """Lists the available partitions

        :rtype: list
        :return: Returns a list of partition names (e.g., ["aws", "aws-cn"])
        """
        pass

    def get_available_regions(
        self, service_name, partition_name='aws', allow_non_regional=False
    ):
        """Lists the region and endpoint names of a particular partition.

        The list of regions returned by this method are regions that are
        explicitly known by the client to exist and is not comprehensive. A
        region not returned in this list may still be available for the
        provided service.

        :type service_name: string
        :param service_name: Name of a service to list endpoint for (e.g., s3).

        :type partition_name: string
        :param partition_name: Name of the partition to limit endpoints to.
            (e.g., aws for the public AWS endpoints, aws-cn for AWS China
            endpoints, aws-us-gov for AWS GovCloud (US) Endpoints, etc.)

        :type allow_non_regional: bool
        :param allow_non_regional: Set to True to include endpoints that are
             not regional endpoints (e.g., s3-external-1,
             fips-us-gov-west-1, etc).

        :return: Returns a list of endpoint names (e.g., ["us-east-1"]).
        """
        pass

    def get_credentials(self):
        """
        Return the :class:`botocore.credentials.Credentials` object
        associated with this session.  If the credentials have not
        yet been loaded, this will attempt to load them.  If they
        have already been loaded, this will return the cached
        credentials.
        """
        pass

    def get_partition_for_region(self, region_name):
        """Lists the partition name of a particular region.

        :type region_name: string
        :param region_name: Name of the region to list partition for (e.g.,
             us-east-1).

        :rtype: string
        :return: Returns the respective partition name (e.g., aws).
        """
        pass

    def client(
        self,
        service_name,
        region_name=None,
        api_version=None,
        use_ssl=True,
        verify=None,
        endpoint_url=None,
        aws_access_key_id=None,
        aws_secret_access_key=None,
        aws_session_token=None,
        config=None,
        aws_account_id=None,
    ):
        """
        Create a low-level service client by name.

        :type service_name: string
        :param service_name: The name of a service, e.g. 's3' or 'ec2'. You
            can get a list of available services via
            :py:meth:`get_available_services`.

        :type region_name: string
        :param region_name: The name of the region associated with the client.
            A client is associated with a single region.

        :type api_version: string
        :param api_version: The API version to use.  By default, botocore will
            use the latest API version when creating a client.  You only need
            to specify this parameter if you want to use a previous API version
            of the client.

        :type use_ssl: boolean
        :param use_ssl: Whether or not to use SSL.  By default, SSL is used.
            Note that not all services support non-ssl connections.

        :type verify: boolean/string
        :param verify: Whether or not to verify SSL certificates.  By default
            SSL certificates are verified.  You can provide the following
            values:

            * False - do not validate SSL certificates.  SSL will still be
              used (unless use_ssl is False), but SSL certificates
              will not be verified.
            * path/to/cert/bundle.pem - A filename of the CA cert bundle to
              uses.  You can specify this argument if you want to use a
              different CA cert bundle than the one used by botocore.

        :type endpoint_url: string
        :param endpoint_url: The complete URL to use for the constructed
            client. Normally, botocore will automatically construct the
            appropriate URL to use when communicating with a service.  You
            can specify a complete URL (including the "http/https" scheme)
            to override this behavior.  If this value is provided,
            then ``use_ssl`` is ignored.

        :type aws_access_key_id: string
        :param aws_access_key_id: The access key to use when creating
            the client.  This is entirely optional, and if not provided,
            the credentials configured for the session will automatically
            be used.  You only need to provide this argument if you want
            to override the credentials used for this specific client.

        :type aws_secret_access_key: string
        :param aws_secret_access_key: The secret key to use when creating
            the client.  Same semantics as aws_access_key_id above.

        :type aws_session_token: string
        :param aws_session_token: The session token to use when creating
            the client.  Same semantics as aws_access_key_id above.

        :type config: botocore.client.Config
        :param config: Advanced client configuration options. If region_name
            is specified in the client config, its value will take precedence
            over environment variables and configuration values, but not over
            a region_name value passed explicitly to the method. See
            `botocore config documentation
            <https://docs.aws.amazon.com/botocore/latest/reference/config.html>`_
            for more details.

        :type aws_account_id: string
        :param aws_account_id: The account id to use when creating
            the client.  Same semantics as aws_access_key_id above.

        :return: Service client instance

        """
        pass

    def resource(
        self,
        service_name,
        region_name=None,
        api_version=None,
        use_ssl=True,
        verify=None,
        endpoint_url=None,
        aws_access_key_id=None,
        aws_secret_access_key=None,
        aws_session_token=None,
        config=None,
    ):
        """
        Create a resource service client by name.

        :type service_name: string
        :param service_name: The name of a service, e.g. 's3' or 'ec2'. You
            can get a list of available services via
            :py:meth:`get_available_resources`.

        :type region_name: string
        :param region_name: The name of the region associated with the client.
            A client is associated with a single region.

        :type api_version: string
        :param api_version: The API version to use.  By default, botocore will
            use the latest API version when creating a client.  You only need
            to specify this parameter if you want to use a previous API version
            of the client.

        :type use_ssl: boolean
        :param use_ssl: Whether or not to use SSL.  By default, SSL is used.
            Note that not all services support non-ssl connections.

        :type verify: boolean/string
        :param verify: Whether or not to verify SSL certificates.  By default
            SSL certificates are verified.  You can provide the following
            values:

            * False - do not validate SSL certificates.  SSL will still be
              used (unless use_ssl is False), but SSL certificates
              will not be verified.
            * path/to/cert/bundle.pem - A filename of the CA cert bundle to
              uses.  You can specify this argument if you want to use a
              different CA cert bundle than the one used by botocore.

        :type endpoint_url: string
        :param endpoint_url: The complete URL to use for the constructed
            client. Normally, botocore will automatically construct the
            appropriate URL to use when communicating with a service.  You
            can specify a complete URL (including the "http/https" scheme)
            to override this behavior.  If this value is provided,
            then ``use_ssl`` is ignored.

        :type aws_access_key_id: string
        :param aws_access_key_id: The access key to use when creating
            the client.  This is entirely optional, and if not provided,
            the credentials configured for the session will automatically
            be used.  You only need to provide this argument if you want
            to override the credentials used for this specific client.

        :type aws_secret_access_key: string
        :param aws_secret_access_key: The secret key to use when creating
            the client.  Same semantics as aws_access_key_id above.

        :type aws_session_token: string
        :param aws_session_token: The session token to use when creating
            the client.  Same semantics as aws_access_key_id above.

        :type config: botocore.client.Config
        :param config: Advanced client configuration options. If region_name
            is specified in the client config, its value will take precedence
            over environment variables and configuration values, but not over
            a region_name value passed explicitly to the method.  If
            user_agent_extra is specified in the client config, it overrides
            the default user_agent_extra provided by the resource API. See
            `botocore config documentation
            <https://docs.aws.amazon.com/botocore/latest/reference/config.html>`_
            for more details.

        :return: Subclass of :py:class:`~boto3.resources.base.ServiceResource`
        """
        pass

    def _register_default_handlers(self):
        # S3 customizations
        pass

    def _account_id_set_without_credentials(
        self,
        *,
        aws_account_id,
        aws_access_key_id,
        aws_secret_access_key,
        **kwargs,
    ):
        pass
