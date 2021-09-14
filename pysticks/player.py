import time


class Player:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        assert type in ("human", "bot")
    
    def __repr__(self):
        return f"{self.name} ({self.type})"

    @staticmethod
    def check_game_state(game_state):
        keys = sorted(["max_pick", "nb_sticks", "current_stick"])
        return isinstance(game_state, dict) and (sorted(game_state.keys()) == keys)

    def play(self, game_state):
        assert self.check_game_state(game_state)
        return self._play(game_state)
    
    def _play(self, game_state):
        raise NotImplementedError


class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name, "human")

    def _play(self, game_state):
        n = int(input() or 1)
        return n


class BotPlayer(Player):
    def __init__(self, name, sleep=None):
        super().__init__(name, "bot")
        self.sleep = sleep

    @staticmethod
    def compute_best_pick(nb_sticks, current_stick, max_pick):
        step_size = max_pick + 1
        next_trap = list(range(nb_sticks, current_stick, -step_size))[-1]
        optimal_pick = next_trap - current_stick - 1
        return min(max_pick, max(1, optimal_pick))
        
    def _play(self, game_state):
        n = self.compute_best_pick(**game_state)
        if self.sleep is not None:
            time.sleep(self.sleep)
        input(f"{n} (press Enter to continue)")
        return n
    