import os

DATA_SOURCE_FOLDER = "ExtraSensory.per_uuid_features_labels"
ROOT_FOLDER = os.path.join(os.getcwd(), "temp")
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DATABASE = "extrasensory"
MONGO_COLLECTION = "location_labels"
