# Boomerang Fractions Solver

This little tool searches for **“boomerang paths”** on rational numbers.

You start at the value **1**, pick a rational step  

\[
r = \frac{m}{n},
\]

and are allowed to repeatedly apply exactly **two operations**:

1. **Add** \( r \): \( x \mapsto x + r \)  (labelled `"+r"`)
2. **Reciprocate**: \( x \mapsto \dfrac{1}{x} \)  (labelled `"inv"`)

A **boomerang path** is a finite sequence of these moves that:

- starts at **1**,  
- first move is **always** `+ r`,  
- and eventually returns **back to 1**.

This code uses BFS to find the **shortest** such path (if it exists within the given limits).

---

## Function Overview

```python
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
    ...
