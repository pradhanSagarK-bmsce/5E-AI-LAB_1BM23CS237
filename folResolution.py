def remove_implications(expr):
    
    if "->" in expr:
        A, B = expr.split("->")
        A = A.strip()
        B = B.strip()
        return f"~{A} v {B}"
    return expr

def to_cnf(expr):
   
    return [expr.replace(" ", "")]
    
def parse_clause(clause):
    return set(clause.split("v"))

def negate_literal(lit):
    return lit[1:] if lit.startswith("~") else "~" + lit

def resolve(ci, cj):
    resolvents = []

    for lit in ci:
        neg = negate_literal(lit)
        if neg in cj:
            new_clause = (ci - {lit}) | (cj - {neg})
            if len(new_clause) == 0:
                resolvents.append("□")
            else:
                resolvents.append("v".join(new_clause))
    return resolvents




def resolution(KB, query):
    print("Knowledge Base:", KB)
    print("Query:", query)

    neg_query = negate_literal(query)
    print("Negated Query:", neg_query)

    clauses = []

    # Convert KB to CNF
    for rule in KB:
        rule_no_imp = remove_implications(rule)
        clauses += to_cnf(rule_no_imp)

    # Add negated query
    clauses += to_cnf(neg_query)

    print("\nCNF Clauses:")
    for c in clauses:
        print("  ", c)

    # Convert to sets
    clauses = [parse_clause(c) for c in clauses]

    print("\nStarting Resolution...\n")

    new = set()

    while True:
        n = len(clauses)
        for i in range(n):
            for j in range(i+1, n):
                resolvents = resolve(clauses[i], clauses[j])

                for r in resolvents:
                    if r == "□":
                        print("Derived empty clause (□)")
                        print("✔ QUERY PROVEN")
                        return True
                    if r not in new:
                        new.add(r)

        if not new:
            print("No new clauses can be produced.")
            print("✘ QUERY NOT PROVEN")
            return False

        # Add new clauses
        for c in new:
            clauses.append(parse_clause(c))
        new.clear()




KB = [
    "P -> Q",
    "Q -> R",
    "P"
]

query = "Q"

resolution(KB, query)
