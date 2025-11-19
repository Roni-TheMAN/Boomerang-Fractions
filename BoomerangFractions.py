from collections import deque
from fractions import Fraction

def best_boomerang_path(m, n, *, max_steps=30, den_limit=5000, value_limit=10**6):
    """
    Find the shortest sequence of moves starting at 1 that returns to 1,
    given the rule: first move must be + m/n, then each step is either + m/n or reciprocal.

    Returns:
        list of (value_after_move, op) from the start, including the first +r step,
        ending with value 1; or None if no path found under the limits.
    """
    r = Fraction(m, n)
    ONE = Fraction(1, 1)
    first = ONE + r
    if first == ONE:
        return [(ONE, "+r")]  # degenerate case r==0

    # BFS setup
    q = deque([first])
    parents = {first: (ONE, "+r")}     # child -> (parent_value, op_taken_to_get_child)
    depth = {first: 1}

    def ok(z: Fraction) -> bool:
        # pruning guardrails: cap denominator size and numeric magnitude
        return (z.denominator <= den_limit) and (abs(z.numerator) <= value_limit)

    def neighbors(x: Fraction):
        yield (x + r, "+r")
        yield (Fraction(1, 1) / x, "inv")  # reciprocal

    # Special-case: if the very first step already returns by a reciprocal
    if first == ONE:
        return [(first, "+r")]

    # We also allow hitting ONE during expansion to terminate early
    visited = {ONE, first}

    while q:
        x = q.popleft()
        if depth[x] >= max_steps:
            continue

        for nxt, op in neighbors(x):
            if not ok(nxt):
                continue
            if nxt not in parents:
                parents[nxt] = (x, op)
                depth[nxt] = depth[x] + 1
                if nxt == ONE:
                    # reconstruct path
                    path = []
                    cur = nxt
                    while cur != ONE or not path:  # ensure we include the first step
                        prev, op_used = parents[cur]
                        path.append((cur, op_used))
                        cur = prev
                        if cur == ONE and prev == ONE:
                            break
                    path.reverse()
                    return path  # sequence from first move to 1
                q.append(nxt)

    return None


# Example: r = 1/2
path = best_boomerang_path(1, 11, max_steps=2000, den_limit=5000)
if path is None:
    print("No path found within limits.")
else:
    cur = Fraction(1, 1)
    print("Start:", cur)
    for val, op in path:
        print(f"{op:>4} -> {val}")
