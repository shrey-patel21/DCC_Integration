import sys
import requests
from PySide6.QtWidgets import QApplication
from ui.ui import InventoryUI

API_URL = "http://127.0.0.1:8000"  # FastAPI server URL

class InventoryApp(InventoryUI):
    def __init__(self):
        super().__init__()

        # Load inventory on startup
        self.load_inventory()

        # Button Actions
        self.buy_button.clicked.connect(self.buy_item)
        self.return_button.clicked.connect(self.return_item)

    def load_inventory(self):
        """Fetch inventory from the server and update UI"""
        try:
            response = requests.get(f"{API_URL}/inventory")
            if response.status_code == 200:
                items = response.json()
                self.inventory_list.clear()
                for item in items:
                    self.inventory_list.addItem(f"{item['name']} - {item['quantity']}")
            else:
                self.inventory_list.addItem("Failed to load inventory")
        except Exception as e:
            self.inventory_list.addItem(f"Error: {e}")

    def buy_item(self):
        """Send request to increase item quantity"""
        selected = self.inventory_list.currentItem()
        if selected:
            item_name = selected.text().split(" - ")[0]
            requests.post(f"{API_URL}/update-quantity", json={"name": item_name, "quantity": 1})
            self.load_inventory()

    def return_item(self):
        """Send request to decrease item quantity"""
        selected = self.inventory_list.currentItem()
        if selected:
            item_name = selected.text().split(" - ")[0]
            requests.post(f"{API_URL}/update-quantity", json={"name": item_name, "quantity": -1})
            self.load_inventory()

# Run the UI
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InventoryApp()
    window.show()
    sys.exit(app.exec())
