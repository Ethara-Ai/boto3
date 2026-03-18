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


def inject_create_tags(event_name, class_attributes, **kwargs):
    """This injects a custom create_tags method onto the ec2 service resource

    This is needed because the resource model is not able to express
    creating multiple tag resources based on the fact you can apply a set
    of tags to multiple ec2 resources.
    """
    pass


def create_tags(self, **kwargs):
    # Call the client method
    pass
