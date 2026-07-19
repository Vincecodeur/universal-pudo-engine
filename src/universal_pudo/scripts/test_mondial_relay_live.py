from pprint import pprint
from pathlib import Path
from universal_pudo.providers.mondial_relay.client import (
    MondialRelayClient,
)
from universal_pudo.providers.mondial_relay.response_parser import (
    MondialRelayResponseParser,
)
from universal_pudo.providers.mondial_relay.mapper import (
    MondialRelayMapper,
)

client = MondialRelayClient(
    enseigne="CC234C1G",
    private_key="DvH8PLS5",
)

xml_response = client.search_pickup_points(
    country_code="FR",
    postal_code="92130",
    city="ISSY LES MOULINEAUX",
)

Path(
    "tests/data/mondial_relay/point_relais_recherche_response.xml"
).write_text(
    xml_response,
    encoding="utf-8",
)


xml_response = client.search_pickup_points(
    country_code="FR",
    postal_code="92130",
    city="ISSY LES MOULINEAUX",
)


pickup_points = (
    MondialRelayResponseParser.extract_pickup_points(
        xml_response
    )
)

print(f"Found {len(pickup_points)} pickup points")

if pickup_points:
    pickup_point = (
        MondialRelayMapper.to_pickup_point(
            pickup_points[0]
        )
    )

    pprint(vars(pickup_point))
    

