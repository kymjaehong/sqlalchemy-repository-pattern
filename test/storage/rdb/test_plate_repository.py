"""test_plate_repository.py"""
import pytest
from datetime import datetime
from .with_mock import MockPlateRepository
from src.storage.rdb.plate.plate_entity import PlateEntity


NOW = datetime.now()


@pytest.fixture
def fixture():
    return {
        0: PlateEntity(
            content="pytest 학습",
            is_complete=False,
            created_at=NOW,
            modified_at=NOW,
            user_id=1,
        ),
        1: PlateEntity(
            content="운동하기",
            is_complete=True,
            created_at=NOW,
            modified_at=NOW,
            user_id=1,
        ),
        2: PlateEntity(
            content="8시간 자기",
            is_complete=True,
            created_at=NOW,
            modified_at=NOW,
            user_id=1,
        ),
    }


@pytest.mark.asyncio
async def test_find_by_id(fixture):
    repo = MockPlateRepository(plates=fixture)
    res = await repo.find_by_id(0)

    assert res.content == "pytest 학습"
    assert res.user_id == 1


if __name__ == "__main__":
    pytest.main()
