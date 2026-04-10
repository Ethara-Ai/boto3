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
import re
from collections import namedtuple

from boto3.exceptions import (
    DynamoDBNeedsConditionError,
    DynamoDBNeedsKeyConditionError,
    DynamoDBOperationNotSupportedError,
)

ATTR_NAME_REGEX = re.compile(r'[^.\[\]]+(?![^\[]*\])')


class ConditionBase:
    expression_format = ''
    expression_operator = ''
    has_grouped_values = False

    def __init__(self, *values):
        self._values = values

    def __and__(self, other):
        if not isinstance(other, ConditionBase):
            raise DynamoDBOperationNotSupportedError('AND', other)
        return And(self, other)

    def __or__(self, other):
        if not isinstance(other, ConditionBase):
            raise DynamoDBOperationNotSupportedError('OR', other)
        return Or(self, other)

    def __invert__(self):
        return Not(self)

    def get_expression(self):
        pass

    def __eq__(self, other):
        if isinstance(other, type(self)):
            if self._values == other._values:
                return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)


class AttributeBase:
    def __init__(self, name):
        self.name = name

    def __and__(self, value):
        raise DynamoDBOperationNotSupportedError('AND', self)

    def __or__(self, value):
        raise DynamoDBOperationNotSupportedError('OR', self)

    def __invert__(self):
        raise DynamoDBOperationNotSupportedError('NOT', self)

    def eq(self, value):
        """Creates a condition where the attribute is equal to the value.

        :param value: The value that the attribute is equal to.
        """
        pass

    def lt(self, value):
        """Creates a condition where the attribute is less than the value.

        :param value: The value that the attribute is less than.
        """
        pass

    def lte(self, value):
        """Creates a condition where the attribute is less than or equal to the
           value.

        :param value: The value that the attribute is less than or equal to.
        """
        pass

    def gt(self, value):
        """Creates a condition where the attribute is greater than the value.

        :param value: The value that the attribute is greater than.
        """
        pass

    def gte(self, value):
        """Creates a condition where the attribute is greater than or equal to
           the value.

        :param value: The value that the attribute is greater than or equal to.
        """
        pass

    def begins_with(self, value):
        """Creates a condition where the attribute begins with the value.

        :param value: The value that the attribute begins with.
        """
        pass

    def between(self, low_value, high_value):
        """Creates a condition where the attribute is greater than or equal
        to the low value and less than or equal to the high value.

        :param low_value: The value that the attribute is greater than or equal to.
        :param high_value: The value that the attribute is less than or equal to.
        """
        pass

    def __eq__(self, other):
        return isinstance(other, type(self)) and self.name == other.name

    def __ne__(self, other):
        return not self.__eq__(other)


class ConditionAttributeBase(ConditionBase, AttributeBase):
    """This base class is for conditions that can have attribute methods.

    One example is the Size condition. To complete a condition, you need
    to apply another AttributeBase method like eq().
    """

    def __init__(self, *values):
        ConditionBase.__init__(self, *values)
        # This is assuming the first value to the condition is the attribute
        # in which can be used to generate its attribute base.
        AttributeBase.__init__(self, values[0].name)

    def __eq__(self, other):
        return ConditionBase.__eq__(self, other) and AttributeBase.__eq__(
            self, other
        )

    def __ne__(self, other):
        return not self.__eq__(other)


class ComparisonCondition(ConditionBase):
    expression_format = '{0} {operator} {1}'


class Equals(ComparisonCondition):
    expression_operator = '='


class NotEquals(ComparisonCondition):
    expression_operator = '<>'


class LessThan(ComparisonCondition):
    expression_operator = '<'


class LessThanEquals(ComparisonCondition):
    expression_operator = '<='


class GreaterThan(ComparisonCondition):
    expression_operator = '>'


class GreaterThanEquals(ComparisonCondition):
    expression_operator = '>='


class In(ComparisonCondition):
    expression_operator = 'IN'
    has_grouped_values = True


class Between(ConditionBase):
    expression_operator = 'BETWEEN'
    expression_format = '{0} {operator} {1} AND {2}'


