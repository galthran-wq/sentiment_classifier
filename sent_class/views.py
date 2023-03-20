from .forms import SentenceUploadForm

from django.shortcuts import render

# Create your views here.
def index(request):
    image_uri = None
    predicted_label = None

    if request.method == 'POST':
        # in case of POST: get the uploaded image from the form and process it
        form = SentenceUploadForm(request.POST, request.FILES)
        if form.is_valid():
            text = form.cleaned_data['sentence']
            print(text)

            # try:
            #     predicted_label = get_prediction(image_bytes)
            # except RuntimeError as re:
            #     print(re)

    else:
        # in case of GET: simply show the empty form for uploading images
        form = SentenceUploadForm()

    
    # pass the form, image URI, and predicted label to the template to be rendered
    context = {
        'form': form,
        'image_uri': image_uri,
        'predicted_label': predicted_label,
    }
    return render(request, 'index.html', context)