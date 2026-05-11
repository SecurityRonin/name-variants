from name_variants import dialect


def test_chan_is_cantonese():
    assert dialect("Chan") == "cantonese"


def test_chen_is_mandarin():
    assert dialect("chen") == "mandarin_pinyin"


def test_tan_is_hokkien():
    assert dialect("tan") == "hokkien"


def test_zhang_is_mandarin():
    assert dialect("Zhang") == "mandarin_pinyin"


def test_cheung_is_cantonese():
    assert dialect("Cheung") == "cantonese"


def test_unknown_returns_none():
    assert dialect("Smith") is None
    assert dialect("Kim") is None  # Korean, not Chinese


def test_traditional_char_tagged():
    assert dialect("陳") == "traditional"


def test_case_insensitive():
    assert dialect("CHAN") == dialect("chan")
