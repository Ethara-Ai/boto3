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
import inspect

import jmespath


def get_resource_ignore_params(params):
    """Helper method to determine which parameters to ignore for actions

    :returns: A list of the parameter names that does not need to be
        included in a resource's method call for documentation purposes.
    """
    pass


def is_resource_action(action_handle):
    pass


def get_resource_public_actions(resource_class):
    pass


def get_identifier_values_for_example(identifier_names):
    pass


def get_identifier_args_for_signature(identifier_names):
    pass


def get_identifier_description(resource_name, identifier_name):
    pass


def add_resource_type_overview(
    section, resource_type, description, intro_link=None
):
    pass


class DocumentModifiedShape:
    def __init__(
        self, shape_name, new_type, new_description, new_example_value
    ):
        self._shape_name = shape_name
        self._new_type = new_type
        self._new_description = new_description
        self._new_example_value = new_example_value

    def replace_documentation_for_matching_shape(
        self, event_name, section, **kwargs
    ):
        pass

    def _replace_documentation(self, event_name, section):
        pass
