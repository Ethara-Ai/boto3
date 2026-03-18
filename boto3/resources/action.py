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

from botocore import xform_name

from boto3.docs.docstring import ActionDocstring
from boto3.utils import inject_attribute

from .model import Action
from .params import create_request_parameters
from .response import RawHandler, ResourceHandler

logger = logging.getLogger(__name__)


class ServiceAction:
    """
    A class representing a callable action on a resource, for example
    ``sqs.get_queue_by_name(...)`` or ``s3.Bucket('foo').delete()``.
    The action may construct parameters from existing resource identifiers
    and may return either a raw response or a new resource instance.

    :type action_model: :py:class`~boto3.resources.model.Action`
    :param action_model: The action model.

    :type factory: ResourceFactory
    :param factory: The factory that created the resource class to which
                    this action is attached.

    :type service_context: :py:class:`~boto3.utils.ServiceContext`
    :param service_context: Context about the AWS service
    """

    def __init__(self, action_model, factory=None, service_context=None):
        pass

    def __call__(self, parent, *args, **kwargs):
        """
        Perform the action's request operation after building operation
        parameters and build any defined resources from the response.

        :type parent: :py:class:`~boto3.resources.base.ServiceResource`
        :param parent: The resource instance to which this action is attached.
        :rtype: dict or ServiceResource or list(ServiceResource)
        :return: The response, either as a raw dict or resource instance(s).
        """
        pass


class BatchAction(ServiceAction):
    """
    An action which operates on a batch of items in a collection, typically
    a single page of results from the collection's underlying service
    operation call. For example, this allows you to delete up to 999
    S3 objects in a single operation rather than calling ``.delete()`` on
    each one individually.

    :type action_model: :py:class`~boto3.resources.model.Action`
    :param action_model: The action model.

    :type factory: ResourceFactory
    :param factory: The factory that created the resource class to which
                    this action is attached.

    :type service_context: :py:class:`~boto3.utils.ServiceContext`
    :param service_context: Context about the AWS service
    """

    def __call__(self, parent, *args, **kwargs):
        """
        Perform the batch action's operation on every page of results
        from the collection.

        :type parent:
            :py:class:`~boto3.resources.collection.ResourceCollection`
        :param parent: The collection iterator to which this action
                       is attached.
        :rtype: list(dict)
        :return: A list of low-level response dicts from each call.
        """
        pass


class WaiterAction:
    """
    A class representing a callable waiter action on a resource, for example
    ``s3.Bucket('foo').wait_until_bucket_exists()``.
    The waiter action may construct parameters from existing resource
    identifiers.

    :type waiter_model: :py:class`~boto3.resources.model.Waiter`
    :param waiter_model: The action waiter.
    :type waiter_resource_name: string
    :param waiter_resource_name: The name of the waiter action for the
                                 resource. It usually begins with a
                                 ``wait_until_``
    """

    def __init__(self, waiter_model, waiter_resource_name):
        self._waiter_model = waiter_model
        self._waiter_resource_name = waiter_resource_name

    def __call__(self, parent, *args, **kwargs):
        """
        Perform the wait operation after building operation
        parameters.

        :type parent: :py:class:`~boto3.resources.base.ServiceResource`
        :param parent: The resource instance to which this action is attached.
        """
        pass


class CustomModeledAction:
    """A custom, modeled action to inject into a resource."""

    def __init__(self, action_name, action_model, function, event_emitter):
        """
        :type action_name: str
        :param action_name: The name of the action to inject, e.g.
            'delete_tags'

        :type action_model: dict
        :param action_model: A JSON definition of the action, as if it were
            part of the resource model.

        :type function: function
        :param function: The function to perform when the action is called.
            The first argument should be 'self', which will be the resource
            the function is to be called on.

        :type event_emitter: :py:class:`botocore.hooks.BaseEventHooks`
        :param event_emitter: The session event emitter.
        """
        self.name = action_name
        self.model = action_model
        self.function = function
        self.emitter = event_emitter

    def inject(self, class_attributes, service_context, event_name, **kwargs):
        pass
