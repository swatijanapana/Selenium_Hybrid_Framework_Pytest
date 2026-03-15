import os
import shutil
import datetime


def create_unique_file_copy(original_path):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    base_dir = os.path.dirname(original_path)
    file_name = os.path.basename(original_path)

    name, ext = os.path.splitext(file_name)

    unique_file = os.path.join(base_dir, f"{name}_{timestamp}{ext}")

    shutil.copy(original_path, unique_file)
    return unique_file