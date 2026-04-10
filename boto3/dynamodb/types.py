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
from decimal import (
    Clamped,
    Context,
    Decimal,
    Inexact,
    Overflow,
    Rounded,
    Underflow,
)

from boto3.compat import collections_abc

STRING = 'S'
NUMBER = 'N'
BINARY = 'B'
STRING_SET = 'SS'
NUMBER_SET = 'NS'
BINARY_SET = 'BS'
NULL = 'NULL'
BOOLEAN = 'BOOL'
MAP = 'M'
LIST = 'L'


DYNAMODB_CONTEXT = Context(
    Emin=-128,
    Emax=126,
    prec=38,
    traps=[Clamped, Overflow, Inexact, Rounded, Underflow],
)


BINARY_TYPES = (bytearray, bytes)


class Binary:
    """A class for representing Binary in dynamodb

    Especially for Python 2, use this class to explicitly specify
    binary data for item in DynamoDB. It is essentially a wrapper around
    binary. Unicode and Python 3 string types are not allowed.
    """

    def __init__(self, value):
        if not isinstance(value, BINARY_TYPES):
            types = ', '.join([str(t) for t in BINARY_TYPES])
            raise TypeError(f'Value must be of the following types: {types}')
        self.value = value

    def __eq__(self, other):
        if isinstance(other, Binary):
            return self.value == other.value
        return self.value == other

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return f'Binary({self.value!r})'

    def __str__(self):
        return self.value

    def __bytes__(self):
        return self.value

    def __hash__(self):
        return hash(self.value)


class TypeSerializer:
    """This class serializes Python data types to DynamoDB types."""

    def serialize(self, value):
        """The method to serialize the Python data types.

        :param value: A python value to be serialized to DynamoDB. Here are
            the various conversions:

            Python                                  DynamoDB
            ------                                  --------
            None                                    {'NULL': True}
            True/False                              {'BOOL': True/False}
            int/Decimal                             {'N': str(value)}
            string                                  {'S': string}
            Binary/bytearray/bytes (py3 only)       {'B': bytes}
            set([int/Decimal])                      {'NS': [str(value)]}
            set([string])                           {'SS': [string])
            set([Binary/bytearray/bytes])           {'BS': [bytes]}
            list                                    {'L': list}
            dict                                    {'M': dict}

            For types that involve numbers, it is recommended that ``Decimal``
            objects are used to be able to round-trip the Python type.
            For types that involve binary, it is recommended that ``Binary``
            objects are used to be able to round-trip the Python type.

        :rtype: dict
        :returns: A dictionary that represents a dynamoDB data type. These
            dictionaries can be directly passed to botocore methods.
        """
        pass

    def _get_dynamodb_type(self, value):
        pass

    def _is_null(self, value):
        pass

    def _is_boolean(self, value):
        pass

    def _is_number(self, value):
        pass

    def _is_string(self, value):
        pass

    def _is_binary(self, value):
        pass

    def _is_set(self, value):
        pass

    def _is_type_set(self, value, type_validator):
        pass

    def _is_map(self, value):
        pass

    def _is_listlike(self, value):
        pass

    def _serialize_null(self, value):
        pass

    def _serialize_bool(self, value):
        pass

    def _serialize_n(self, value):
        pass

    def _serialize_s(self, value):
        pass

    def _serialize_b(self, value):
        pass

    def _serialize_ss(self, value):
        pass

    def _serialize_ns(self, value):
        pass

    def _serialize_bs(self, value):
        pass

    def _serialize_l(self, value):
        pass

    def _serialize_m(self, value):
        pass


class TypeDeserializer:
    """This class deserializes DynamoDB types to Python types."""

    def deserialize(self, value):
        """The method to deserialize the DynamoDB data types.

        :param value: A DynamoDB value to be deserialized to a pythonic value.
            Here are the various conversions:

            DynamoDB                                Python
            --------                                ------
            {'NULL': True}                          None
            {'BOOL': True/False}                    True/False
            {'N': str(value)}                       Decimal(str(value))
            {'S': string}                           string
            {'B': bytes}                            Binary(bytes)
            {'NS': [str(value)]}                    set([Decimal(str(value))])
            {'SS': [string]}                        set([string])
            {'BS': [bytes]}                         set([bytes])
            {'L': list}                             list
            {'M': dict}                             dict

        :returns: The pythonic value of the DynamoDB type.
        """
        pass

    def _deserialize_null(self, value):
        pass

    def _deserialize_bool(self, value):
        pass

    def _deserialize_n(self, value):
        pass

    def _deserialize_s(self, value):
        pass

    def _deserialize_b(self, value):
        pass

    def _deserialize_ns(self, value):
        pass

    def _deserialize_ss(self, value):
        pass

    def _deserialize_bs(self, value):
        pass

    def _deserialize_l(self, value):
        pass

    def _deserialize_m(self, value):
        pass
