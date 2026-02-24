class ReleaseFile(object):
    def __init__(self, file_dict):
        self.size = file_dict.get("size")
        self.downloads = file_dict.get("downloads")
        self.secured = file_dict.get("secured")
        self.id = file_dict.get("id")
        self.name = file_dict.get("name")
        self.url = file_dict.get("url")
        self.extension = file_dict.get("extension")
        self.checksum = file_dict.get("checksum")
        self.release_id = file_dict.get("releaseId")
        self.created_at = file_dict.get("createdAt")
        self.updated_at = file_dict.get("updatedAt")
        
class Release(object):
    def __init__(self, release_dict):
        self.total_files = release_dict.get("totalFiles")
        self.is_private = release_dict.get("isPrivate")
        self.published = release_dict.get("published")
        self.id = release_dict.get("id")
        self.created_at = release_dict.get("createdAt")
        self.updated_at = release_dict.get("updatedAt")
        self.name = release_dict.get("name")
        self.channel = release_dict.get("channel")
        self.version = release_dict.get("version")
        self.notes = release_dict.get("notes")
        self.published_at = release_dict.get("publishedAt")
        self.product_id = release_dict.get("productId")
        self.platforms = release_dict.get("platforms", [])
        self.files = [ReleaseFile(file_dict) for file_dict in release_dict.get("files", [])]







