# Spec: Registration

## Overview
This feature implements the user registration process, allowing new users to create an account by providing their name, email, and password. This is a foundational step in the Spendly roadmap to enable personalized expense tracking.

## Depends on
- 01-setup-database

## Routes
- `GET /register` — displays the registration form — public
- `POST /register` — processes registration data and creates a user account — public

## Database changes
No database changes. The `users` table already exists with the required columns (`name`, `email`, `password_hash`).

## Templates
- **Modify:** `templates/register.html` — update to include a form with fields for name, email, and password, and ensure it extends `base.html`.

## Files to change
- `app.py` — implement the `POST /register` route logic.
- `templates/register.html` — update the registration form.

## Files to create
No new files.

## New dependencies
No new dependencies.

## Rules for implementation
- No SQLAlchemy or ORMs
- Parameterised queries only
- Passwords hashed with werkzeug
- Use CSS variables — never hardcode hex values
- All templates extend `base.html`

## Definition of done
- [ ] Navigating to `/register` displays a registration form.
- [ ] Submitting the form with valid data creates a new user in the `users` table.
- [ ] Attempting to register with an email that already exists returns an appropriate error message.
- [ ] Passwords are stored as hashes in the database, not plain text.
- [ ] Registration successfully redirects the user to the login page or lands them on the dashboard.
