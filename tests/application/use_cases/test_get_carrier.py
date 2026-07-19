from unittest.mock import Mock

from universal_pudo.application.use_cases.get_carrier import (
    GetCarrierUseCase,
)


def test_get_carrier_calls_repository() -> None:
    repository = Mock()

    repository.get_by_id.return_value = "carrier"

    use_case = GetCarrierUseCase(
        repository,
    )

    result = use_case.execute(
        "carrier-001",
    )

    repository.get_by_id.assert_called_once_with(
        "carrier-001",
    )

    assert result == "carrier"