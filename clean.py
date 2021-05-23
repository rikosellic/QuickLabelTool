import os

labeled=os.listdir('labels')
labeled=[item.split('.')[0] for item in labeled]
images=os.listdir('images')
for image in images:
    if image.split('.')[0]  not in labeled:
        os.remove('images/'+image)