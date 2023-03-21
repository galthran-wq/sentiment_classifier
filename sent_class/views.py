import json
import torch
from transformers import DistilBertForSequenceClassification, DistilBertTokenizer
from .forms import SentenceUploadForm

from django.shortcuts import render

tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")
model = DistilBertForSequenceClassification.from_pretrained("galthran/distilbert-base-uncased-acllm")


def get_prediction(text):
    label_to_rating = {}
    for i in [0, 2, 3]:
        label_to_rating[i] = i + 1
    for i in [4, 5, 6, 7]:
        label_to_rating[i] = i + 2
    label_to_rating[1] = 10
    label_to_rating[0] = 1

    inputs = tokenizer(text, return_tensors="pt")
    ratings_dist = model(**inputs).logits.softmax(dim=-1)[0]
    return json.dumps({
        (label_to_rating[i]): (conf.item())
        for i, conf in enumerate(ratings_dist)
    })



# Create your views here.
def index(request):
    predicted_rating = None
    if request.method == 'POST':
        # in case of POST: get the uploaded image from the form and process it
        form = SentenceUploadForm(request.POST, request.FILES)
        if form.is_valid():
            text = form.cleaned_data['sentence']
            print(text)
            try:
                predicted_rating = get_prediction(text)
            except RuntimeError as re:
                print(re)

    else:
        # in case of GET: simply show the empty form for uploading images
        form = SentenceUploadForm()

    
    # pass the form, image URI, and predicted label to the template to be rendered
    context = {
        'form': form,
        'predicted_rating': predicted_rating,
    }
    return render(request, 'index.html', context)