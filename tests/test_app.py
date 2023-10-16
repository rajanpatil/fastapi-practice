import pytest
import app


@pytest.mark.asyncio
async def test_index():
    assert {"message": "Hello World"} == await app.index()
