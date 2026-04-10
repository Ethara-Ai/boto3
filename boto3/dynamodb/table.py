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
import logging

logger = logging.getLogger(__name__)


def register_table_methods(base_classes, **kwargs):
    pass


# This class can be used to add any additional methods we want
# onto a table resource.  Ideally to avoid creating a new
# base class for every method we can just update this
# class instead.  Just be sure to move the bulk of the
# actual method implementation to another class.
class TableResource:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def batch_writer(self, overwrite_by_pkeys=None):
        """Create a batch writer object.

        This method creates a context manager for writing
        objects to Amazon DynamoDB in batch.

        The batch writer will automatically handle buffering and sending items
        in batches.  In addition, the batch writer will also automatically
        handle any unprocessed items and resend them as needed.  All you need
        to do is call ``put_item`` for any items you want to add, and
        ``delete_item`` for any items you want to delete.

        Example usage::

            with table.batch_writer() as batch:
                for _ in range(1000000):
                    batch.put_item(Item={'HashKey': '...',
                                         'Otherstuff': '...'})
                # You can also delete_items in a batch.
                batch.delete_item(Key={'HashKey': 'SomeHashKey'})

        :type overwrite_by_pkeys: list(string)
        :param overwrite_by_pkeys: De-duplicate request items in buffer
            if match new request item on specified primary keys. i.e
            ``["partition_key1", "sort_key2", "sort_key3"]``

        """
        pass


class BatchWriter:
    """Automatically handle batch writes to DynamoDB for a single table."""

    def __init__(
        self, table_name, client, flush_amount=25, overwrite_by_pkeys=None
    ):
        """

        :type table_name: str
        :param table_name: The name of the table.  The class handles
            batch writes to a single table.

        :type client: ``botocore.client.Client``
        :param client: A botocore client.  Note this client
            **must** have the dynamodb customizations applied
            to it for transforming AttributeValues into the
            wire protocol.  What this means in practice is that
            you need to use a client that comes from a DynamoDB
            resource if you're going to instantiate this class
            directly, i.e
            ``boto3.resource('dynamodb').Table('foo').meta.client``.

        :type flush_amount: int
        :param flush_amount: The number of items to keep in
            a local buffer before sending a batch_write_item
            request to DynamoDB.

        :type overwrite_by_pkeys: list(string)
        :param overwrite_by_pkeys: De-duplicate request items in buffer
            if match new request item on specified primary keys. i.e
            ``["partition_key1", "sort_key2", "sort_key3"]``

        """
        self._table_name = table_name
        self._client = client
        self._items_buffer = []
        self._flush_amount = flush_amount
        self._overwrite_by_pkeys = overwrite_by_pkeys

    def put_item(self, Item):
        pass

    def delete_item(self, Key):
        pass

    def _add_request_and_process(self, request):
        pass

    def _remove_dup_pkeys_request_if_any(self, request):
        pass

    def _extract_pkey_values(self, request):
        pass

    def _flush_if_needed(self):
        pass

    def _flush(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        # When we exit, we need to keep flushing whatever's left
        # until there's nothing left in our items buffer.
        while self._items_buffer:
            self._flush()
