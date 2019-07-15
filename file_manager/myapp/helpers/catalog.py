from myapp.models import Folder, File

def get_catalog(user, root_folder):
    root_folder_details = {
        'id': Folder.objects.filter(user__email=user['email'])[0].id
    }

    children = []

    folders = Folder.objects.filter(user__email=user['email'], parentID=root_folder.id)
    for folder in folders:
        children.append({
            "type": "folder",
            "name": folder.name,
            "id": folder.id
        })

    files = File.objects.filter(folder__id=root_folder.id)
    for file in files:
        children.append({
            'type': 'file',
            'name': file.file.name[file.file.name.rfind('/') + 1:],
            'url': file.file.url
        })

    root_folder_details["children"] = children
    return root_folder_details