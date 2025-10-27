from itertools import combinations


def negate(literal):
    return literal[1:] if literal.startswith('~') else '~' + literal


def resolve(ci, cj):
    resolvents = []
    for li in ci:
        for lj in cj:
            if li == negate(lj):
                
                new_clause = set(ci.union(cj))
                new_clause.discard(li)
                new_clause.discard(lj)
                resolvents.append(new_clause)
    return resolvents

# Main entailment function
def wumpus_resolution_entailment(KB, query):
    # 1. Negate the query and add to KB
    negated_query = negate(query)
    clauses = KB + [{negated_query}]
    new = set()

    print(f"\nInitial clauses (KB ∪ ¬Q):")
    for c in clauses:
        print(c)

    # 2. Resolution loop
    while True:
        pairs = list(combinations(clauses, 2))
        for (ci, cj) in pairs:
            resolvents = resolve(ci, cj)
            for r in resolvents:
                if not r:  # Empty clause derived
                    print("\nDerived empty clause □ — entailment proven.")
                    return True
                new.add(frozenset(r))
        # Stop if no new information
        new_clauses = new.difference(map(frozenset, clauses))
        if not new_clauses:
            print("\nNo new clauses can be derived — entailment failed.")
            return False
        for c in new_clauses:
            clauses.append(set(c))
            print("Added new clause:", set(c))


if __name__ == "__main__":

    # Knowledge Base (in CNF)
    KB = []


    KB.append({'B11', '~P12'})
    KB.append({'B11', '~P21'})

    KB.append({'~B11'})

   
    KB.append({'~P11'})

    # Query: ¬P21  (is cell (2,1) safe?)
    query = '~P21'

    print("\n=== WUMPUS RESOLUTION ENTAILMENT ===")
    result = wumpus_resolution_entailment(KB, query)

    print("\nResult:")
    if result:
        print("✅ KB ⊨", query, "→ Cell (2,1) is safe.")
    else:
        print("❌ KB ⊭", query, "→ Cannot conclude safety.")

