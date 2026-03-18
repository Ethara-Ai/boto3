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
from botocore.utils import get_service_module_name

from boto3.docs.base import NestedDocumenter
from boto3.docs.utils import (
    add_resource_type_overview,
    get_identifier_args_for_signature,
    get_identifier_description,
    get_identifier_values_for_example,
)


class SubResourceDocumenter(NestedDocumenter):
    def document_sub_resources(self, section):
        pass


def document_sub_resource(
    section,
    resource_name,
    sub_resource_model,
    service_model,
    include_signature=True,
):
    """Documents a resource action

    :param section: The section to write to

    :param resource_name: The name of the resource

    :param sub_resource_model: The model of the subresource

    :param service_model: The model of the service

    :param include_signature: Whether or not to include the signature.
        It is useful for generating docstrings.
    """
    pass
