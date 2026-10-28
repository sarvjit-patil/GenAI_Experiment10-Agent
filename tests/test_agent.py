import pytest

from agent import validate_topic, format_three_bullets


def test_validate_topic():
    assert validate_topic("  AI research  ") == "AI research"


def test_empty_topic():
    with pytest.raises(ValueError):
        validate_topic("   ")


def test_exactly_three_bullets():
    result = format_three_bullets(
        "- First finding\n"
        "- Second finding\n"
        "- Third finding"
    )

    assert result.count("\n") == 2
    assert result.startswith("- First finding")


def test_wrong_bullet_count():
    with pytest.raises(ValueError):
        format_three_bullets("- First\n- Second")