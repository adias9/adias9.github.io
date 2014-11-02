DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "ef89c582-63b8-41c8-bcd5-a96650613bcc43f81825-f37a-4582-9907-70d805ba8a409f2c139e-365c-44d7-8c18-ec55015a4236"
NEVERCACHE_KEY = "12e68457-c70f-418b-8dc3-3968f2d5b27714d4960a-c123-499e-975c-f2cd456ebb3b37cbd60a-2a65-44e3-81e5-a7bbbbd5f2ad"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
