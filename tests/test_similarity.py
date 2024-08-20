import pytest
import asyncio
from thispkg.odm import Embedding
import numpy as np

async def create_embedding(vector_store_id: str):
    embedding = Embedding(embedding=np.random.rand(768),content=vector_store_id)
    return await embedding.put(vector_store_id=vector_store_id)
    

@pytest.mark.parametrize("vector_store_id", [str(i) for i in range(10)])
@pytest.mark.asyncio
async def test_create(vector_store_id: str):
    data = await asyncio.gather(*[create_embedding(vector_store_id) for _ in range(10)])
    assert isinstance(data, list)
    assert len(data) == 10

@pytest.mark.parametrize("vector_store_id", [str(i) for i in range(10)])
@pytest.mark.asyncio
async def test_search(vector_store_id: str):
    embedding = Embedding(embedding=np.random.rand(768),content=vector_store_id)
    data = await embedding.search(
        vector_store_id=vector_store_id,
        query={"vector": embedding.embedding, "topK": 10},
        algorithm="cosine",
    )
    assert isinstance(data, list)
    assert len(data) == 10


@pytest.mark.skip(reason="Not implemented")
@pytest.mark.parametrize("vector_store_id", [str(i) for i in range(10)])
@pytest.mark.asyncio
async def test_delete(vector_store_id: str):
    embeddings = await Embedding.scan(vector_store_id=vector_store_id)
    await asyncio.gather(*[e.delete(vector_store_id=vector_store_id,id=e.id) for e in embeddings])
    assert len(await Embedding.find(vector_store_id=vector_store_id)) == 0
    
