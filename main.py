import hydra


@hydra.main(config_path="./config", config_name="config")
def main(cfg):
    
    game = hydra.utils.instantiate(cfg.game)
    
    player1 = hydra.utils.instantiate(cfg.players.player1)
    player2 = hydra.utils.instantiate(cfg.players.player2)

    game.play(player1, player2)  
    
    return 0


if __name__ == "__main__":
    main()