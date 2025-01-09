import os

def list_projects():
    current_dir = os.getcwd()
    ab_folders = []

    for folder in os.listdir(current_dir):
        username_dir = os.path.join(current_dir, folder)
        if os.path.isdir(username_dir):
            for ds_folder in os.listdir(username_dir):
                proj_dir = os.path.join(username_dir, ds_folder)
                if os.path.isdir(proj_dir):
                    dfj = os.path.join(proj_dir, 'datafact.json')
                    if os.path.exists(dfj):
                        ab_folders.append((folder, ds_folder))
    return ab_folders

if __name__ == "__main__":
    ab_directories = list_projects()
    for a ,b in ab_directories:
        print(f'dataset.sh remote upload -s {a}/{b} -t latest haowu4/{b}')