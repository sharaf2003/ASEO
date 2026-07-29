from ai_engine.engineering_brain import (
    EngineeringAnalyzer,
    EngineeringPlanner
)



analyzer = EngineeringAnalyzer()


planner = EngineeringPlanner()



analysis = analyzer.analyze(

    "Build ecommerce platform"

)



plan = planner.create_plan(

    analysis

)



print(

    {

        "analysis":
            analysis,


        "plan":
            plan

    }

)