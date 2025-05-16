# Nitron Browser

-Nitron Browser is a simple, tabbed web browser built with Python, using PyQt5 and QtWebEngine. It features navigation controls, tab management, bookmarking, and a dark mode toggle. 
-The browser features navigation controls (back, forward, reload, home), tab management, bookmarking, and a toggle for dark mode. 
-Bookmarks are stored in memory for the session, and the interface is styled for both light and dark themes.

## Features

- Multiple tabs with easy switching and closing
- Navigation toolbar: Back, Forward, Reload, Home, New Tab
- Bookmarking: Add and view bookmarks (session-based)
- Dark mode and light mode toggle
- Styled interface for a modern look

## Requirements

- Python 3.x
- PyQt5
- PyQtWebEngine

Install dependencies with:

```sh
pip install PyQt5 PyQtWebEngine
```

## Usage

Run the browser with:

```sh
python Browserpy.py
```

## File Overview

- [`Browserpy.py`](r:/Browserpy.py): Main application file containing the browser implementation.

## Notes

- Bookmarks are not persistent and will be lost when the browser is closed.
- The default homepage is set to [Brave Search](https://search.brave.com).

## License

This project is provided as-is for educational purposes.
