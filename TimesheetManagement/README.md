# TimesheetManagement

A Flask timesheet app backed by MySQL. Employees log hours, managers review them, and
login is protected by time-based one-time passwords.

## Two-factor auth

Signup generates a TOTP secret per user with `pyotp`. Login is a two-step flow: the
password check at `/login/` does not create a session on its own, it sends a one-time code
over SMTP and hands off to `/login/2fa/`, which verifies the code before the user is let
in. A leaked password alone is not enough to sign in.

## Roles

Routes are separated by role rather than branching inside one view.

| Route | Who it serves |
|---|---|
| `/login/`, `/login/2fa/`, `/signup/` | everyone, unauthenticated |
| `/manager/` | managers reviewing and approving submitted time |
| `/premanager/` | the approval step ahead of a manager |
| `/other/`, `/nonothers/` | employee time entry, split by category |

Each has a GET for the page and a POST for the submission, with templates in `templates/`.

## Running it

```
pip install flask pyotp mysql-connector-python
```

Set the MySQL connection details and the SMTP credentials for code delivery, create the
user and timesheet tables, then:

```
python app.py
```

The app serves on `http://127.0.0.1:5000`.

## Known gaps

Credentials are read from the source rather than the environment. Move them to environment
variables before this runs anywhere real. There is also no rate limit on the 2FA endpoint,
so the code is brute-forceable, and `login.html` exists both at the top level and in
`templates/`, where only the second is used.

## Stack

Python, Flask, MySQL, pyotp, smtplib, HTML, CSS.
