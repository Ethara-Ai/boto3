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
from botocore.docs.utils import get_official_service_name

from boto3.docs.action import ActionDocumenter
from boto3.docs.attr import (
    document_attribute,
    document_identifier,
    document_reference,
)
from boto3.docs.base import BaseDocumenter
from boto3.docs.collection import CollectionDocumenter
from boto3.docs.subresource import SubResourceDocumenter
from boto3.docs.utils import (
    add_resource_type_overview,
    get_identifier_args_for_signature,
    get_identifier_description,
    get_identifier_values_for_example,
)
from boto3.docs.waiter import WaiterResourceDocumenter


class ResourceDocumenter(BaseDocumenter):
    def __init__(self, resource, botocore_session, root_docs_path):
        pass

    def document_resource(self, section):
        pass

    def _add_title(self, section):
        pass

    def _add_intro(self, section):
        pass

    def _add_description(self, section):
        pass

    def _add_example(self, section, identifier_names):
        pass

    def _add_params_description(self, section, identifier_names):
        pass

    def _add_overview_of_member_type(self, section, resource_member_type):
        pass

    def _add_identifiers(self, section):
        pass

    def _add_attributes(self, section):
        pass

    def _add_references(self, section):
        pass

    def _add_actions(self, section):
        pass

    def _add_sub_resources(self, section):
        pass

    def _add_collections(self, section):
        pass

    def _add_waiters(self, section):
        pass

    def _add_resource_note(self, section):
        pass


class ServiceResourceDocumenter(ResourceDocumenter):
    @property
    def class_name(self):
        pass

    def _add_title(self, section):
        pass

    def _add_description(self, section):
        pass

    def _add_example(self, section, identifier_names):
        pass
