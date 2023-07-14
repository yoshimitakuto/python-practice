""""
dataclass
データの格納に特化したクラスのこと。
※複数のデータを格納する必要がある時によく使用される。
"""

from dataclasses import dataclasses, dataclass, field

@dataclass
class User:
    name: str
    age: int
    items: list[int] = field(default_factory=list)
    items1: list[int] = field(default_factory=lambda: ['note', 'pen'])
    
user = User('sato', 20)
result = dataclasses.asdict(user)
print(user.name)
print(user.age)    
print(user.items)
print(user.items1)
print(result)