from app.core.theme import load_qss


def test_load_qss():
    qss = load_qss()
    assert isinstance(qss, str)
    assert "Card" in qss
