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
from botocore.compat import OrderedDict


class BaseDocumenter:
    def __init__(self, resource):
        pass

    @property
    def class_name(self):
        pass


class NestedDocumenter(BaseDocumenter):
    def __init__(self, resource, root_docs_path):
        pass

    @property
    def class_name(self):
        pass
