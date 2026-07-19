from __future__ import annotations

from typing import Any

import requests


class ColissimoClient:
    BASE_URL = (
        "https://ws.colissimo.fr/"
        "pointretrait-ws-cxf/rest/v2/"
        "pointretrait/"
        "findRDVPointRetraitAcheminement"
    )

    def __init__(
        self,
        api_key: str,
        timeout: int = 10,
    ) -> None:
        self.api_key = api_key
        self.timeout = timeout

    def search_pickup_points(
        self,
        *,
        address: str,
        zip_code: str,
        city: str,
        country_code: str = "FR",
        weight: str = "1000",
        shipping_date: str,
        filter_relay: str = "1",
        request_id: str = "universal-pudo",
        lang: str = "FR",
    ) -> dict[str, Any]:

        payload = {
            "apikey": self.api_key,
            "address": address,
            "zipCode": zip_code,
            "city": city,
            "countryCode": country_code,
            "weight": weight,
            "shippingDate": shipping_date,
            "filterRelay": filter_relay,
            "requestId": request_id,
            "lang": lang,
        }

        response = requests.post(
            self.BASE_URL,
            json=payload,
            timeout=self.timeout,
        )

        response.raise_for_status()

        return response.json()