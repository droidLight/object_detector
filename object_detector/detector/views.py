from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageUploadForm
from .predictor import apply_bounds_masks, savedImages

def result_page(request, context = {}):
    context['title'] = "Result"
    return render(request, 'detector/result_page.html', context)

def image_view(request):

    context = {}
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            orgImage, maskedImage, croppedDict = apply_bounds_masks(form)
            
            context['org_image'] = orgImage
            context['masked_image'] = maskedImage
            context['cropped_images'] = croppedDict
            print(croppedDict)
            context['result'] = True

            return result_page(request, context)
    else:
        form = ImageUploadForm()
        context['form'] = form
        return render(request, 'detector/image_view.html', context)

