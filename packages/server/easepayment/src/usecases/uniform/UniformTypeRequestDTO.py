from dataclasses import dataclass, fields


@dataclass
class UniformTypeRequestDTO:
    type: str
    price: float
