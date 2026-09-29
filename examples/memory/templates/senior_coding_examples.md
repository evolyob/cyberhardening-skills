# Senior Clean Code Radar: Practical Examples

Empirical Before/After case studies for `senior_coding_laws.md`.

---

## 1. Step 1: Own the Boundary & Dict Lookups

> **Action Mandate**: Prohibit string concatenation for file paths. Enforce `Path.resolve()` and `Path.is_relative_to()` to prevent directory traversal. Prohibit nested loops for collection matching; build hash maps for O(1) key lookups.

### Before (Over-engineered dependency)
```python
import pandas as pd

def sum_sales(path: str) -> float:
    df = pd.read_csv(path)
    return float(df["amount"].sum())
```

### After (Standard Library First)
```python
import csv

def sum_sales(path: str) -> float:
    with open(path, newline="", encoding="utf-8") as f:
        return sum(float(row["amount"]) for row in csv.DictReader(f))
```

### Before (Brute-force nested loops O(N^2))
```python
def match_order_items(orders: list[dict], products: list[dict]) -> list[tuple]:
    matched = []
    for order in orders:
        for product in products:
            if order["product_id"] == product["id"]:
                matched.append((order, product))
    return matched
```

### After (Single-pass hash map index O(N))
```python
def match_order_items(orders: list[dict], products: list[dict]) -> list[tuple]:
    product_map = {p["id"]: p for p in products}
    return [
        (order, product_map[order["product_id"]])
        for order in orders
        if order["product_id"] in product_map
    ]
```

### Before (Vulnerable path concatenation)
```python
def read_asset(filename: str) -> str:
    path = f"uploads/{filename}"
    with open(path, encoding="utf-8") as f:
        return f.read()
```

### After (Standard library boundary validation with Path.is_relative_to)
```python
from pathlib import Path

def read_asset(filename: str, *, base_dir: Path = Path("uploads")) -> str:
    base = base_dir.resolve()
    target = (base / filename).resolve()
    if not target.is_relative_to(base):
        raise ValueError(f"Path traversal detected: {filename}")
    return target.read_text(encoding="utf-8")
```

---

## 2. Step 2: Pure Core & Constrained States

> **Action Mandate**: Prohibit loose string status checks; enforce `StrEnum` for valid state representation. Strictly isolate I/O, database writes, and mutable default arguments from calculation logic.

### Before (Mixed side effects & mutable defaults)
```python
def process_orders(orders: list, status_log: list = []) -> list:
    for order in orders:
        if order["status"] == "ok":
            status_log.append(order["id"])
            db.update_order(order["id"])  # Inline side effect inside pure calculation
    return status_log
```

### After (Pure functional core & strict enum)
```python
from enum import StrEnum

class OrderStatus(StrEnum):
    PENDING = "pending"
    COMPLETED = "completed"

def filter_completed_order_ids(orders: list[dict]) -> list[str]:
    return [o["id"] for o in orders if o.get("status") == OrderStatus.COMPLETED]
```

---

## 3. Step 3: Flattened Flow & Keyword-Only Arguments

> **Action Mandate**: Use Guard Clauses for early returns to keep happy paths flat (nesting depth <= 2). Enforce keyword-only arguments (`*`) for boolean switches and optional configuration flags to eliminate boolean blindness.

### Before (Deep nesting & boolean blindness)
```python
def dispatch_task(task: dict, force: bool):
    if task:
        if task.get("ready"):
            if force or task.get("priority") > 10:
                execute(task)
```

### After (Guard clauses & keyword-only flags)
```python
def dispatch_task(task: dict | None, *, force: bool = False) -> None:
    if not task or not task.get("ready"):
        return
    if not (force or task.get("priority", 0) > 10):
        return
    execute(task)
```

---

## 4. Step 4: Useful Errors & Context Chaining

> **Action Mandate**: Enforce exception chaining (`raise DomainError(...) from err`) when re-raising lower-level exceptions to retain the causal trace. Never use bare `except:` or silent `pass` blocks.

### Before (Silent swallowing or uninformative generic exception)
```python
try:
    data = load_remote_config(url)
except Exception:
    pass  # Silently swallows error
```

### After (Explicit domain exception with causality chaining)
```python
try:
    data = load_remote_config(url)
except urllib.error.URLError as err:
    raise ConfigLoadError(f"Failed to fetch config from {url}") from err
```

---

## 5. Step 5: Delete-List & Subtractive Engineering

> **Action Mandate**: Invoke native standard library functions directly. Reject single-caller wrapper classes or trivial factory layers. Optimize every diff for net-negative line counts (Deletions > Additions).

### Before (Sprawling wrapper layers)
```python
class TextSanitizerFactory:
    def create_sanitizer(self): ...
class TextSanitizerWrapper:
    def sanitize(self, text): ...
```

### After (Direct root invocation: net negative lines)
```python
def sanitize_text(text: str) -> str:
    return text.strip().replace("\r\n", "\n")
```
