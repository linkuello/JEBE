from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SectionForm
from .models import Section

def cafe_view(request):
    return render(request, 'cafe/cafe.html', {
    
    })


@login_required
def section_detail(request, section_id):
    section = get_object_or_404(Section, pk=section_id)
    return render(request, 'cafe/section_detail.html', {'section': section})

def section_detail(request, section_id):
    section = Section.objects.get(pk=section_id)
    return render(request, 'cafe/section_detail.html', {'section': section})

def update_section(request, section_id):
    section = Section.objects.get(pk=section_id)

    if request.method == 'POST':
        form = SectionForm(request.POST, instance=section)
        if form.is_valid():
            form.save()
            return redirect('cafe:section_detail', section_id=section_id)
    else:
        form = SectionForm(instance=section)

    return render(request, 'cafe/update_section.html', {'form': form, 'section': section})
