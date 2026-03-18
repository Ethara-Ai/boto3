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
from botocore.docs.method import (
    document_custom_method,
    document_model_driven_method,
)
from botocore.model import OperationModel
from botocore.utils import get_service_module_name

from boto3.docs.base import NestedDocumenter
from boto3.docs.method import document_model_driven_resource_method
from boto3.docs.utils import (
    add_resource_type_overview,
    get_resource_ignore_params,
    get_resource_public_actions,
)

PUT_DATA_WARNING_MESSAGE = """
.. warning::
    It is recommended to use the :py:meth:`put_metric_data`
    :doc:`client method <../../cloudwatch/client/put_metric_data>`
    instead. If you would still like to use this resource method,
    please make sure that ``MetricData[].MetricName`` is equal to
    the metric resource's ``name`` attribute.
"""

WARNING_MESSAGES = {
    "Metric": {"put_data": PUT_DATA_WARNING_MESSAGE},
}

IGNORE_PARAMS = {"Metric": {"put_data": ["Namespace"]}}


class ActionDocumenter(NestedDocumenter):
    def document_actions(self, section):
        pass


def document_action(
    section,
    resource_name,
    event_emitter,
    action_model,
    service_model,
    include_signature=True,
):
    """Documents a resource action

    :param section: The section to write to

    :param resource_name: The name of the resource

    :param event_emitter: The event emitter to use to emit events

    :param action_model: The model of the action

    :param service_model: The model of the service

    :param include_signature: Whether or not to include the signature.
        It is useful for generating docstrings.
    """
    pass


def document_load_reload_action(
    section,
    action_name,
    resource_name,
    event_emitter,
    load_model,
    service_model,
    include_signature=True,
):
    """Documents the resource load action

    :param section: The section to write to

    :param action_name: The name of the loading action should be load or reload

    :param resource_name: The name of the resource

    :param event_emitter: The event emitter to use to emit events

    :param load_model: The model of the load action

    :param service_model: The model of the service

    :param include_signature: Whether or not to include the signature.
        It is useful for generating docstrings.
    """
    pass
