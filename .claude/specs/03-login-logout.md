# Spec: Login and Logout

## Overview
This feature implements the full user session lifecycle, including authentication (Login) and session termination (Logout). This allows users to securely access their private expense data and exit the application safely.

## Depends on
- 02-registration

## Routes
- `GET /login` — displays the login form — public
- `POST /login` — authenticates user credentials and establishes a session — public
- `GET /logout` — clears the user session and redirects to login — logged-in

## Database changes
No database changes.

## Templates
- **Modify:** `templates/login.html` — update to include a login form with email and password fields, and ensure it extends `base.html`.

## Files to change
- `app.py` — implement `POST /login` and `GET /logout` route logic.
- `templates/login.html` — update the login form.

## Files to create
No new files.

## New dependencies
No new dependencies.

## Rules for implementation
- No SQLAlchemy or ORMs
- Parameterised queries only
- Passwords verified using `werkzeug.security.check_password_hash`
- Use CSS variables — never hardcode hex values
- All templates extend `base.html`
- Store `user_id` in the Flask `session` object upon successful login
- Use `session.clear()` or `session.pop('user_id', None)` during logout

## Definition of done
- [ ] Navigating to `/login` displays a login form.
- [ ] Submitting valid credentials successfully authenticates the user and redirects them to a protected page (e.g., `/profile`).
- [ ] Submitting invalid credentials returns an appropriate error message.
- [ ] Navigating to `/logout` while authenticated clears the session and redirects to the login page.
- [ ] Attempting to access protected routes without being logged in redirects the user to the login page.
- [ ] The user's `user_id` is correctly stored in the session after login and removed after logout.
