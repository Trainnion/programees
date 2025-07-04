from itertools import combinations

def count_ones(binary):
    return binary.count('1')

def combine_terms(term1, term2):
    combined = ''
    differences = 0
    for a, b in zip(term1, term2):
        if a == b:
            combined += a
        else:
            combined += '-'
            differences += 1
    return combined if differences == 1 else None

def is_covered(term, minterm):
    minterm_bin = format(minterm, f'0{len(term)}b')
    return all(t == m or t == '-' for t, m in zip(term, minterm_bin))

def get_prime_implicants(minterms, num_vars):
    terms = [format(m, f'0{num_vars}b') for m in minterms]
    unchecked = set(terms)
    checked = set()
    next_terms = set()
    
    while unchecked:
        grouped = {}
        for term in unchecked:
            ones = count_ones(term)
            grouped.setdefault(ones, []).append(term)

        used = set()
        for i in sorted(grouped):
            if i+1 not in grouped: continue
            for a in grouped[i]:
                for b in grouped[i+1]:
                    combined = combine_terms(a, b)
                    if combined:
                        next_terms.add(combined)
                        used.add(a)
                        used.add(b)

        checked |= (unchecked - used)
        unchecked = next_terms
        next_terms = set()

    return checked

def get_essential_prime_implicants(prime_implicants, minterms, num_vars):
    chart = {m: [] for m in minterms}
    for imp in prime_implicants:
        for m in minterms:
            if is_covered(imp, m):
                chart[m].append(imp)

    essential = set()
    for m, imps in chart.items():
        if len(imps) == 1:
            essential.add(imps[0])

    covered = set()
    for imp in essential:
        for m in minterms:
            if is_covered(imp, m):
                covered.add(m)

    remaining_minterms = [m for m in minterms if m not in covered]
    remaining_imps = set(prime_implicants) - essential

    while remaining_minterms:
        counts = {imp: 0 for imp in remaining_imps}
        for m in remaining_minterms:
            for imp in remaining_imps:
                if is_covered(imp, m):
                    counts[imp] += 1
        best = max(counts, key=counts.get)
        essential.add(best)
        for m in minterms:
            if is_covered(best, m) and m in remaining_minterms:
                remaining_minterms.remove(m)

    return essential

def boolean_expression(term):
    variables = ['A', 'B', 'C', 'D', 'E']  # 5 variables
    expr = ''
    for i, val in enumerate(term):
        if val == '1':
            expr += variables[i]
        elif val == '0':
            expr += variables[i] + "'"
    return expr or '1'

def quine_mccluskey(minterms, num_vars):
    print("\nStep 1: Getting Prime Implicants...")
    prime_implicants = get_prime_implicants(minterms, num_vars)
    for p in sorted(prime_implicants):
        print("  ", p)

    print("\nStep 2: Getting Essential Prime Implicants...")
    essential = get_essential_prime_implicants(prime_implicants, minterms, num_vars)
    for e in sorted(essential):
        print("  ", e, "->", boolean_expression(e))

    print("\n✅ Final Minimized Boolean Expression:")
    minimized = ' + '.join(boolean_expression(e) for e in sorted(essential))
    print("  ", minimized)
    return minimized

# ---------------------
# ✅ MAIN PROGRAM START
# ---------------------

def main():
    print("🔧 Quine–McCluskey Boolean Minimizer (5 Variables Max, Minterms 0–31)")
    num_vars = 5  # Fixed to 5 variables

    try:
        minterm_input = input("Enter space-separated minterms (0–31): ")
        minterms = list(map(int, minterm_input.strip().split()))

        if any(m < 0 or m > 31 for m in minterms):
            print("❌ Error: All minterms must be between 0 and 31.")
            return

        quine_mccluskey(minterms, num_vars)

    except ValueError:
        print("❌ Invalid input. Please enter integers separated by spaces.")


main()
