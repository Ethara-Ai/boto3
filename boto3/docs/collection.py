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
import os

from botocore import xform_name
from botocore.docs.bcdoc.restdoc import DocumentStructure
from botocore.docs.method import get_instance_public_methods
from botocore.docs.utils import DocumentedShape

from boto3.docs.base import NestedDocumenter
from boto3.docs.method import document_model_driven_resource_method
from boto3.docs.utils import (
    add_resource_type_overview,
    get_resource_ignore_params,
)


class CollectionDocumenter(NestedDocumenter):
    def document_collections(self, section):
        pass

    def _document_collection(self, section, collection):
        pass


def document_collection_object(
    section,
    collection_model,
    include_signature=True,
):
    """Documents a collection resource object

    :param section: The section to write to

    :param collection_model: The model of the collection

    :param include_signature: Whether or not to include the signature.
        It is useful for generating docstrings.
    """
    pass


def document_batch_action(
    section,
    resource_name,
    event_emitter,
    batch_action_model,
    service_model,
    collection_model,
    include_signature=True,
):
    """Documents a collection's batch action

    :param section: The section to write to

    :param resource_name: The name of the resource

    :param action_name: The name of collection action. Currently only
        can be all, filter, limit, or page_size

    :param event_emitter: The event emitter to use to emit events

    :param batch_action_model: The model of the batch action

    :param collection_model: The model of the collection

    :param service_model: The model of the service

    :param include_signature: Whether or not to include the signature.
        It is useful for generating docstrings.
    """
    pass


def document_collection_method(
    section,
    resource_name,
    action_name,
    event_emitter,
    collection_model,
    service_model,
    include_signature=True,
):
    """Documents a collection method

    :param section: The section to write to

    :param resource_name: The name of the resource

    :param action_name: The name of collection action. Currently only
        can be all, filter, limit, or page_size

    :param event_emitter: The event emitter to use to emit events

    :param collection_model: The model of the collection

    :param service_model: The model of the service

    :param include_signature: Whether or not to include the signature.
        It is useful for generating docstrings.
    """
    pass
