from fastapi.testclient import TestClient
from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession


async def test_select_1(acync_session: AsyncSession):
    result = await acync_session.scalar(select(text("1")))
    assert result == 1
