from django.core.files.storage import default_storage

def upload_file(file, id):
    return default_storage.save("blog"+str(id), file)

def get_file_url(file_name):
    return default_storage.url(file_name)