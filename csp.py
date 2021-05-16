from typing import Generic, TypeVar, Dict, List, Optional
from abc import ABC, abstractmethod

V = TypeVar('V')
D = TypeVar('D')

# Base class for all constraints
class Constraint(Generic[V, D], ABC):
    # The variables that the constraint is between
    def __init__(self, variables: List[V]) -> None:
        self.variables = variables
    
    # Must be overridden by subclasses
    @abstractmethod
    def satisfied(self, assignment: Dict[V, D]) -> bool:
        ...

class CSP(Generic[V, D]):
    def __init__(self, variables: List[V], domains: Dict[V, D]) -> None:
        self.variables: List[V]= variables
        self.domains: Dict[V, List[D]] = domains
        self.constraints: Dict[V, List[Constraint[V, D]]] = {}
        for variable in self.variables:
            self.constraints[variable] = []
            if variable not in self.domains:
                raise LookupError("Every variable must have an associated domain")

    def add_constraint(self, constraint: Constraint[V, D]):
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError("Variable in constraint not present in CSP")
            else:
                self.constraints[variable].append(constraint)

    def is_consistent(self, variable: V, assignment: Dict[V, D]) -> bool:
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True

    def backtracking_search(self, assignment: Dict[V, D]= {}) -> Optional[Dict[V, D]]:
        # return if we found an assignment for every variable in the CSP
        if len(self.variables) == len(assignment):
            return assignment
        
        unassigned: List[V] = [v for v in self.variables if v not in assignment]
        first: V = unassigned[0]
        for value in self.domains[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value
            if self.is_consistent(first, local_assignment):
                result: Optional[Dict[V, D]] = self.backtracking_search(local_assignment)
                if result is not None:
                    return result
        return None
            