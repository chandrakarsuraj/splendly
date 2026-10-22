import sqlite3

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
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Expenses table
        conn.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                description TEXT,
                date DATE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
            )
        """)
    conn.close()

def seed_db():
    """Inserts sample data for development."""
    conn = get_db()
    with conn:
        # Sample user
        conn.execute(
            "INSERT OR IGNORE INTO users (username, password, email) VALUES (?, ?, ?)",
            ("testuser", "hashed_password_123", "test@example.com")
        )

        # Get the user ID
        user = conn.execute("SELECT id FROM users WHERE username = 'testuser'").fetchone()
        if user:
            user_id = user['id']
            # Sample expenses
            expenses = [
                (user_id, 15.50, "Food", "Lunch at cafe", "2023-10-01"),
                (user_id, 50.00, "Transport", "Gas", "2023-10-02"),
                (user_id, 120.00, "Shopping", "New shoes", "2023-10-03"),
                (user_id, 12.00, "Entertainment", "Movie ticket", "2023-10-04"),
            ]
            conn.executemany(
                "INSERT INTO expenses (user_id, amount, category, description, date) VALUES (?, ?, ?, ?, ?)",
                expenses
            )
    conn.close()

if __name__ == "__main__":
    # Allow running this script directly to setup the database
    print("Initializing database...")
    init_db()
    print("Seeding database...")
    seed_db()
    print("Database setup complete.")
