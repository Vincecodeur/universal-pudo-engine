from unittest.mock import Mock

from universal_pudo.application.use_cases.list_carriers import (
    ListCarriersUseCase,
)


def test_list_carriers_calls_repository() -> None:
    repository = Mock()

    repository.list_all.return_value = [
        "carrier-a",
        "carrier-b",
    ]

    use_case = ListCarriersUseCase(
        repository,
    )

    result = use_case.execute()

    repository.list_all.assert_called_once()

    assert len(result) == 2