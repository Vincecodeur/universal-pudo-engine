from universal_pudo.providers.mondial_relay.security import (
    MondialRelaySecurity,
)


def test_generate_returns_string():
    result = MondialRelaySecurity.generate(
        "ABC",
        "123",
        private_key="SECRET",
    )

    assert isinstance(result, str)


def test_generate_returns_md5_length():
    result = MondialRelaySecurity.generate(
        "ABC",
        private_key="SECRET",
    )

    assert len(result) == 32


def test_generate_returns_uppercase():
    result = MondialRelaySecurity.generate(
        "ABC",
        private_key="SECRET",
    )

    assert result == result.upper()


def test_generate_is_deterministic():
    value_1 = MondialRelaySecurity.generate(
        "ABC",
        "123",
        private_key="SECRET",
    )

    value_2 = MondialRelaySecurity.generate(
        "ABC",
        "123",
        private_key="SECRET",
    )

    assert value_1 == value_2