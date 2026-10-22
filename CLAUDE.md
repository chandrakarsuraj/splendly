# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

- **Run App**: `python app.py` (Runs on port 5001 by default)
- **Install Dependencies**: `pip install -r requirements.txt`
- **Run Tests**: `pytest`
- **Run Single Test**: `pytest path/to/test_file.py`

## Architecture & Structure

The project is a Flask-based Expense Tracker application.

### High-Level Structure
- `app.py`: Main entry point containing Flask app initialization and route definitions.
- `database/`: Contains database logic.
  - `db.py`: Intended for SQLite connection management (`get_db`), initialization (`init_db`), and seeding (`seed_db`).
- `templates/`: Jinja2 HTML templates for the frontend (landing, login, register, terms).
- `static/`: CSS and JavaScript assets.
  - `static/css/style.css`: Main application styling.
  - `static/js/main.js`: Frontend logic.

### Current State
The project is currently in an early stage with basic routing for authentication and landing pages. Core functionality (logout, profile, and CRUD operations for expenses) is currently implemented as placeholders.
̦