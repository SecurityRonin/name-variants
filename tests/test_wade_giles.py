"""Tests for Wade-Giles and postal Chinese surname romanizations."""
from name_variants import lookup, share_cluster, lookup_dialect


def test_zhou_chou_same_cluster():
    assert share_cluster("Chou", "Zhou")


def test_zhao_chao_same_cluster():
    assert share_cluster("Chao", "Zhao")


def test_qian_chien_same_cluster():
    assert share_cluster("Chien", "Qian")


def test_jiang_chiang_same_cluster():
    # Chiang Kai-shek / Jiang Jieshi — same character 蒋
    assert share_cluster("Chiang", "Jiang")


def test_song_sung_same_cluster():
    assert share_cluster("Sung", "Song")


def test_cao_tsao_same_cluster():
    assert share_cluster("Tsao", "Cao")


def test_cai_tsai_same_cluster():
    assert share_cluster("Tsai", "Cai")


def test_guo_kuo_same_cluster():
    assert share_cluster("Kuo", "Guo")


def test_ye_yeh_same_cluster():
    assert share_cluster("Yeh", "Ye")


def test_xu_hsu_same_cluster():
    # Hsu is extremely common for 徐 in Taiwan/diaspora
    assert share_cluster("Hsu", "Xu")


def test_zhu_chu_same_cluster():
    assert share_cluster("Chu", "Zhu")


def test_gao_kao_same_cluster():
    assert share_cluster("Kao", "Gao")


def test_xie_hsieh_same_cluster():
    assert share_cluster("Hsieh", "Xie")


def test_wade_giles_dialect_tag():
    # At least some W-G forms should be tagged
    # chou is W-G for 周
    d = lookup_dialect("chou")
    assert d == "wade_giles", f"Expected wade_giles, got {d!r}"


def test_wade_giles_forms_in_cluster():
    # lookup("Chou") should return a cluster containing both 周 and chou and zhou
    clusters = lookup("Chou")
    assert len(clusters) > 0
    c = clusters[0]
    assert "周" in c
    assert "chou" in c
    assert "zhou" in c
