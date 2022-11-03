from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage as fs
import csv
import io

rows = ["NO CSV ADDED"]

def add(request):
    if request.method == 'POST' and request.FILES['csv']:
        name = request.FILES['csv']
        file = name.read().decode('utf-8')
        global rows
        rows = list(csv.DictReader(io.StringIO(file), delimiter=';'))
        for row in rows:
            print(row)


        return render(request, "html/simple_upload.html")

    return render(request, "html/simple_upload.html")

def check(request):
    return render(request, 'html/csv_read.html', {
        'rows': rows
    })