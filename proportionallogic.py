import itertools

def parse_expr(expr):
    expr = expr.replace("=>", " <= ")
    expr = expr.replace("<=", " == ")
    expr = expr.replace("<=>", " == ")
    expr = expr.replace("~", " not ")
    expr = expr.replace("&", " and ")
    expr = expr.replace("|", " or ")
    return expr

def evaluate(expr, values):
    local_dict = {var: val for var, val in values.items()}
    return eval(expr, {}, local_dict)

expr = input("Enter propositional logic formula (use ~, &, |, =>, <=>): ").strip()

vars_in_expr = sorted(set([ch for ch in expr if ch.isalpha()]))

if not vars_in_expr:
    print("No propositional variables found!")
    exit()

expr_parsed = parse_expr(expr)

print(f"\nVariables: {vars_in_expr}")
print("\nTruth Table:")
print("-" * (len(vars_in_expr) * 8 + 10))
print(" | ".join(vars_in_expr) + " | Result")
print("-" * (len(vars_in_expr) * 8 + 10))

results = []
for values in itertools.product([False, True], repeat=len(vars_in_expr)):
    assignment = dict(zip(vars_in_expr, values))
    result = evaluate(expr_parsed, assignment)
    results.append(result)
    vals = ["T" if v else "F" for v in values]
    print(" | ".join(vals) + f" |   {'T' if result else 'F'}")

print("-" * (len(vars_in_expr) * 8 + 10))

# Analyze final result
if all(results):
    print("\n The formula is a TAUTOLOGY (always true).")
elif not any(results):
    print("\nThe formula is a CONTRADICTION (always false).")
else:
    print("\n  The formula is SATISFIABLE (true for some values).")
