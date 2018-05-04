from classes.game_logic import Game


def main():

    h = int(input("Cells rows num: "))
    w = int(input("Cells cols num: "))

    game = Game.Game(h, w)
    game.run()

if __name__ == '__main__':
    main()