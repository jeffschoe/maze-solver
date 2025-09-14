from graphics import Window


def main():
    win = Window(800, 600)
    win.wait_for_close()


if __name__ == "__main__": # evaluates to TRUE if this script/file is run directly, so code below executes. If you import it to something else, this will be FALSE, so code below will not run automatically
    main() # main function gets executed