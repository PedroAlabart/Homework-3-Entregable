from abc import ABC, abstractmethod
from collections import deque
from datetime import datetime, timedelta
from typing import List, Dict, Any, Deque

# === Interfaces (Abstracciones) ===

class EvictionPolicy(ABC):
    @abstractmethod
    def evict(self, data: Deque[Dict[str, Any]]) -> None:
        pass

class Storage(ABC):
    @abstractmethod
    def add(self, room: str, data: Any) -> None:
        pass

    @abstractmethod
    def get_all(self) -> List[Dict]:
        pass

    @abstractmethod
    def get_by_room(self, room: str) -> List[Dict]:
        pass

    @abstractmethod
    def get_by_time_range(self, start: datetime, end: datetime) -> List[Dict]:
        pass

# === Implementaciones concretas ===

class SlidingWindowEvictionPolicy(EvictionPolicy):
    def __init__(self, window_minutes: int = 5):
        self.window = timedelta(minutes=window_minutes)

    def evict(self, data: Deque[Dict[str, Any]]) -> None:
        now = datetime.now()
        while data and data[0]['timestamp'] < now - self.window:
            data.popleft()

class SlidingWindowStorage(Storage):
    def __init__(self, eviction_policy: EvictionPolicy):
        self.eviction_policy = eviction_policy
        self.cache: Deque[Dict[str, Any]] = deque()

    def add(self, room: str, data: Any) -> None:
        entry = {
            'timestamp': datetime.now(),
            'room': room,
            'data': data
        }
        self.cache.append(entry)
        self.eviction_policy.evict(self.cache)

    def get_all(self) -> List[Dict]:
        self.eviction_policy.evict(self.cache)
        return list(self.cache)

    def get_by_room(self, room: str) -> List[Dict]:
        self.eviction_policy.evict(self.cache)
        return [entry for entry in self.cache if entry['room'] == room]

    def get_by_time_range(self, start: datetime, end: datetime) -> List[Dict]:
        self.eviction_policy.evict(self.cache)
        return [entry for entry in self.cache if start <= entry['timestamp'] <= end]

# === Cliente: usa el sistema sin acoplarse a la implementación ===

class SlidingWindowCache:
    def __init__(self, storage: Storage):
        self.storage = storage

    def add(self, room: str, data: Any):
        self.storage.add(room, data)

    def get_recent(self):
        return self.storage.get_all()

    def get_by_room(self, room: str):
        return self.storage.get_by_room(room)

    def get_by_time_range(self, start: datetime, end: datetime):
        return self.storage.get_by_time_range(start, end)

# === Uso ===

if __name__ == "__main__":
    eviction_policy = SlidingWindowEvictionPolicy(window_minutes=5)
    storage = SlidingWindowStorage(eviction_policy)
    cache = SlidingWindowCache(storage)

    cache.add("Sala1", {"temp": 21})
    cache.add("Sala2", {"temp": 23})

    print("Todas las entradas:", cache.get_recent())
    print("Sala1:", cache.get_by_room("Sala1"))
