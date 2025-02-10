import sys
import json
import requests
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLabel
from PyQt6.QtCore import Qt, QThread, pyqtSignal

API_URL = "http://127.0.0.1:8000/inventory"

class FetchInventoryThread(QThread):
    data_fetched = pyqtSignal(list)

    def run(self):
        try:
            response = requests.get(API_URL)
            if response.status_code == 200:
                self.data_fetched.emit(response.json())  # Emit fetched data
            else:
                self.data_fetched.emit([])
        except Exception as e:
            print("Error fetching inventory:", e)
            self.data_fetched.emit([])

class InventoryApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.loadInventory()  # Load inventory on startup

    def initUI(self):
        self.setWindowTitle("Inventory Management")
        self.setGeometry(100, 100, 500, 300)
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.label = QLabel("Inventory:")
        layout.addWidget(self.label)
        
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Item Name", "Quantity"])
        layout.addWidget(self.table)
        
        self.refresh_button = QPushButton("Refresh Inventory")
        self.refresh_button.clicked.connect(self.loadInventory)
        layout.addWidget(self.refresh_button)

    def loadInventory(self):
        """ Fetch inventory data using a background thread. """
        self.thread = FetchInventoryThread()
        self.thread.data_fetched.connect(self.updateTable)  # Connect signal
        self.thread.start()

    def updateTable(self, inventory_data):
        """ Update table with fetched inventory data. """
        self.table.setRowCount(len(inventory_data))

        for row, item in enumerate(inventory_data):
            self.table.setItem(row, 0, QTableWidgetItem(item["name"]))
            self.table.setItem(row, 1, QTableWidgetItem(str(item["quantity"])))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InventoryApp()
    window.show()
    sys.exit(app.exec())
