from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.core.files.storage import FileSystemStorage as fs
import csv
import io

rows = ["NO CSV ADDED"]

def add(request):
    if request.method == 'POST' and request.FILES['csv']:
        name = request.FILES['csv']
        file = name.read().decode('utf-8')
        delim = request.POST['input_del']
        if len(delim) == 1:
            try:
                print(delim)
                global rows
                rows = list(csv.DictReader(io.StringIO(file), delimiter=delim))
                return render(request, "html/simple_upload.html")
            except:
                return HttpResponse("No such delimiter, refresh page and try again")
        else:
            return HttpResponse("one delimiter or NO, refresh page")

    return render(request, "html/simple_upload.html")

def check(request):
    return render(request, 'html/csv_read.html', {
        'rows': rows
    })