from pathlib import Path

from constants import GOOGLE_DRIVE_MIME_TYPES
from google_integration.drive import GoogleDriveService


def upload_file_to_the_google_drive(f_path: str, g_path: str):
    filename = 'Sam Smith'
    mimetype = 'application/vnd.ms-excel'
    drive = GoogleDriveService()
    parent_id = drive.get_path_parent_id(g_path)
    drive.upload_file(
        Path(f_path).absolute(),
        mime_type=mimetype,
        g_name=filename,
        g_mime_type=GOOGLE_DRIVE_MIME_TYPES["document"],
        parent_id=parent_id
    )
    drive.quit()
