from django.shortcuts import render
import praw
import random

# Create your views here.
def index(request):
    r = praw.Reddit('Statistics bot by /u/filthyneckbeard')
    puppies = r.get_subreddit('puppies').get_top_from_all(limit=250)
    puplist = list(puppies)
    puppy = puplist[random.randrange(1, 250)]
    while str(puppy.url).endswith('jpg') == False:
        puppy = puplist[random.randrange(1, 250)]
    return render(request, 'puppy/index.html', {'puppy': puppy.url})
