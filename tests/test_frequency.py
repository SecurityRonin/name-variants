from name_variants import lookup


def test_get_frequency_known():
    clusters = lookup("陈")
    assert any(c.frequency is not None and c.frequency > 0 for c in clusters)


def test_get_frequency_top_chinese():
    clusters = lookup("王")
    assert any(c.frequency is not None and c.frequency > 100_000_000 for c in clusters)


def test_get_frequency_unknown():
    assert lookup("Smith") == []
    assert lookup("UnknownXyz") == []


def test_language_distribution_nguyen():
    clusters = lookup("Nguyen")
    assert any(c.language == "vietnamese" for c in clusters)


def test_language_distribution_lee_is_ambiguous():
    clusters = lookup("Lee")
    languages = {c.language for c in clusters}
    assert len(languages) >= 2


def test_language_distribution_unknown():
    assert lookup("Kowalski") == []
    assert lookup("") == []


def test_get_language_chan():
    clusters = lookup("陈")
    assert any(c.language == "chinese" for c in clusters)


def test_get_language_korean():
    clusters = lookup("이")
    assert any(c.language == "korean" for c in clusters)


def test_get_language_unknown():
    assert lookup("Smith") == []
