"""test_user_repository.py"""
import pytest
from datetime import datetime
from .with_mock import MockUserRepository
from src.storage.rdb.user.user_entity import UserEntity

NOW = datetime.now()


@pytest.fixture
def fixture():
    return {
        0: UserEntity(
            account_id="gildong@gmail.com",
            name="홍길동",
            phone_number="01012341234",
            created_at=NOW,
            modified_at=NOW,
        ),
        1: UserEntity(
            account_id="son5gong@gmail.com",
            name="손오공",
            phone_number="01012341235",
            created_at=NOW,
            modified_at=NOW,
        ),
        2: UserEntity(
            account_id="cultureland@gmail.com",
            name="문상훈",
            phone_number="01012341236",
            created_at=NOW,
            modified_at=NOW,
        ),
    }


@pytest.mark.asyncio
async def test_find_by_id(fixture):
    repo = MockUserRepository(users=fixture)
    res = await repo.find_by_id(0)

    assert res.account_id == "gildong@gmail.com"
    assert res.name == "홍길동"


if __name__ == "__main__":
    pytest.main()
