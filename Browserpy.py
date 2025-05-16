import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QWidget, QToolBar, QAction, QTabWidget, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nitron Browser")
        self.setGeometry(100, 100, 1200, 800)


        # Default homepage and initial settings
        self.default_homepage = "https://search.brave.com"
        self.dark_mode_enabled = False
        self.bookmarks = []

        # Apply styles
        self.apply_styles()

        # Create the tab widget to manage tabs
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)

        # Add an initial tab
        self.add_new_tab(self.default_homepage, "Home")

        # Create a toolbar with navigation, home, new tab, bookmarks, and dark mode buttons
        nav_toolbar = QToolBar("Navigation")
        self.addToolBar(nav_toolbar)
        nav_toolbar.setIconSize(QSize(24, 24))

        # Add buttons with text
        back_button = QAction("Back", self)
        back_button.triggered.connect(lambda: self.current_tab().back())
        nav_toolbar.addAction(back_button)

        forward_button = QAction("Forward", self)
        forward_button.triggered.connect(lambda: self.current_tab().forward())
        nav_toolbar.addAction(forward_button)

        reload_button = QAction("Reload", self)
        reload_button.triggered.connect(lambda: self.current_tab().reload())
        nav_toolbar.addAction(reload_button)

        home_button = QAction("Home", self)
        home_button.triggered.connect(self.navigate_to_home)
        nav_toolbar.addAction(home_button)

        new_tab_button = QAction("Newtab", self)
        new_tab_button.triggered.connect(lambda: self.add_new_tab(self.default_homepage, "New Tab"))
        nav_toolbar.addAction(new_tab_button)

        bookmark_button = QAction("Bookmarks", self)
        bookmark_button.triggered.connect(self.add_bookmark)
        nav_toolbar.addAction(bookmark_button)

        view_bookmarks_button = QAction("View", self)
        view_bookmarks_button.triggered.connect(self.view_bookmarks)
        nav_toolbar.addAction(view_bookmarks_button)

        dark_mode_button = QAction("Toggle", self)
        dark_mode_button.triggered.connect(self.toggle_dark_mode)
        nav_toolbar.addAction(dark_mode_button)

        # Layout for the tabs
        layout = QVBoxLayout()
        layout.addWidget(self.tabs)

        # Container for the layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    


    def add_new_tab(self, url, title):
        browser = QWebEngineView()
        browser.setUrl(QUrl(url))
        browser.urlChanged.connect(self.update_tab_title)

        url_bar = QLineEdit()
        url_bar.setPlaceholderText("Enter URL and press Enter")
        url_bar.returnPressed.connect(lambda: self.navigate_to_url(url_bar, browser))

        tab_layout = QVBoxLayout()
        tab_layout.addWidget(url_bar)
        tab_layout.addWidget(browser)

        tab_container = QWidget()
        tab_container.setLayout(tab_layout)

        self.tabs.addTab(tab_container, title)
        self.tabs.setCurrentWidget(tab_container)
    
    def adjust_toolbar_size(self):
        # Check where the toolbar is docked
        if self.toolBarArea(self.nav_toolbar) in [Qt.LeftToolBarArea, Qt.RightToolBarArea]:
            self.nav_toolbar.setFixedWidth(150)  # Force a narrow width for side docking
        else:
            self.nav_toolbar.setFixedWidth(self.width())  # Expand width for top or bottom docking

    def current_tab(self):
        current_tab_container = self.tabs.currentWidget()
        return current_tab_container.layout().itemAt(1).widget()

    def navigate_to_url(self, url_bar, browser):
        url_text = url_bar.text().strip()
        if not (url_text.startswith("http://") or url_text.startswith("https://")):
            url_text = "https://" + url_text
        browser.setUrl(QUrl(url_text))

    def navigate_to_home(self):
        self.current_tab().setUrl(QUrl(self.default_homepage))

    def update_tab_title(self, url):
        current_tab_index = self.tabs.currentIndex()
        self.tabs.setTabText(current_tab_index, url.toString().split("/")[2])

    def close_tab(self, index):
        if self.tabs.count() > 1:
            self.tabs.removeTab(index)
        else:
            self.close()

    def toggle_dark_mode(self):
        if self.dark_mode_enabled:
        # Apply light mode styles
            self.setStyleSheet("""
            QMainWindow {
                background-color: #f2f2f2;  /* Light background */
                color: black;  /* Dark text */
            }
            QToolBar {
                background-color: #e0e0e0;
                border: none;
                padding: 6px;
            }
            QToolBar QToolButton {
                color: black;  /* Button text color */
                background: transparent;
                border: none;
                padding: 5px;
                font-size: 14px;
            }
            QToolBar QToolButton:hover {
                color: #0078d7;  /* Hover effect */
            }
            QTabWidget::pane {
                background-color: #e0e0e0;
                border: none;
            }
            QTabBar::tab {
                background: #d0d0d0;
                border-radius: 6px;
                padding: 12px;
                margin: 2px;
                color: black;
            }
            QTabBar::tab:selected {
                background: #c0c0c0;
                border: 1px solid #b0b0b0;
            }
            QTabBar::tab:hover {
                background: #b0b0b0;
                border-radius: 6px;
                color: black;
            }
            QLineEdit {
                background-color: #ffffff;
                border: none;
                border-radius: 6px;
                color: black;
                padding: 8px;
            }
        """)
            self.dark_mode_enabled = False
        else:
        # Apply dark mode styles
            self.setStyleSheet("""
            QMainWindow {
                background-color: #282828;  /* Dark background */
                color: white;
            }
            QToolBar {
                background-color: #333333;
                border: none;
                padding: 6px;
            }
            QToolBar QToolButton {
                color: white;  /* Button text color */
                background: transparent;
                border: none;
                padding: 5px;
                font-size: 14px;
            }
            QToolBar QToolButton:hover {
                color: #00bfff;  /* Hover effect */
            }
            QTabWidget::pane {
                background-color: #333333;
                border: none;
            }
            QTabBar::tab {
                background: #3c3c3c;
                border-radius: 6px;
                padding: 12px;
                margin: 2px;
                color: white;
            }
            QTabBar::tab:selected {
                background: #4c4c4c;
                border: 1px solid #5c5c5c;
            }
            QTabBar::tab:hover {
                background: #444444;
                border-radius: 6px;
                color: white;
            }
            QLineEdit {
                background-color: #3c3c3c;
                border: none;
                border-radius: 6px;
                color: white;
                padding: 8px;
            }
        """)
            self.dark_mode_enabled = True

    def add_bookmark(self):
        current_url = self.current_tab().url().toString()
        self.bookmarks.append(current_url)
        QMessageBox.information(self, "Bookmark Added", f"Bookmarked: {current_url}")

    def view_bookmarks(self):
        bookmarks_list = "\n".join(self.bookmarks)
        QMessageBox.information(self, "Bookmarks", f"Your bookmarks:\n{bookmarks_list}")

    def adjust_toolbar_size(self):
        # Check where the toolbar is docked
        if self.toolBarArea(self.nav_toolbar) in [Qt.LeftToolBarArea, Qt.RightToolBarArea]:
            self.nav_toolbar.setMinimumWidth(150)  # Set minimum width for side docking
            self.nav_toolbar.setMaximumWidth(150)  # Set maximum width for side docking
        else:
            self.nav_toolbar.setMinimumWidth(0)  # Reset for top/bottom docking
            self.nav_toolbar.setMaximumWidth(self.width())  # Reset for full width
        

    def apply_styles(self):
        # Apply styles with white button text
        self.setStyleSheet("""
            QMainWindow {
                background-color: #282828;
                color: white;
            }
            QToolBar {
                background-color: #333333;
                border: none;
                padding: 6px;
            }
            QToolBar QToolButton {
                color: white;  /* Button text color */
                background: transparent;
                border: none;
                padding: 5px;
                font-size: 14px;
            }
            QToolBar QToolButton:hover {
                color: #00bfff;  /* Hover effect color */
            }
            QTabWidget::pane {
                background-color: #333333;
                border: none;
            }
            QTabBar::tab {
                background: #3c3c3c;
                border-radius: 6px;
                padding: 12px;
                margin: 2px;
                color: white;
            }
            QTabBar::tab:selected {
                background: #4c4c4c;
                border: 1px solid #5c5c5c;
            }
            QTabBar::tab:hover {
                background: #444444;
                border-radius: 6px;
                color: #ffffff;
            }
            QLineEdit {
                background-color: #3c3c3c;
                border: none;
                border-radius: 6px;
                color: white;
                padding: 8px;
            }
        """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())
