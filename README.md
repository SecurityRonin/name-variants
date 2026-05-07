# name-variants

Multilingual name romanization lookup tables for NLP, entity resolution, and document processing.

Maps native script forms to all known romanization variants so that `陳 / Chen / Chan / Tan`,
`박 / Park / Bak`, `Nguyễn / Nguyen`, and `محمد / Muhammad / Mohammed` are treated as the same entity.

## Languages

| Script | Coverage | Example |
|--------|----------|---------|
| Chinese (Han) | 200+ surnames | `陈 → Chen / Chan / Tan / Chin` |
| Arabic | 100+ given names | `محمد → Muhammad / Mohammed / Mohamed` |
| Japanese | 150+ surnames | `田中 → Tanaka` |
| Korean | 100+ surnames | `박 → Park / Bak / Pak` |
| Vietnamese | 80+ surnames + given | `Nguyễn → Nguyen` |
| Hindi/North Indian | 80+ names | `शर्मा → Sharma / Sarma` |
| Tamil | 60+ names | `சுப்பிரமணியம் → Subramaniam / Subramanian` |
| Bengali | 60+ names | `চট্টোপাধ্যায় → Chattopadhyay / Chatterjee` |
| Persian/Farsi | 80+ names | `حسین → Hossein / Hussein` |
| Hebrew | 80+ names | `יצחק → Yitzhak / Isaac` |
| Thai | 80+ names | `ประยุทธ์ → Prayuth / Prayut` |
| Greek | 70+ names | `Κωνσταντίνος → Konstantinos / Constantine` |
| Turkish | 70+ names | `Çelik → Celik` |
| Russian/Slavic | 80+ names | `Иванов → Ivanov / Ivanoff` |
| Indonesian/Malay | 60+ names | `Suharto → Soeharto` |

## Usage

```python
from name_variants import lookup_key

lookup_key("Chan")      # → "陈"
lookup_key("陳")        # → "陈"
lookup_key("Tan")       # → "陈"
lookup_key("Xu")        # → "许"
lookup_key("Park")      # → "박"
lookup_key("Bak")       # → "박"
lookup_key("Nguyen")    # → "nguyễn"
lookup_key("Muhammad")  # → "محمد"
lookup_key("Mohammed")  # → "محمد"
lookup_key("Unknown")   # → None  (not in any table)
```

### Checking if two names are variants of each other

```python
def same_person(a: str, b: str) -> bool:
    ka, kb = lookup_key(a), lookup_key(b)
    if ka is not None and kb is not None:
        return ka == kb
    # Fall back to fuzzy matching for unknown names
    from rapidfuzz import fuzz
    return fuzz.ratio(a.lower(), b.lower()) >= 85
```

### Getting all known variants

```python
from name_variants import lookup_all

key, variants = lookup_all("Chan")
# key      → "陈"
# variants → ["陳", "chen", "chan", "tan", "chin", "zen", "chern"]
```

## Design

- **Script form is always the canonical key** — `陈`, `박`, `محمد`, not romanizations
- **Zero runtime dependencies** — pure Python dicts
- **Lowercase romanizations** — callers casefold before lookup
- **`None` for unknowns** — explicit signal to fall back to fuzzy matching

## Install

```bash
pip install name-variants
```

Optional: CJK normalization helpers (opencc + jaconv):

```bash
pip install "name-variants[normalize]"
```
