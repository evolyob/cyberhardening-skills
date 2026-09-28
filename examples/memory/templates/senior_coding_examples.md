# Senior Clean Code Radar: Practical Examples

Empirical Before/After case studies for `senior_coding_laws.md`.

---

## 1. Step 1: 禁用字串拼接路徑，強制標準庫邊界與字典索引 (Own the Boundary & Dict Lookups)

> **行動守則**：禁止使用字串拼接檔案路徑，強制呼叫 Path.resolve() 與 Path.is_relative_to() 封死目錄穿越邊界；集合比對禁止使用雙重迴圈，強制以字典鍵值建立索引。

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

## 2. Step 2: 封死模糊狀態，消除純計算副作用 (Pure Core & Constrained States)

> **行動守則**：停用鬆散字串比對，全面改用 StrEnum 限定合法值；計算函式內嚴禁穿插 I/O、資料庫寫入或可變預設參數。

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

## 3. Step 3: 提早 Return 攤平巢狀，強制關鍵字參數 (Flattened Flow & Keyword-Only Arguments)

> **行動守則**：使用 Guard Clauses 提早 return，巢狀結構深度不得超過兩層；布林切換與選用設定強制使用關鍵字參數（*）以消除布林盲點。

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

## 4. Step 4: 異常必須連坐，嚴禁靜默吞沒 (Useful Errors & Context Chaining)

> **行動守則**：捕獲例外時強制使用 raise ... from err 保留因果追溯鏈；嚴禁使用 bare except 或 pass 靜默吞沒錯誤。

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

## 5. Step 5: 拔除無效封裝，追求負淨行數 (Delete-List & Subtractive Engineering)

> **行動守則**：直接呼叫原生函式，拒絕僅具備單一轉發功能的 Factory 或 Wrapper 類別；每次變更以刪除行數大於新增行數為原則。

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
