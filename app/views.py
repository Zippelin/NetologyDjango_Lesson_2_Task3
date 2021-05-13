import datetime

from django.shortcuts import render
import os

files_dir_name = 'files/'

def file_list(request, date=None):

    template_name = 'index.html'
    context = {
        'files': [],
        'date': datetime.datetime.now()
    }

    print('date', date)

    dirs_list = os.listdir(files_dir_name)
    for file in dirs_list:
        if date and date.date() == datetime.datetime.fromtimestamp(os.path.getctime(files_dir_name + file)).date():
            context['files'].append({
                'name': file,
                'ctime': datetime.datetime.fromtimestamp(os.path.getctime(files_dir_name + file)),
                'mtime': datetime.datetime.fromtimestamp(os.path.getmtime(files_dir_name + file))
            })
        elif date is None:
            context['files'].append({
                'name': file,
                'ctime': datetime.datetime.fromtimestamp(os.path.getctime(files_dir_name + file)),
                'mtime': datetime.datetime.fromtimestamp(os.path.getmtime(files_dir_name + file))
            })

    return render(request, template_name, context)


def file_content(request, name):
    with open(files_dir_name + name) as f:
        file = f.readlines()
    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': '\n'.join(file)}
    )

