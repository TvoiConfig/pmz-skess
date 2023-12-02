from django.shortcuts import render
from contact.forms import RecordForm

def contact(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RecordForm()
    return render(request, 'contact.html', {'form': form})
