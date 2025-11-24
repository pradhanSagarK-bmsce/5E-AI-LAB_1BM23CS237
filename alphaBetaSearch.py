INF = 10**9  # numeric infinity

def alpha_beta(node, maximizing, alpha, beta, tree):
    def val_str(v):
        if v >= INF:
            return "INF"
        elif v <= -INF:
            return "-INF"
        else:
            return str(v)

    print(f"\nVisiting {node}, α={val_str(alpha)}, β={val_str(beta)}")
    if node not in tree:  # Leaf
        print(f"Leaf value: {node}")
        return node

    if maximizing:
        value = -INF
        for child in tree[node]:
            val = alpha_beta(child, False, alpha, beta, tree)
            value = max(value, val)
            alpha = max(alpha, value)
            print(f"Max node {node}, value={value}, α={val_str(alpha)}, β={val_str(beta)}")
            if alpha >= beta:
                print("Prune!")
                break
        return value
    else:
        value = INF
        for child in tree[node]:
            val = alpha_beta(child, True, alpha, beta, tree)
            value = min(value, val)
            beta = min(beta, value)
            print(f"Min node {node}, value={value}, α={val_str(alpha)}, β={val_str(beta)}")
            if alpha >= beta:
                print("Prune!")
                break
        return value

# Example tree
tree = {"A":["B","C"], "B":[3,5,6], "C":[9,1,2]}

print("\nAlpha–Beta Pruning Result:", alpha_beta("A", True, -INF, INF, tree))
