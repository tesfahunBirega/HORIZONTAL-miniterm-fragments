from typing import List

class MinitermGenerator:
    def __init__(self, predicates: List[str]):
        self.predicates = predicates

    def generate_miniterms(self) -> List[str]:
        miniterms = []
        for predicate in self.predicates:
            miniterms.extend(self._split_predicate(predicate))
        return miniterms

    def _split_predicate(self, predicate: str) -> List[str]:
        parts = predicate.split("AND")
        miniterms = []
        for part in parts:
            part = part.strip()
            if "OR" in part:
                miniterms.extend(part.split("OR"))
            else:
                miniterms.append(part)
        return miniterms

# Example usage:
predicates = ["A AND B OR C", "D AND E AND F OR G"]
miniterm_generator = MinitermGenerator(predicates)
miniterms = miniterm_generator.generate_miniterms()
print(miniterms)
