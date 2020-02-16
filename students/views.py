from django.http import HttpResponse
from polls.forms import SuggestionsForm


def index(request):
    return HttpResponse("Hello, world. You're at the students home page.")
