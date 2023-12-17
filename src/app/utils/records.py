"""Records"""


import os
import json


class Records:
    """Records"""
    def __create_records_folder(self):
        """Create records folder and get folder path"""
        # Folder path
        folder_path = os.path.join(
            os.path.expanduser('~'),
            '38-and-8-gui.records')

        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

        return folder_path

    def best_record(self):
        """Get best record"""
        file_path = os.path.join(self.__create_records_folder(), 'records.json')

        if os.path.exists(file_path):
            with open(file_path) as file:
                data = json.load(file)

            if data:
                record = min(map(int, data.keys()))
                return data[str(record)]

        return None

    def load_record(self, moves_count, seconds):
        """Load new record"""
        record_id = int(moves_count) + int(seconds)
        file_path = os.path.join(self.__create_records_folder(), 'records.json')

        if os.path.exists(file_path):
            with open(file_path, 'r') as current:
                data = json.load(current)

        else:
            data = {} # dict()

        # Writing
        with open(file_path, 'x' if not os.path.exists(file_path) else 'w') as file:
            if not data.get(record_id, None):
                data[record_id] = {'moves': moves_count, 'seconds': seconds}
                json.dump(data, file, indent=4)
