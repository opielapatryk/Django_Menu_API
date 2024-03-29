import dataclasses

@dataclasses.dataclass
class Dish:
    name: str
    description: str
    price: float
    
    @classmethod
    def from_dict(self,d):
        return self(**d)
    
    def to_dict(self):
        return dataclasses.asdict(self)
    