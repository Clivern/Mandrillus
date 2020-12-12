# Copyright 2023 Clivern
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from qdrant_client import QdrantClient
from app.shortcuts import Logger


class Qdrant:
    """Qdrant Class"""

    def __init__(self, url, api_key):
        self._url = url
        self._api_key = api_key
        self._logger = Logger().get_logger(__name__)

    def connect(self):
        self._client = QdrantClient(
            url=self._url,
            api_key=self._api_key,
        )

    def add_records(self, collection, records):
        """
        Add Records

        Args:
            collection: The collection name
            records: The records list like
                [{"doc": "...", "metadata": {"source": "web"}, "id": 1}]
        """

        docs = []
        metadatas = []
        ids = []

        for record in records:
            docs.append(record["doc"])
            metadatas.append(record["metadata"])
            ids.append(record["id"])

        return self._client.add(
            collection_name=collection, documents=docs, metadata=metadatas, ids=ids
        )

    def search_records(self, collection, search_term, limit):
        """
        Search The Records
        """
        return self._client.query(
            collection_name=collection, query_text=search_term, limit=limit
        )
