from app.online.models import Query, QueryIntent


class QueryAnalyzer:

    def analyze(
        self,
        query: Query
    ) -> Query:

        text = query.query.lower()

        # ------------------------
        # Intent Detection
        # ------------------------

        if "procedure" in text or "steps" in text:

            query.intent = QueryIntent.PROCEDURE

        elif "troubleshoot" in text or "failure" in text:

            query.intent = QueryIntent.TROUBLESHOOTING

        elif "compare" in text:

            query.intent = QueryIntent.COMPARISON

        elif "summary" in text:

            query.intent = QueryIntent.SUMMARY

        else:

            query.intent = QueryIntent.QA

        # ------------------------
        # Entity Detection
        # ------------------------

        entities = []

        equipment = [

            "Steam Drum",

            "Boiler",

            "Economizer",

            "Boiler Feed Pump",

            "Superheater"
        ]

        for item in equipment:

            if item.lower() in text:

                entities.append(item)

        query.entities = entities

        return query