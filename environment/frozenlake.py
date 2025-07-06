from typing import Tuple

class FrozenLakeEnv:
    def __init__(self, level, reward_hole=0):
        self.map = level
        self.reward_hole = reward_hole
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.start_pos = self._find_start()
        self.agent_pos = self.start_pos
        self.actions = ["up", "right", "down", "left"]
    
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
    
    def move_agent(self, direction: str):
        x, y = self.agent_pos

        match direction:
            case "up":
                new_x, new_y = x, y -1
            case "right":
                new_x, new_y = x + 1, y
            case "down":
                new_x, new_y = x, y + 1
            case "left":
                new_x, new_y = x - 1, y
            case _:
                print(f"Direction inconnue : {direction}")
                return self.agent_pos
        
        if 0 <= new_x < self.width and 0 <= new_y < self.height:
            self.agent_pos = (new_x, new_y)
        else:
            print(f"Sortie de map")
        
        return self.agent_pos
    
    def get_current_cell(self) -> str:
        return self.map[self.agent_pos[1]][self.agent_pos[0]]
    
    def is_terminal_state(self) -> bool:
        return self.get_current_cell() in ("H", "G")
        
    def get_reward(self) -> int:
        match self.get_current_cell():
            case "S" | "F":
                return 0
            case "G":
                return 1
            case "H":
                return self.reward_hole

    def step(self, action: str) -> Tuple[Tuple[int, int], int, bool]:
        self.move_agent(action)
        reward = self.get_reward()
        done = self.is_terminal_state()
        return self.agent_pos, reward, done
    
    def get_available_actions(self) -> list[str]:
        return self.actions

    def render_text(self):
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                if (x, y) == self.agent_pos:
                    row += "A "
                else:
                    row += self.map[y][x] + " "
            print(row)
        print()
