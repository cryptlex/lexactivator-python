class Metadata(object):
    def __init__(self, metadata_dict):
        self.key = metadata_dict.get("key")
        self.value = metadata_dict.get("value")

class UserLicense(object):
    def __init__(self, user_license_dict):
        self.allowed_activations = user_license_dict.get("allowedActivations")
        self.allowed_deactivations = user_license_dict.get("allowedDeactivations")
        self.key = user_license_dict.get("key")
        self.type = user_license_dict.get("type")
        self.metadata = [Metadata(metadata_dict) for metadata_dict in user_license_dict.get("metadata", [])]

