from name_variants import lookup_dialect


def test_chan_is_cantonese():
    assert lookup_dialect("Chan") == "cantonese"


def test_chen_is_mandarin():
    assert lookup_dialect("chen") == "mandarin_pinyin"


def test_tan_is_hokkien():
    assert lookup_dialect("tan") == "hokkien"


def test_zhang_is_mandarin():
    assert lookup_dialect("Zhang") == "mandarin_pinyin"


def test_cheung_is_cantonese():
    assert lookup_dialect("Cheung") == "cantonese"


def test_unknown_returns_none():
    assert lookup_dialect("Smith") is None
    assert lookup_dialect("Kim") is None  # Korean, not Chinese


def test_traditional_char_tagged():
    assert lookup_dialect("陳") == "traditional"


def test_case_insensitive():
    assert lookup_dialect("CHAN") == lookup_dialect("chan")
