class MemoryConsolidationEngine:


    """
    Combines similar memories
    into stronger knowledge patterns
    """



    def clamp(

        self,

        value: float

    ):

        return max(

            0,

            min(

                value,

                1

            )

        )



    def weighted_average(

        self,

        items: list,

        field: str

    ):


        values = []



        total_weight = 0



        for item in items:


            value = item.get(

                field

            )


            usage = item.get(

                "usage_count",

                0

            )



            if value is None:

                continue



            if usage <= 0:

                usage = 1



            values.append(

                value * usage

            )


            total_weight += usage



        if total_weight == 0:

            return 0



        return self.clamp(

            sum(values) / total_weight

        )



    def consolidate(

        self,

        memories: list

    ) -> list:


        groups = {}



        for memory in memories:


            architecture = memory.get(

                "architecture",

                {}

            )



            if not architecture:

                continue



            key = self.create_signature(

                architecture

            )



            if not key:

                continue



            if key not in groups:

                groups[key] = []



            groups[key].append(

                memory

            )



        consolidated = []



        for key, items in groups.items():


            if not items:

                continue



            total_usage = sum(

                item.get(

                    "usage_count",

                    0

                )

                for item in items

            )



            average_success = round(

                self.weighted_average(

                    items,

                    "success_score"

                ),

                2

            )



            average_confidence = round(

                self.weighted_average(

                    items,

                    "confidence"

                ),

                2

            )



            average_adaptive_score = round(

                self.weighted_average(

                    items,

                    "adaptive_decision_score"

                ),

                2

            )



            average_memory_score = round(

                self.weighted_average(

                    items,

                    "memory_score"

                ),

                2

            )



            consolidated.append({


                "architecture": items[0].get(

                    "architecture",

                    {}

                ),


                "total_usage": total_usage,


                "average_success": average_success,


                "average_confidence": average_confidence,


                "average_adaptive_score": average_adaptive_score,


                "average_memory_score": average_memory_score,


                "memory_count": len(items),


                "signature": key


            })



        return consolidated





    def create_signature(

        self,

        architecture: dict

    ) -> str:



        values = []



        for layer, data in architecture.items():


            if isinstance(data, dict):


                for value in data.values():


                    if value and str(value).lower() != "null":


                        values.append(

                            str(value)

                            .lower()

                            .strip()

                        )



        return "|".join(

            sorted(values)

        )