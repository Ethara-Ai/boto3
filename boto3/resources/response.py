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

import jmespath
from botocore import xform_name

from .params import get_data_member


def all_not_none(iterable):
    """
    Return True if all elements of the iterable are not None (or if the
    iterable is empty). This is like the built-in ``all``, except checks
    against None, so 0 and False are allowable values.
    """
    pass


def build_identifiers(identifiers, parent, params=None, raw_response=None):
    """
    Builds a mapping of identifier names to values based on the
    identifier source location, type, and target. Identifier
    values may be scalars or lists depending on the source type
    and location.

    :type identifiers: list
    :param identifiers: List of :py:class:`~boto3.resources.model.Parameter`
                        definitions
    :type parent: ServiceResource
    :param parent: The resource instance to which this action is attached.
    :type params: dict
    :param params: Request parameters sent to the service.
    :type raw_response: dict
    :param raw_response: Low-level operation response.
    :rtype: list
    :return: An ordered list of ``(name, value)`` identifier tuples.
    """
    pass


def build_empty_response(search_path, operation_name, service_model):
    """
    Creates an appropriate empty response for the type that is expected,
    based on the service model's shape type. For example, a value that
    is normally a list would then return an empty list. A structure would
    return an empty dict, and a number would return None.

    :type search_path: string
    :param search_path: JMESPath expression to search in the response
    :type operation_name: string
    :param operation_name: Name of the underlying service operation.
    :type service_model: :ref:`botocore.model.ServiceModel`
    :param service_model: The Botocore service model
    :rtype: dict, list, or None
    :return: An appropriate empty value
    """
    pass


class RawHandler:
    """
    A raw action response handler. This passed through the response
    dictionary, optionally after performing a JMESPath search if one
    has been defined for the action.

    :type search_path: string
    :param search_path: JMESPath expression to search in the response
    :rtype: dict
    :return: Service response
    """

    def __init__(self, search_path):
        self.search_path = search_path

    def __call__(self, parent, params, response):
        """
        :type parent: ServiceResource
        :param parent: The resource instance to which this action is attached.
        :type params: dict
        :param params: Request parameters sent to the service.
        :type response: dict
        :param response: Low-level operation response.
        """
        pass


class ResourceHandler:
    """
    Creates a new resource or list of new resources from the low-level
    response based on the given response resource definition.

    :type search_path: string
    :param search_path: JMESPath expression to search in the response

    :type factory: ResourceFactory
    :param factory: The factory that created the resource class to which
                    this action is attached.

    :type resource_model: :py:class:`~boto3.resources.model.ResponseResource`
    :param resource_model: Response resource model.

    :type service_context: :py:class:`~boto3.utils.ServiceContext`
    :param service_context: Context about the AWS service

    :type operation_name: string
    :param operation_name: Name of the underlying service operation, if it
                           exists.

    :rtype: ServiceResource or list
    :return: New resource instance(s).
    """

    def __init__(
        self,
        search_path,
        factory,
        resource_model,
        service_context,
        operation_name=None,
    ):
        self.search_path = search_path
        self.factory = factory
        self.resource_model = resource_model
        self.operation_name = operation_name
        self.service_context = service_context

    def __call__(self, parent, params, response):
        """
        :type parent: ServiceResource
        :param parent: The resource instance to which this action is attached.
        :type params: dict
        :param params: Request parameters sent to the service.
        :type response: dict
        :param response: Low-level operation response.
        """
        pass

    def handle_response_item(
        self, resource_cls, parent, identifiers, resource_data
    ):
        """
        Handles the creation of a single response item by setting
        parameters and creating the appropriate resource instance.

        :type resource_cls: ServiceResource subclass
        :param resource_cls: The resource class to instantiate.
        :type parent: ServiceResource
        :param parent: The resource instance to which this action is attached.
        :type identifiers: dict
        :param identifiers: Map of identifier names to value or values.
        :type resource_data: dict or None
        :param resource_data: Data for resource attributes.
        :rtype: ServiceResource
        :return: New resource instance.
        """
        pass
