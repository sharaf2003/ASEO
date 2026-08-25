class EvidenceFusion:


    def combine(self, context):

        total_weight = 0
        count = 0


        for evidence in context.evidence:

            weight = evidence.get(
                "weight",
                0
            )

            total_weight += weight
            count += 1



        if count > 0:

            context.confidence = (
                total_weight / count
            )


        return context