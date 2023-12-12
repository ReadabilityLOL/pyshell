import curses
import subprocess


def draw_borders(window):
    window.border('|', '|', '-', '-', '+', '+', '+', '+')

def main(stdscr):
    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()
    stdscr.refresh()

    # Calculate window sizes and positions
    max_y, max_x = stdscr.getmaxyx()
    half_x = max_x // 2
    half_y = max_y // 2

    # Create windows for different sections
    window1 = curses.newwin(max_y - 4, half_x - 2, 1, 1)
    window2 = curses.newwin(max_y - 4, half_x - 2, 1, half_x + 1)
    window3 = curses.newwin(5, max_x - 2, max_y - 6, 1)
    window4 = curses.newwin(3, max_x - 2, max_y - 3, 1)

    while True:
        # Clear windows
        window1.clear()
        window2.clear()
        window3.clear()
        window4.clear()

        # Draw borders for windows
        draw_borders(window1)
        draw_borders(window2)
        draw_borders(window3)
        draw_borders(window4)

        window1.addstr(1, 2, "top")
        window2.addstr(1, 2, "Other Useful Output")
        window3.addstr(1, 2, "EX:")
        window3.addstr(2, 2, "After a command is inputted it goes here")
        window4.addstr(1, 2, "Command Input")

        # Refresh windows
        window1.refresh()
        window2.refresh()
        window3.refresh()
        window4.refresh()

        # Get user input
        user_input = window4.getstr(2, 2).decode('utf-8')

        # Exit when 'q' is pressed
        if user_input.lower() == 'q':
            break

curses.wrapper(main)
