from pathlib import Path

from dotenv import load_dotenv

from examples.drive.upload_file import upload_file_to_the_google_drive

DOTENV_PATH = Path('.env')


if __name__ == '__main__':
    load_dotenv(DOTENV_PATH)
    f_path = "data/invoice.xls"
    g_path = "Invoices/2021/Contract Type"
    upload_file_to_the_google_drive(f_path, g_path)
