from .agent_score import AgentScore




class AgentEvaluator:
    """
    ASEO Agent Evaluation Engine v14
    """



    def __init__(self):

        self.scores = {}





    def evaluate(
        self,
        agent,
        success,
        quality_score=100
    ):


        if agent not in self.scores:


            self.scores[agent] = AgentScore(

                agent

            )



        score = self.scores[agent]



        score.executions += 1



        if success:

            score.successful += 1


        else:

            score.failed += 1




        score.quality_score = quality_score



        return score.to_dict()





    def report(self):


        return {


            name:

                score.to_dict()


            for name, score

            in self.scores.items()

        }