from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageUploadForm
from .predictor import apply_bounds_masks, savedImages

def main_page(request):
    context = {}
    context['title'] = "Main Page"
    context['images'] = savedImages()
    return render(request, 'detector/main_page.html', context)

def image_view(request):

    context = {}
    image = None
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            orgImage, maskedImage, croppedList = apply_bounds_masks(form)

            context['org_image'] = orgImage
            context['masked_image'] = maskedImage
            context['cropped_images'] = croppedList
            context['result'] = True
    else:
        form = ImageUploadForm()

    context['form'] = form
    return render(request, 'detector/image_view.html', context)

