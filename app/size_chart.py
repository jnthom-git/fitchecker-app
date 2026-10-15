from dataclasses import dataclass

@dataclass(frozen=True)
class MeasurementRange:
    min_cm: float 
    max_cm: float

    def __post_init__(self) -> None:
        if self.min_cm <= 0:
            raise ValueError("min_cm must be positive")
        if self.min_cm > self.max_cm:
            raise ValueError(f"min_cm ({self.min_cm}) cannot be greater than max_cm ({self.max_cm})"
            )
    def contains(self, value_cm: float) -> bool:
        return self.min_cm <= value_cm <= self.max_cm

@dataclass(frozen=True)
class SizeChartRow:
    label: str
    chest: MeasurementRange | None = None
    waist: MeasurementRange | None = None
    hips: MeasurementRange | None = None

    def __post_init__(self) -> None:
        if self.chest is None and self.waist is None and self.hips is None:
            raise ValueError(f"SizeChartRow '{self.label}' must have at least one measurement range defined")
        
@dataclass(frozen=True)
class SizeChart:

    rows: tuple[SizeChartRow, ...]

    def __post_init__(self) -> None:
        if not self.rows:
            raise ValueError("SizeChart must have at least one row")
        labels = [row.label for row in self.rows]
        if len(labels) != len(set(labels)):
            raise ValueError("SizeChart rows must have unique labels")
    
    def labels(self) -> list[str]:
        return [row.label for row in self.rows]

    def get_row(self, label: str) -> SizeChartRow | None:
        for row in self.rows:
            if row.label == label:
                return row
        return None