from app.intelligence.self_improvement.failure_analyzer import (
    FailureAnalyzer
)



def main():


    analyzer = FailureAnalyzer()



    result = analyzer.analyze(

        execution_result={

            "success": False

        },


        architecture_decisions=[

            {

                "id": 1,

                "pattern": "FastAPI",

                "layer": "backend"

            },

            {

                "id": 5,

                "pattern": "React",

                "layer": "frontend"

            }

        ]

    )


    print(result)



if __name__ == "__main__":

    main()