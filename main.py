import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from welcome import Ui_MainWindow
from dashboard import Ui_Dashboard  # Import the Dashboard UI class


class WelcomeScreen(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.PushButton.clicked.connect(
            self.open_dashboard)  # Connect to the new method

    def open_dashboard(self):
        self.dashboard_screen = DashboardScreen()  # Create an instance of the Dashboard
        self.dashboard_screen.showMaximized()  # Show the dashboard
        self.close()  # Close the welcome screen


class DashboardScreen(QMainWindow, Ui_Dashboard):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    welcome_screen = WelcomeScreen()
    welcome_screen.showMaximized()  # Open in full screen
    sys.exit(app.exec_())
