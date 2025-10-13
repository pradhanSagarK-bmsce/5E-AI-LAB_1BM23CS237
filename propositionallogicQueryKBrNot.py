from sympy.logic.boolalg import Or, And, Not
from sympy.abc import A, B, C

def generate_truth_assignments(variables):
    
    assignments = []
    n = len(variables)
    for i in range(2 ** n):
        assignment = {}
        for j in range(n):
            assignment[variables[j]] = bool(i & (1 << j))
        assignments.append(assignment)
    return assignments

def evaluate_formula(formula, assignment):
   
    return formula.subs(assignment)

def check_entailment(kb, query):
    
    negated_query = Not(query)
   
    kb_prime = And(*kb)  
    kb_prime_with_neg_query = And(kb_prime, negated_query)
   

    variables = [A, B, C]  
    assignments = generate_truth_assignments(variables)
   
  
    unsatisfiable = True 
    satisfying_assignments = []
   
    for assignment in assignments:
        kb_value = evaluate_formula(kb_prime_with_neg_query, assignment)
       
    
        if kb_value:
            satisfying_assignments.append(assignment)
            unsatisfiable = False
   
  
    print("\nKnowledge Base (KB):")
    for formula in kb:
        print(f"  {formula}")
   
    print("\nNegated Query (¬Q):")
    print(f"  {negated_query}")
   
    if unsatisfiable:
        print("\nKB entails Q because KB' (KB ∪ {¬Q}) is unsatisfiable under all truth assignments.")
        return True
    else:
        print("\nKB does not entail Q because KB' is satisfiable for the following truth assignments:")
        for assignment in satisfying_assignments:
            print(f"  {assignment}")
        return False

def main():
    # Example Knowledge Base KB = {A ∨ B, ¬A ∨ C, B ∨ ¬C}
    kb = [Or(A, B), Or(Not(A), C), Or(B, Not(C))]
   
    # Example Query Q = A ∨ C
    query = Or(A, C)
   
    # Check entailment and print the detailed reason
    result = check_entailment(kb, query)
    print(f"\nEntailment result: {result}")

if __name__ == "__main__":
    main()
