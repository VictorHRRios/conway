from window import Window
from conway import Conway

def main():
    root_window = Window(1600, 1200)

    a_game = Conway(5, 5, 100, 100, 10, 10, root_window)

    a_game.start_game()
    

    root_window.wait_for_close()


if __name__ == "__main__":
    main()