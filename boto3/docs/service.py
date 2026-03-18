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

from botocore.docs.bcdoc.restdoc import DocumentStructure
from botocore.docs.service import ServiceDocumenter as BaseServiceDocumenter
from botocore.exceptions import DataNotFoundError

import boto3
from boto3.docs.client import Boto3ClientDocumenter
from boto3.docs.resource import ResourceDocumenter, ServiceResourceDocumenter
from boto3.utils import ServiceContext


class ServiceDocumenter(BaseServiceDocumenter):
    # The path used to find examples
    EXAMPLE_PATH = os.path.join(os.path.dirname(boto3.__file__), 'examples')

    def __init__(self, service_name, session, root_docs_path):
        pass

    def document_service(self):
        """Documents an entire service.

        :returns: The reStructured text of the documented service.
        """
        pass

    def client_api(self, section):
        pass

    def resource_section(self, section):
        pass

    def _document_service_resource(self, section):
        # Create a new DocumentStructure for each Service Resource and add contents.
        pass

    def _document_resources(self, section):
        pass

    def _get_example_file(self):
        pass

    def _document_examples(self, section):
        pass