class BeginsWith(ConditionBase):
    expression_operator = 'begins_with'
    expression_format = '{operator}({0}, {1})'


class Contains(ConditionBase):
    expression_operator = 'contains'
    expression_format = '{operator}({0}, {1})'


class Size(ConditionAttributeBase):
    expression_operator = 'size'
    expression_format = '{operator}({0})'


class AttributeType(ConditionBase):
    expression_operator = 'attribute_type'
    expression_format = '{operator}({0}, {1})'


class AttributeExists(ConditionBase):
    expression_operator = 'attribute_exists'
    expression_format = '{operator}({0})'


class AttributeNotExists(ConditionBase):
    expression_operator = 'attribute_not_exists'
    expression_format = '{operator}({0})'


class And(ConditionBase):
    expression_operator = 'AND'
    expression_format = '({0} {operator} {1})'


class Or(ConditionBase):
    expression_operator = 'OR'
    expression_format = '({0} {operator} {1})'


class Not(ConditionBase):
    expression_operator = 'NOT'
    expression_format = '({operator} {0})'


class Key(AttributeBase):
    pass


class Attr(AttributeBase):
    """Represents an DynamoDB item's attribute."""

    def ne(self, value):
        """Creates a condition where the attribute is not equal to the value

        :param value: The value that the attribute is not equal to.
        """
        pass

    def is_in(self, value):
        """Creates a condition where the attribute is in the value,

        :type value: list
        :param value: The value that the attribute is in.
        """
        pass

    def exists(self):
        """Creates a condition where the attribute exists."""
        return AttributeExists(self)

    def not_exists(self):
        """Creates a condition where the attribute does not exist."""
        pass

    def contains(self, value):
        """Creates a condition where the attribute contains the value.

        :param value: The value the attribute contains.
        """
        pass

    def size(self):
        """Creates a condition for the attribute size.

        Note another AttributeBase method must be called on the returned
        size condition to be a valid DynamoDB condition.
        """
        pass

    def attribute_type(self, value):
        """Creates a condition for the attribute type.

        :param value: The type of the attribute.
        """
        pass


BuiltConditionExpression = namedtuple(
    'BuiltConditionExpression',
    [
        'condition_expression',
        'attribute_name_placeholders',
        'attribute_value_placeholders',
    ],
)


class ConditionExpressionBuilder:
    """This class is used to build condition expressions with placeholders"""

    def __init__(self):
        self._name_count = 0
        self._value_count = 0
        self._name_placeholder = 'n'
        self._value_placeholder = 'v'

    def _get_name_placeholder(self):
        pass

    def _get_value_placeholder(self):
        pass

    def reset(self):
        """Resets the placeholder name and values"""
        pass

    def build_expression(self, condition, is_key_condition=False):
        """Builds the condition expression and the dictionary of placeholders.

        :type condition: ConditionBase
        :param condition: A condition to be built into a condition expression
            string with any necessary placeholders.

        :type is_key_condition: Boolean
        :param is_key_condition: True if the expression is for a
            KeyConditionExpression. False otherwise.

        :rtype: (string, dict, dict)
        :returns: Will return a string representing the condition with
            placeholders inserted where necessary, a dictionary of
            placeholders for attribute names, and a dictionary of
            placeholders for attribute values. Here is a sample return value:

            ('#n0 = :v0', {'#n0': 'myattribute'}, {':v1': 'myvalue'})
        """
        pass

    def _build_expression(
        self,
        condition,
        attribute_name_placeholders,
        attribute_value_placeholders,
        is_key_condition,
    ):
        pass

    def _build_expression_component(
        self,
        value,
        attribute_name_placeholders,
        attribute_value_placeholders,
        has_grouped_values,
        is_key_condition,
    ):
        # Continue to recurse if the value is a ConditionBase in order
        # to extract out all parts of the expression.
        pass

    def _build_name_placeholder(self, value, attribute_name_placeholders):
        pass

    def _build_value_placeholder(
        self, value, attribute_value_placeholders, has_grouped_values=False
    ):
        # If the values are grouped, we need to add a placeholder for
        # each element inside of the actual value.
        pass
