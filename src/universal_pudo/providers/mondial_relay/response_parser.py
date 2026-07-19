from xml.etree import ElementTree


class MondialRelayResponseParser:
    @staticmethod
    def extract_pickup_points(
        xml_content: str,

    ) -> list[dict]:
        root = ElementTree.fromstring(
            xml_content
        )

        pickup_points: list[dict] = []

        for point in root.findall(
            ".//{*}PointRelais_Details"
        ):

            pickup_points.append(
                {
                    "Num": point.findtext(
                        "{*}Num",
                        default="",
                    ),
                    "LgAdr1": point.findtext(
                        "{*}LgAdr1",
                        default="",
                    ),
                    "LgAdr2": point.findtext(
                        "{*}LgAdr2",
                        default="",
                    ),
                    "LgAdr3": point.findtext(
                        "{*}LgAdr3",
                        default="",
                    ),
                    "LgAdr4": point.findtext(
                        "{*}LgAdr4",
                        default="",
                    ),
                    "CP": point.findtext(
                        "{*}CP",
                        default="",
                    ),
                    "Ville": point.findtext(
                        "{*}Ville",
                        default="",
                    ),
                    "Pays": point.findtext(
                        "{*}Pays",
                        default="",
                    ),
                    "Latitude": point.findtext(
                        "{*}Latitude",
                        default="",
                    ),
                    "Longitude": point.findtext(
                        "{*}Longitude",
                        default="",
                    ),
                    "TypeActivite": point.findtext(
                        "{*}TypeActivite",
                        default="",
                    ),
                    "Distance": point.findtext(
                        "{*}Distance",
                        default="",
                    ),
                }
            )

        return pickup_points