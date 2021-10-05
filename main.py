from pathlib import Path

from dotenv import load_dotenv

from google_integration.drive import GoogleDriveService
from constants import GOOGLE_DRIVE_MIME_TYPES

DOTENV_PATH = Path('.env')


if __name__ == '__main__':
    load_dotenv(DOTENV_PATH)
    drive = GoogleDriveService()
    # drive.list_files()
    # drive.list_folders()
    # folder_id = drive.get_folder_id('Documents')
    # print(folder_id)
    parent_id = drive.get_path_parent_id("Invoices/2021/Contract Type")
    drive.upload_file(
        Path('data/invoice.xls').absolute(),
        'application/vnd.ms-excel',
        g_name='Sam Smith',
        g_mime_type=GOOGLE_DRIVE_MIME_TYPES["document"],
        parent_id=parent_id
    )
    drive.quit()
