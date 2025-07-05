from levels import LEVEL_1
from typing import Tuple

class FrozenLakeEnv:
    def __init__(self):
        self.map = LEVEL_1
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.start_pos = self._find_start()
        self.agent_pos = self.start_pos
    
    def _find_start(self) -> Tuple[int, int]:
        for y, row in enumerate(self.map):
            for x, cell in enumerate(row):
                if cell == "S":
                    return (x, y)
        raise ValueError("Start position ('S') not found in level")
    
    def reset(self) -> Tuple[int, int]:
        self.agent_pos = self.start_pos
        return self.agent_pos
    
    def get_map(self):
        return self.map
    
    def get_agent_position(self) -> Tuple[int, int]:
        return self.agent_pos