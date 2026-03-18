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
from botocore.docs.method import document_model_driven_method


def document_model_driven_resource_method(
    section,
    method_name,
    operation_model,
    event_emitter,
    method_description=None,
    example_prefix=None,
    include_input=None,
    include_output=None,
    exclude_input=None,
    exclude_output=None,
    document_output=True,
    resource_action_model=None,
    include_signature=True,
):
    pass


def _method_returns_resource_list(resource):
    pass
