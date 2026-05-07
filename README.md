[![Stars](https://img.shields.io/github/stars/SecurityRonin/name-variants?style=flat-square)](https://github.com/SecurityRonin/name-variants/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI](https://github.com/SecurityRonin/name-variants/actions/workflows/ci.yml/badge.svg)](https://github.com/SecurityRonin/name-variants/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/name-variants)](https://pypi.org/project/name-variants/)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/)
[![Sponsor](https://img.shields.io/badge/sponsor-h4x0r-ea4aaa?logo=github-sponsors)](https://github.com/sponsors/h4x0r)

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
- **No language detection** — the index is a flat map; romanization collisions across languages are resolved last-write-wins with the highest-priority table winning (Chinese > Korean > Arabic > …). When a romanization is ambiguous (e.g. `Lee` could be Chinese 李 or Korean 이), the table loaded last wins. Use `lookup_all()` to see all candidates.

## Install

```bash
pip install name-variants
```

Optional: CJK normalization helpers (opencc + jaconv):

```bash
pip install "name-variants[normalize]"
```

The `[normalize]` extra installs two pure-Python packages:
- **opencc-python-reimplemented** — converts Traditional Chinese input to Simplified before lookup (e.g. `陳` → `陈` programmatically, beyond the explicit Traditional variants already in the table)
- **jaconv** — normalizes Japanese kana (katakana ↔ hiragana, full-width ↔ half-width)

Both are optional because the core package ships zero dependencies — most callers pre-normalize upstream.

---

## Related Projects

- **[veil](https://github.com/SecurityRonin/veil)** — pseudonymization pipeline that uses `name-variants` for entity resolution before anonymization
- **[winevt-forensic](https://github.com/SecurityRonin/winevt-forensic)** — Windows event log recovery and forensic parsing

---

[Privacy Policy](https://securityronin.github.io/name-variants/privacy/) · [Terms of Service](https://securityronin.github.io/name-variants/terms/) · © 2026 Security Ronin Ltd.
