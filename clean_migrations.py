import os
import shutil

for app in os.listdir('./'):
    # print(app)
    if os.path.exists(f'{app}/migrations/'):
        # print("pass")
        shutil.rmtree(f'{app}/migrations/')
        print(f'clean migrations: {app}')
