import sqlite3
from werkzeug.security import generate_password_hash

DATABASE = "expense_tracker.db"

def get_db():
    """Returns a SQLite connection with row_factory and foreign keys enabled."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init_db():
    """Creates all tables using CREATE TABLE IF NOT EXISTS."""
    conn = get_db()
    with conn:
        # Users table
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TEXT DEFAULT (datetime('now'))
            )
        """)

        # Expenses table
        conn.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                date TEXT NOT NULL,
                description TEXT,
                created_at TEXT DEFAULT (datetime('now')),
                FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
            )
        """)
    conn.close()

def seed_db():
    """Inserts sample data for development if no users exist."""
    conn = get_db()
    with conn:
        # Idempotency check: return early if any user exists
        user_exists = conn.execute("SELECT 1 FROM users LIMIT 1").fetchone()
        if user_exists:
            return

        # Demo user
        conn.execute(
            "INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)",
            ("Demo User", "demo@spendly.com", generate_password_hash("demo123"))
        )

        # Get the user ID
        user = conn.execute("SELECT id FROM users WHERE email = 'demo@spendly.com'").fetchone()
        if user:
            user_id = user['id']
            # Sample expenses (8 total, covering all 7 categories)
            expenses = [
                (user_id, 15.50, "Food", "2023-10-01", "Lunch at cafe"),
                (user_id, 50.00, "Transport", "2023-10-02", "Gas"),
                (user_id, 120.00, "Bills", "2023-10-03", "Internet Bill"),
                (user_id, 45.00, "Health", "2023-10-04", "Pharmacy"),
                (user_id, 12.00, "Entertainment", "2023-10-05", "Movie ticket"),
                (user_id, 80.00, "Shopping", "2023-10-06", "New shoes"),
                (user_id, 20.00, "Other", "2023-10-07", "Misc item"),
                (user_id, 25.00, "Food", "2023-10-08", "Dinner"),
            ]
            conn.executemany(
                "INSERT INTO expenses (user_id, amount, category, date, description) VALUES (?, ?, ?, ?, ?)",
                expenses
            )
    conn.close()

if __name__ == "__main__":
    print("Initializing database...")
    init_db()
    print("Seeding database...")
    seed_db()
    print("Database setup complete.")
