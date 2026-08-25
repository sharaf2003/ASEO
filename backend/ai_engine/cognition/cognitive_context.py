class CognitiveContext:

    def __init__(self, requirement=None):
        self.requirement = requirement
        self.domain = None
        self.entities = []
        self.constraints = []
        self.patterns = []
        self.evidence = []
        self.reasoning = []
        self.decision = None
        self.confidence = 0.0

    def add_evidence(self, evidence):
        self.evidence.append(evidence)