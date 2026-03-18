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
from botocore.docs.params import ResponseParamsDocumenter

from boto3.docs.utils import get_identifier_description


class ResourceShapeDocumenter(ResponseParamsDocumenter):
    EVENT_NAME = 'resource-shape'


def document_attribute(
    section,
    service_name,
    resource_name,
    attr_name,
    event_emitter,
    attr_model,
    include_signature=True,
):
    pass


def document_identifier(
    section,
    resource_name,
    identifier_model,
    include_signature=True,
):
    pass


def document_reference(section, reference_model, include_signature=True):
    pass
