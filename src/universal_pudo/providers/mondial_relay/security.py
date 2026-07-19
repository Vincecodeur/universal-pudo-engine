import hashlib


class MondialRelaySecurity:
    """
    Mondial Relay SECURITY hash generator.

    SECURITY is computed as:

    concat(parameters in exact API order)
    +
    private key

    ↓

    MD5
    ↓
    UPPERCASE HEX
    """

    @staticmethod
    def generate(
        *values: str,
        private_key: str,
    ) -> str:
        payload = "".join(
            str(value)
            for value in values
        )

        payload += private_key

        return hashlib.md5(
            payload.encode("utf-8")
        ).hexdigest().upper()