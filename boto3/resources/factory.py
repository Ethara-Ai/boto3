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
from functools import partial

from ..docs import docstring
from ..exceptions import ResourceLoadException
from .action import ServiceAction, WaiterAction
from .base import ResourceMeta, ServiceResource
from .collection import CollectionFactory
from .model import ResourceModel
from .response import ResourceHandler, build_identifiers

logger = logging.getLogger(__name__)


class ResourceFactory:
    """
    A factory to create new :py:class:`~boto3.resources.base.ServiceResource`
    classes from a :py:class:`~boto3.resources.model.ResourceModel`. There are
    two types of lookups that can be done: one on the service itself (e.g. an
    SQS resource) and another on models contained within the service (e.g. an
    SQS Queue resource).
    """

    def __init__(self, emitter):
        self._collection_factory = CollectionFactory()
        self._emitter = emitter

    def load_from_definition(
        self, resource_name, single_resource_json_definition, service_context
    ):
        """
        Loads a resource from a model, creating a new
        :py:class:`~boto3.resources.base.ServiceResource` subclass
        with the correct properties and methods, named based on the service
        and resource name, e.g. EC2.Instance.

        :type resource_name: string
        :param resource_name: Name of the resource to look up. For services,
                              this should match the ``service_name``.

        :type single_resource_json_definition: dict
        :param single_resource_json_definition:
            The loaded json of a single service resource or resource
            definition.

        :type service_context: :py:class:`~boto3.utils.ServiceContext`
        :param service_context: Context about the AWS service

        :rtype: Subclass of :py:class:`~boto3.resources.base.ServiceResource`
        :return: The service or resource class.
        """
        pass

    def _load_identifiers(self, attrs, meta, resource_model, resource_name):
        """
        Populate required identifiers. These are arguments without which
        the resource cannot be used. Identifiers become arguments for
        operations on the resource.
        """
        pass

    def _load_actions(
        self, attrs, resource_name, resource_model, service_context
    ):
        """
        Actions on the resource become methods, with the ``load`` method
        being a special case which sets internal data for attributes, and
        ``reload`` is an alias for ``load``.
        """
        pass

    def _load_attributes(
        self, attrs, meta, resource_name, resource_model, service_context
    ):
        """
        Load resource attributes based on the resource shape. The shape
        name is referenced in the resource JSON, but the shape itself
        is defined in the Botocore service JSON, hence the need for
        access to the ``service_model``.
        """
        pass

    def _load_collections(self, attrs, resource_model, service_context):
        """
        Load resource collections from the model. Each collection becomes
        a :py:class:`~boto3.resources.collection.CollectionManager` instance
        on the resource instance, which allows you to iterate and filter
        through the collection's items.
        """
        pass

    def _load_has_relations(
        self, attrs, resource_name, resource_model, service_context
    ):
        """
        Load related resources, which are defined via a ``has``
        relationship but conceptually come in two forms:

        1. A reference, which is a related resource instance and can be
           ``None``, such as an EC2 instance's ``vpc``.
        2. A subresource, which is a resource constructor that will always
           return a resource instance which shares identifiers/data with
           this resource, such as ``s3.Bucket('name').Object('key')``.
        """
        pass

    def _create_available_subresources_command(self, attrs, subresources):
        pass

    def _load_waiters(
        self, attrs, resource_name, resource_model, service_context
    ):
        """
        Load resource waiters from the model. Each waiter allows you to
        wait until a resource reaches a specific state by polling the state
        of the resource.
        """
        pass

    def _create_identifier(factory_self, identifier, resource_name):
        """
        Creates a read-only property for identifier attributes.
        """
        pass

    def _create_identifier_alias(
        factory_self, resource_name, identifier, member_model, service_context
    ):
        """
        Creates a read-only property that aliases an identifier.
        """
        pass

    def _create_autoload_property(
        factory_self,
        resource_name,
        name,
        snake_cased,
        member_model,
        service_context,
    ):
        """
        Creates a new property on the resource to lazy-load its value
        via the resource's ``load`` method (if it exists).
        """
        pass

    def _create_waiter(
        factory_self, resource_waiter_model, resource_name, service_context
    ):
        """
        Creates a new wait method for each resource where both a waiter and
        resource model is defined.
        """
        pass

    def _create_collection(
        factory_self, resource_name, collection_model, service_context
    ):
        """
        Creates a new property on the resource to lazy-load a collection.
        """
        pass

    def _create_reference(
        factory_self, reference_model, resource_name, service_context
    ):
        """
        Creates a new property on the resource to lazy-load a reference.
        """
        pass

    def _create_class_partial(
        factory_self, subresource_model, resource_name, service_context
    ):
        """
        Creates a new method which acts as a functools.partial, passing
        along the instance's low-level `client` to the new resource
        class' constructor.
        """
        pass

    def _create_action(
        factory_self,
        action_model,
        resource_name,
        service_context,
        is_load=False,
    ):
        """
        Creates a new method which makes a request to the underlying
        AWS service.
        """
        pass
