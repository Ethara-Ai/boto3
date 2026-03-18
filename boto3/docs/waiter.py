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
from botocore.docs.method import document_model_driven_method
from botocore.utils import get_service_module_name

from boto3.docs.base import NestedDocumenter
from boto3.docs.utils import (
    add_resource_type_overview,
    get_resource_ignore_params,
)


class WaiterResourceDocumenter(NestedDocumenter):
    def __init__(self, resource, service_waiter_model, root_docs_path):
        super().__init__(resource, root_docs_path)
        self._service_waiter_model = service_waiter_model

    def document_resource_waiters(self, section):
        pass


def document_resource_waiter(
    section,
    resource_name,
    event_emitter,
    service_model,
    resource_waiter_model,
    service_waiter_model,
    include_signature=True,
):
    pass
