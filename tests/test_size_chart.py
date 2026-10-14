import pytest

from app.size_chart import MeasurementRange, SizeChart, SizeChartRow

def test_range_contains_boundaries_and_inside():
    r = MeasurementRange(91, 97)
    assert r.contains(91)
    assert r.contains(94)
    assert r.contains(97)

def test_range_does_not_contain_outside_values():
    r = MeasurementRange(91, 97)
    assert not r.contains(90.9)
    assert not r.contains(97.1)

def test_range_rejects_min_greater_than_max():
    with pytest.raises(ValueError):
        MeasurementRange(97, 91)

def test_chart_get_row_found_and_missing():
    chart = SizeChart(rows=(SizeChartRow("M", chest=MeasurementRange(91,97)),))
    assert chart.get_row("M").chest == MeasurementRange(91, 97)
    assert chart.get_row("XL") is None

def test_chart_rejects_duplicate_labels():
    with pytest.raises(ValueError):
        SizeChart(rows=(SizeChartRow("M"), SizeChartRow("M")))