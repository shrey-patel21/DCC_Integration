**Introduction :**
This project implements a complete Inventory Management System integrating FastAPI, SQLite, and PyQt6. The system provides a robust API for inventory management, a database for storage, a PyQt6 GUI for user interaction, and DCC integration for automation.

**System Architecture :**
The system follows a four-layer architecture:
  FastAPI Backend – Handles API requests, communicates with the database.
  SQLite Database – Stores inventory details persistently.
  DCC Integration – Ensures real-time inventory updates in the DCC environment.
  PyQt6 GUI – Provides a user-friendly interface for interacting with inventory data.

**Implementation Details :**
Backend (FastAPI & SQLite):
  Created API endpoints for CRUD operations on inventory.
  Integrated SQLite database using SQLAlchemy ORM.
  Implemented Pydantic models for data validation.
Frontend (PyQt6 UI):
  Built a responsive GUI that fetches and displays inventory data.
  Implemented multi-threading (QThread) to prevent UI blocking.
  Used requests library to communicate with the backend.
DCC Integration:
   The DCC tool communicates with our API to fetch and modify inventory data.
  Ensured seamless updates between the DCC plugin and the inventory system.

**Workflow:**
The PyQt6 GUI fetches data from the FastAPI backend.
The FastAPI backend retrieves inventory details from the SQLite database.
The user performs actions (add, update, delete), triggering API requests.
Changes reflect in both DCC Plugin and PyQt6 UI dynamically.

**Conclusion:**
This project successfully demonstrates the integration of FastAPI, SQLite, and PyQt6 for inventory management. The system provides real-time updates, smooth interaction, and efficient API communication. Future improvements could include user authentication, cloud database support, and data visualization.
