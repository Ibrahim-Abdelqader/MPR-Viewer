import sys
from PyQt5.QtWidgets import QApplication 
from app import MainWindow

def main():
    """Main function for the application."""

    # Create the application
    app = QApplication(sys.argv)

    # Set a custom dark theme
    app.setStyleSheet("""
    QWidget {
        background-color: #2E2E2E;  /* Background color */
        color: #FFFFFF;              /* Text color */
    }
    QPushButton {
        background-color: #444444;   /* Button background */
        color: #FFFFFF;               /* Button text color */
        border: none;
        padding: 5px;
        border-radius: 3px;           /* Rounded corners */
    }
    QPushButton:hover {
        background-color: #555555;    /* Button hover background */
    }
    QLineEdit {
        background-color: #3E3E3E;    /* Line edit background */
        color: #FFFFFF;                /* Line edit text color */
        border: 1px solid #666666;     /* Border for line edit */
        border-radius: 3px;            /* Rounded corners */
        padding: 5px;                  /* Padding inside the line edit */
    }
    QLabel {
        color: #FFFFFF;                /* Label text color */
    }
    """)

    # Create and show the main window
    window = MainWindow()
    window.show()

    # Start the event loop
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()