from django.shortcuts import render
from .models import MiniAppCategory, Organization
from django.shortcuts import get_object_or_404
from .forms import MiniAppCategoryForm

# Create your views here.
def minapp(request):
    app_category = MiniAppCategory.objects.all()
    print("app_category", app_category)
    return render(request, 'miniapp/all_miniapp.html', {'app_category': app_category})

def miniapp_detail(request, app_id):
    app = get_object_or_404(MiniAppCategory, pk=app_id)
    return render(request, 'miniapp/miniapp_details.html', {'app': app })

def miniapp_organization_view(request):
    organization = None
    if request.method == "POST":
        form = MiniAppCategoryForm(request.POST)
        if form.is_valid():
            app_variety = form.cleaned_data['app_varieties']
            organization = Organization.objects.filter(app_varieties = app_variety)
    else:
        form = MiniAppCategoryForm()
    return render(request, 'miniapp/organization.html', {'organization': organization, 'form': form})
    