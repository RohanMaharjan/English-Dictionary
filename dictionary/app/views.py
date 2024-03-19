from django.shortcuts import render
from django.http import HttpResponse
from .models import Word

def home(request):
    return render(request, 'home.html')

def search_meaning(request):
    if request.method== 'GET':
        word = request.GET.get('word', ' ')
        # previous_searchs = request.session.get('previous_searches', [])

        try:
            word_obj = Word.objects.get(word=word)
            meaning = word_obj.meaning.meaning
            context = {
                'word' : word,
                'meaning' : meaning,
                # 'previous_searches' : previous_searchs
            }
            # previous_searchs.append((word,meaning))
            # request.session['previous_searches'] = previous_searchs
            return render(request, 'search_result.html', context)
        except Word.DoesNotExist:
            return render(request, 'word_not_found.html')
        return render(request, 'search_result.html')