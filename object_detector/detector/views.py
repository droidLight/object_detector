from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageUploadForm
from .predictor import apply_bounds_masks

def image_view(request):

    context = {}
    image = None
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            output_name = form.cleaned_data.get('input_name')
            #form.cleaned_data.get('input_image')
            threshold = form.cleaned_data.get('input_threshold')
            image = image.input_image.url
            maskedImage, croppedList = apply_bounds_masks(image, threshold, output_name)

            context['org_image'] = image
            context['masked_image'] = maskedImage
            context['cropped_images'] = croppedList
            context['result'] = True
    else:
        form = ImageUploadForm()

    context['form'] = form
    return render(request, 'detector/image_view.html', context)

