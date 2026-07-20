from xml.etree import ElementTree


class ChronopostResponseParser:
    @staticmethod
    def extract_pickup_points(
        xml_content: str,
    ) -> list[dict]:
        root = ElementTree.fromstring(
            xml_content
        )

        pickup_points: list[dict] = []

        for point in root.findall(
            ".//{*}listePointRelais"
        ):
            opening_hours = [
                value.text.strip()
                for value in point.findall(
                    ".//{*}horairesAsString"
                )
                if value.text
            ]

            pickup_points.append(
                {
                    "identifiant": point.findtext(
                        "{*}identifiant",
                        default="",
                    ),
                    "nom": point.findtext(
                        "{*}nom",
                        default="",
                    ),
                    "adresse1": point.findtext(
                        "{*}adresse1",
                        default="",
                    ),
                    "adresse2": point.findtext(
                        "{*}adresse2",
                        default="",
                    ),
                    "adresse3": point.findtext(
                        "{*}adresse3",
                        default="",
                    ),
                    "codePostal": point.findtext(
                        "{*}codePostal",
                        default="",
                    ),
                    "localite": point.findtext(
                        "{*}localite",
                        default="",
                    ),
                    "codePays": point.findtext(
                        "{*}codePays",
                        default="",
                    ),
                    "coordGeolocalisationLatitude": point.findtext(
                        "{*}coordGeolocalisationLatitude",
                        default="0",
                    ),
                    "coordGeolocalisationLongitude": point.findtext(
                        "{*}coordGeolocalisationLongitude",
                        default="0",
                    ),
                    "typeDePoint": point.findtext(
                        "{*}typeDePoint",
                        default="P",
                    ),
                    "actif": point.findtext(
                        "{*}actif",
                        default="true",
                    ),
                    "opening_hours": (
                        " | ".join(
                            opening_hours
                        )
                        if opening_hours
                        else None
                    ),
                }
            )

        return pickup_points