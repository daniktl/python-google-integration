# Google integration constants
GOOGLE_DRIVE_SCOPES = {
    'full': 'https://www.googleapis.com/auth/drive'
}
GOOGLE_DRIVE_DEFAULT_PAGE_SIZE = 100
# https://developers.google.com/drive/api/v3/mime-types
GOOGLE_DRIVE_MIME_TYPES = {
    "spreadsheet": "application/vnd.google-apps.spreadsheet",
    "file": "application/vnd.google-apps.file",
    "folder": "application/vnd.google-apps.folder",
    "document": "application/vnd.google-apps.document"
}
GOOGLE_DRIVE_ROOT_FOLDER_NAME = "root"

# Logging
LOGGER_DIR_PATH = 'logs'
LOGGER_MAX_FILE_SIZE = 1000000
LOGGER_MAX_BACKUP_SIZE = 5
