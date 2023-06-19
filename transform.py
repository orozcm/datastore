import os


def get_filename(filename: str):
    return os.path.splitext(filename)[0]


def get_useruuid(filename: str):
    return filename.split(".")[0]


def get_fields(row: dict, filename: str):
    user_uuid = get_useruuid(get_filename(filename))
    row["user_uuid"] = user_uuid
    _row = {col: row[col] for col in row.keys() if
            col.startswith("location_quick_features") or col.startswith(
                "location") or col == "timestamp" or col == "user_uuid"}
    _row["timestamp"] = int(_row["timestamp"])
    return _row
