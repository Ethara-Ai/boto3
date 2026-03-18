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
import copy

from boto3.compat import collections_abc
from boto3.docs.utils import DocumentModifiedShape
from boto3.dynamodb.conditions import ConditionBase, ConditionExpressionBuilder
from boto3.dynamodb.types import TypeDeserializer, TypeSerializer


def register_high_level_interface(base_classes, **kwargs):
    pass


class _ForgetfulDict(dict):
    """A dictionary that discards any items set on it. For use as `memo` in
    `copy.deepcopy()` when every instance of a repeated object in the deepcopied
    data structure should result in a separate copy.
    """

    def __setitem__(self, key, value):
        pass


def copy_dynamodb_params(params, **kwargs):
    pass


class DynamoDBHighLevelResource:
    def __init__(self, *args, **kwargs):
        pass


class TransformationInjector:
    """Injects the transformations into the user provided parameters."""

    def __init__(
        self,
        transformer=None,
        condition_builder=None,
        serializer=None,
        deserializer=None,
    ):
        pass

    def inject_condition_expressions(self, params, model, **kwargs):
        """Injects the condition expression transformation into the parameters

        This injection includes transformations for ConditionExpression shapes
        and KeyExpression shapes. It also handles any placeholder names and
        values that are generated when transforming the condition expressions.
        """
        pass

    def inject_attribute_value_input(self, params, model, **kwargs):
        """Injects DynamoDB serialization into parameter input"""
        pass

    def inject_attribute_value_output(self, parsed, model, **kwargs):
        """Injects DynamoDB deserialization into responses"""
        pass


class ConditionExpressionTransformation:
    """Provides a transformation for condition expressions

    The ``ParameterTransformer`` class can call this class directly
    to transform the condition expressions in the parameters provided.
    """

    def __init__(
        self,
        condition_builder,
        placeholder_names,
        placeholder_values,
        is_key_condition=False,
    ):
        self._condition_builder = condition_builder
        self._placeholder_names = placeholder_names
        self._placeholder_values = placeholder_values
        self._is_key_condition = is_key_condition

    def __call__(self, value):
        pass


class ParameterTransformer:
    """Transforms the input to and output from botocore based on shape"""

    def transform(self, params, model, transformation, target_shape):
        """Transforms the dynamodb input to or output from botocore

        It applies a specified transformation whenever a specific shape name
        is encountered while traversing the parameters in the dictionary.

        :param params: The parameters structure to transform.
        :param model: The operation model.
        :param transformation: The function to apply the parameter
        :param target_shape: The name of the shape to apply the
            transformation to
        """
        pass

    def _transform_parameters(
        self, model, params, transformation, target_shape
    ):
        pass

    def _transform_structure(
        self, model, params, transformation, target_shape
    ):
        pass

    def _transform_map(self, model, params, transformation, target_shape):
        pass

    def _transform_list(self, model, params, transformation, target_shape):
        pass
