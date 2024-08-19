from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import ImageCreateForm
from .models import Image

@login_required
def image_create(request):
    if request.method == "POST":
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            new_image = form.save(commit=False)
            new_image.user = request.user
            new_image.save()
            messages.success(request, "Image created successfully")
            return redirect(new_image.get_absolute_url())
    else:
        form = ImageCreateForm(data=request.GET)
    return render(
        request,
        "images/image/create.html",
        {"form": form}
    )

def image_detail(request, id):
    image = get_object_or_404(Image, id=id)
    return render(
        request,
        "images/image/detail.html",
        {"image": image}
    )

@login_required
@require_POST
def image_like(request):
    image_id = request.GET.get("id")
    action = request.GET.get("action")
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == "like":
                image.like.add(request.user)
            else:
                image.like.remove(request.user)
            return JsonResponse({"status": "ok"})
        except Image.DoesNotExist:
            pass
    return JsonResponse({"status": "error"})