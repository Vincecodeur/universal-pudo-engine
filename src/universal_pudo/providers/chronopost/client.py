from __future__ import annotations

import requests


class ChronopostClient:
    BASE_URL = (
        "https://ws.chronopost.fr/"
        "recherchebt-ws-cxf/"
        "PointRelaisServiceWS/"
        "recherchePointChronopostInter"
    )

    def __init__(
        self,
        account_number: str,
        password: str,
        timeout: int = 30,
    ) -> None:
        self.account_number = account_number
        self.password = password
        self.timeout = timeout

    def search_pickup_points(
        self,
        *,
        address: str | None = None,
        zip_code: str,
        city: str,
        country_code: str = "FR",
        pickup_type: str = "P",
        product_code: str = "86",
        service: str = "L",
        weight: str = "1",
        shipping_date: str,
        max_point_chronopost: str = "10",
        max_distance_search: str = "10",
        holiday_tolerant: str = "1",
        language: str = "FR",
    ) -> str:

        params = {
            "accountNumber": self.account_number,
            "password": self.password,
            "zipCode": zip_code,
            "city": city,
            "countryCode": country_code,
            "type": pickup_type,
            "productCode": product_code,
            "service": service,
            "weight": weight,
            "shippingDate": shipping_date,
            "maxPointChronopost": max_point_chronopost,
            "maxDistanceSearch": max_distance_search,
            "holidayTolerant": holiday_tolerant,
            "language": language,
        }

        if address:
            params["address"] = address

        response = requests.get(
            self.BASE_URL,
            params=params,
            timeout=self.timeout,
        )

        response.raise_for_status()

        return response.text