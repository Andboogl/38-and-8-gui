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
                data: dict = json.load(file)

            record = min(map(int, data.keys()))
            return data[str(record)]

        else:
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
            data[record_id] = {'moves': moves_count, 'seconds': seconds}
            json.dump(data, file, indent=4)


def test():
    records = Records()
    print(records.best_record())
    # records.load_record(6, 80)

if __name__ == '__main__':
    test()
