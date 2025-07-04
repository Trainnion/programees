import itertools

def gray_code(n):
    if n == 0:
        return ['']
    first_half = gray_code(n - 1)
    second_half = first_half[::-1]
    return ['0' + code for code in first_half] + ['1' + code for code in second_half]

def get_kmap_grid(num_vars):
    if num_vars == 2:
        return gray_code(1), gray_code(1)
    elif num_vars == 3:
        return gray_code(1), gray_code(2)
    elif num_vars == 4:
        return gray_code(2), gray_code(2)
    elif num_vars == 5:
        return gray_code(2), gray_code(3)
    else:
        raise ValueError("Only 2 to 5 variables are supported")

def print_kmap(minterms, num_vars):
    if num_vars < 5:
        # Standard K-map
        rows, cols = get_kmap_grid(num_vars)
        print(f"\n{num_vars}-Variable K-Map")
        print("     " + "  ".join(cols))
        print("   +" + "---"*len(cols) + "+")

        for r, row_bits in enumerate(rows):
            row_str = f"{row_bits} |"
            for c, col_bits in enumerate(cols):
                bin_input = row_bits + col_bits
                dec = int(bin_input, 2)
                row_str += " " + ('1' if dec in minterms else '0') + " "
            row_str += "|"
            print(row_str)
        print("   +" + "---"*len(cols) + "+")

    elif num_vars == 5:
        # 5-variable: Two 4x4 maps (A=0 and A=1)
        print("\n5-Variable K-Map (Split into 2 maps of 4x4 for A=0 and A=1)")
        row_labels = gray_code(2)  # B C
        col_labels = gray_code(2)  # D E

        for a_val in [0, 1]:
            print(f"\nA = {a_val}")
            print("      " + "   ".join(col_labels))
            print("    +" + "----" * len(col_labels) + "+")

            for r in row_labels:
                row_str = f"{r} |"
                for c in col_labels:
                    full_bits = str(a_val) + r + c  # ABCDE
                    dec = int(full_bits, 2)
                    row_str += " " + ('1' if dec in minterms else '0') + "  "
                row_str += "|"
                print(row_str)
            print("    +" + "----" * len(col_labels) + "+")


def combine_terms(term1, term2):
    result = ""
    diff_count = 0
    for a, b in zip(term1, term2):
        if a != b:
            result += '-'
            diff_count += 1
        else:
            result += a
    return result if diff_count == 1 else None

def get_prime_implicants(minterms, num_vars):
    terms = [format(m, f'0{num_vars}b') for m in minterms]
    unchecked = set(terms)
    prime_implicants = set()

    while unchecked:
        next_round = set()
        checked = set()
        pairs = set()
        for a in unchecked:
            for b in unchecked:
                if a == b:
                    continue
                combined = combine_terms(a, b)
                if combined:
                    pairs.add(combined)
                    checked.add(a)
                    checked.add(b)
        prime_implicants.update(unchecked - checked)
        unchecked = pairs
    prime_implicants.update(unchecked)
    return prime_implicants

def term_covers(term, minterm):
    for t_bit, m_bit in zip(term, format(minterm, f'0{len(term)}b')):
        if t_bit != '-' and t_bit != m_bit:
            return False
    return True



def simplify(minterms, num_vars):
    terms = [format(m, f'0{num_vars}b') for m in minterms]
    unchecked = set(terms)
    prime_implicants = set()

    while unchecked:
        next_round = set()
        checked = set()
        pairs = set()

        for a in unchecked:
            for b in unchecked:
                if a >= b:
                    continue
                combined = combine_terms(a, b)
                if combined:
                    pairs.add(combined)
                    checked.add(a)
                    checked.add(b)

        unused = unchecked - checked
        prime_implicants.update(unused)
        unchecked = pairs

    prime_implicants.update(unchecked)

    # Prime implicant chart (internal only)
    chart = {m: [] for m in minterms}
    for pi in prime_implicants:
        for m in minterms:
            if term_covers(pi, m):
                chart[m].append(pi)

    # Step 1: Find essential prime implicants
    essential = set()
    covered = set()
    for m, implicants in chart.items():
        if len(implicants) == 1:
            pi = implicants[0]
            essential.add(pi)
            for k in minterms:
                if term_covers(pi, k):
                    covered.add(k)

    # Step 2: Cover remaining minterms greedily
    uncovered = set(minterms) - covered
    selected = set()
    while uncovered:
        best_pi = None
        best_coverage = 0
        for pi in prime_implicants - essential - selected:
            covers = {m for m in uncovered if term_covers(pi, m)}
            if len(covers) > best_coverage:
                best_pi = pi
                best_coverage = len(covers)
        if best_pi is None:
            break
        selected.add(best_pi)
        uncovered -= {m for m in minterms if term_covers(best_pi, m)}

    return essential.union(selected)

    
    terms = [format(m, f'0{num_vars}b') for m in minterms]
    unchecked = set(terms)
    prime_implicants = set()

    while unchecked:
        next_round = set()
        checked = set()
        pairs = set()

        for a in unchecked:
            for b in unchecked:
                if a >= b:
                    continue
                combined = combine_terms(a, b)
                if combined:
                    pairs.add(combined)
                    checked.add(a)
                    checked.add(b)

        unused = unchecked - checked
        prime_implicants.update(unused)
        unchecked = pairs

    prime_implicants.update(unchecked)

    # Build prime implicant chart (not printed)
    chart = {m: [] for m in minterms}
    for pi in prime_implicants:
        for m in minterms:
            if term_covers(pi, m):
                chart[m].append(pi)

    # Identify and show only essential prime implicants
    print("\nIdentifying Essential Prime Implicants:")
    essential = set()
    while chart:
        found_essential = False
        for m, implicants in list(chart.items()):
            if len(implicants) == 1:
                pi = implicants[0]
                print(f" → {pi} covers minterm {m}")
                essential.add(pi)
                for k in list(chart.keys()):
                    if term_covers(pi, k):
                        del chart[k]
                found_essential = True
                break
        if not found_essential:
            break

    return essential

def term_to_expr(term, var_names):
    parts = []
    for i, bit in enumerate(term):
        if bit == '1':
            parts.append(var_names[i])
        elif bit == '0':
            parts.append(var_names[i] + "'")
    return " ".join(parts) if parts else "1"

def main():
    print("Karnaugh Map Simplifier (2 to 5 variables)")
    try:
        num_vars = int(input("Enter number of variables (2 to 5): "))
        if not 2 <= num_vars <= 5:
            raise ValueError("Variable count must be between 2 and 5.")

        max_minterm = 2 ** num_vars - 1
        raw_input_data = input(f"Enter space-separated minterms (0 to {max_minterm}): ")
        minterms = list(map(int, raw_input_data.strip().split()))

        if not minterms:
            print("No minterms entered.")
            return
        for m in minterms:
            if not 0 <= m <= max_minterm:
                raise ValueError(f"Invalid minterm: {m}")

        print_kmap(minterms, num_vars)
        essentials = simplify(minterms, num_vars)
        var_names = ['A', 'B', 'C', 'D', 'E'][:num_vars]
        expression = ' + '.join(term_to_expr(term, var_names) for term in essentials)
        print("\nSimplified Boolean Expression (space-separated terms):")
        print("F =", expression if expression else "0")

    except Exception as e:
        print("Error:", e)


main()
