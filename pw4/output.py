import curses

def write_line(stdscr, row, text):
    height, width = stdscr.getmaxyx()
    if 0 <= row < height - 1 and width > 1:
        stdscr.addnstr(row, 1, str(text), width - 2)

def show_message(stdscr, message):
    stdscr.clear()
    stdscr.box()
    stdscr.addstr(2, 2, message)
    stdscr.addstr(4, 2, "Press any key to continue")
    stdscr.refresh()
    stdscr.getch()

def show_lines(stdscr, title, lines):
    height, width = stdscr.getmaxyx()
    page_size = max(1, height - 5)
    lines = lines or ["No records."]
    pages = (len(lines) + page_size - 1) // page_size

    for page in range(pages):
        stdscr.clear()
        stdscr.box()
        write_line(stdscr, 1, title)
        start = page * page_size
        for row, line in enumerate(lines[start:start + page_size], start=3):
            write_line(stdscr, row, line)
        footer = "Press any key to continue" if page + 1 < pages else "Press any key to return"
        write_line(stdscr, height - 2, footer)
        stdscr.refresh()
        stdscr.getch()