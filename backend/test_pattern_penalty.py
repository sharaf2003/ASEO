from app.intelligence.self_improvement.pattern_penalty import (
    PatternPenaltyEngine
)



def main():


    engine = PatternPenaltyEngine()



    result = engine.calculate_penalty(

        current_score=0.55,

        failure_count=2

    )


    print(result)



if __name__ == "__main__":

    main()