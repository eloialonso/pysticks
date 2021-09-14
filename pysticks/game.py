import os

from pysticks.player import Player
from pysticks.sticks import Sticks


class Game:
    def __init__(self, nb_sticks, max_pick):
        self.nb_sticks = nb_sticks
        self.max_pick = max_pick
        self.sticks, self.current_stick = None, None
        self.reset()

    def reset(self):
        self.sticks = Sticks(self.nb_sticks)
        self.current_stick = 0

    def is_over(self):
        return self.current_stick >= len(self.sticks)
    
    def clear_and_show_sticks(self):
        os.system('clear')
        print(self.sticks)

    def check_nb_to_pick_and_print_error(self, n):
        if n < 1:
            print("You must pick at least 1 stick.")
            return False
        if n > self.max_pick:
            print(f"You cannot pick more than {self.max_pick} sticks.")
            return False
        return True
    
    def get_state(self):
        state = {
            "nb_sticks": self.nb_sticks,
            "max_pick": self.max_pick,
            "current_stick": self.current_stick,
        }
        return state

    def pick(self, n):
        assert self.check_nb_to_pick_and_print_error(n)
        remaining_sticks = len(self.sticks) - self.current_stick
        n = min(n, remaining_sticks)
        for i in range(n):
            self.sticks.pick(self.current_stick)
            self.current_stick += 1

    def ask_to_play_while_not_valid(self, player):
        prompt = f"How many sticks do you want to pick (max: {self.max_pick}) ? "
        prompt = self.format_message_to_player(player, prompt)
        can_pick = False
        while not can_pick:
            print(prompt, end="", flush=True)
            n = player.play(self.get_state())
            can_pick = self.check_nb_to_pick_and_print_error(n)
        return n

    def format_message_to_player(self, player, message):
        return f"[{str(player)}] >> {message}"
    
    def play(self, player1, player2):
        assert all([isinstance(p, Player) for p in (player1, player2)])
        self.reset()
        self.clear_and_show_sticks()
        is_first_player_next = True
               
        while True:

            player = player1 if is_first_player_next else player2
            n = self.ask_to_play_while_not_valid(player)
            self.pick(n)
            self.clear_and_show_sticks()
            
            if self.is_over():
                lose_message = self.format_message_to_player(player, "You lose.")
                print(lose_message)
                win_message = self.format_message_to_player(player2 if is_first_player_next else player1, "You win.")
                print(win_message)
                return

            is_first_player_next = not is_first_player_next
