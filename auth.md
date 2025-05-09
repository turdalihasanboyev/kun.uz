
```python
LOGIN_URL = 'login' # URL for login page (for @login_required page)
LOGIN_REDIRECT_URL = 'profile' # URL for redirect after login
LOGOUT_REDIRECT_URL = 'home' # URL for redirect after logout
SESSION_EXPIRE_AT_BROWSER_CLOSE = True # Session expires when browser is closed
SESSION_COOKIE_AGE = 3600 # Session expires after 1 hour
AUTH_USER_MODEL = 'auth.User' # User model for authentication
```
