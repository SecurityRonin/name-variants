from name_variants import (
    _get_language_for_canonical,  # internal, test directly
    get_frequency,
    language_distribution,
)


def test_get_frequency_known():
    assert get_frequency("陈") is not None
    assert get_frequency("陈") > 0


def test_get_frequency_top_chinese():
    assert get_frequency("王") > 100_000_000


def test_get_frequency_unknown():
    assert get_frequency("Smith") is None
    assert get_frequency("UnknownXyz") is None


def test_language_distribution_nguyen():
    dist = language_distribution("Nguyen")
    assert "vietnamese" in dist
    assert dist["vietnamese"] > 0.9  # nguyễn is ~40% of Vietnam, very dominant


def test_language_distribution_lee_is_ambiguous():
    dist = language_distribution("Lee")
    assert len(dist) >= 2
    total = sum(dist.values())
    assert abs(total - 1.0) < 0.01  # sums to 1


def test_language_distribution_unknown():
    assert language_distribution("Kowalski") == {}
    assert language_distribution("") == {}


def test_language_distribution_sums_to_one():
    for name in ["Chan", "Park", "Nguyen", "Muhammad", "Sato"]:
        dist = language_distribution(name)
        if dist:
            total = sum(dist.values())
            assert abs(total - 1.0) < 0.01, f"{name}: sum={total}"


def test_get_language_chan():
    lang = _get_language_for_canonical("陈")
    assert lang == "chinese"


def test_get_language_korean():
    lang = _get_language_for_canonical("이")
    assert lang == "korean"


def test_get_language_unknown():
    assert _get_language_for_canonical("Smith") is None
