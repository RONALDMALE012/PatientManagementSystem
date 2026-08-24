from django.shortcuts import render, redirect, get_object_or_404
from .models import Visit
from .forms import VisitForm
def visit_list(request):
    visits = Visit.objects.select_related('patient').all()
    return render(request,
                  'visits/visit_list.html',
                  {'visits': visits})
def add_visit(request):
    if request.method == 'POST':
        form = VisitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visit_list')
    else:
        form = VisitForm()
    return render(request,
                  'visits/visit_form.html',
                  {'form': form})
def edit_visit(request, id):
    visit = get_object_or_404(Visit, pk=id)
    if request.method == 'POST':
        form = VisitForm(request.POST, instance=visit)
        if form.is_valid():
            form.save()
            return redirect('visit_list')
    else:
        form = VisitForm(instance=visit)
    return render(request,
                  'visits/visit_form.html',
                  {'form': form})
def delete_visit(request, id):
    visit = get_object_or_404(Visit, pk=id)
    visit.delete()
    return redirect('visit_list')
