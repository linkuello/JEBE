from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ItemForm

@login_required
def Special_views(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')  
    else:
        form = ItemForm()

    return render(request, 'create_item.html', {'form': form})
