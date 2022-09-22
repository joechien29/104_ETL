import os


DOWNLOADS_DIR = 'downloads'
JOBS_DIR = os.path.join(DOWNLOADS_DIR, 'jobs')
OUTPUTS_DIR = 'outputs'


def create_dir():
    os.makedirs(DOWNLOADS_DIR, exist_ok=True)
    os.makedirs(JOBS_DIR, exist_ok=True)
    os.makedirs(OUTPUTS_DIR, exist_ok=True)


def job_file_exists(filepath):
    return os.path.exists(filepath) and os.path.getsize(filepath) > 0
