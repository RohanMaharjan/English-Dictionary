from django.shortcuts import render
from django.http import HttpResponse
from .models import Word
from django.shortcuts import render, redirect

def home(request):
    # return render(request, 'home.html')
    previous_searches = request.session.get('previous_searches', [])
    return render(request, 'home.html', {'previous_searches': previous_searches})

def search_meaning(request):
    if request.method== 'GET':
        word = request.GET.get('word', ' ').lower()
        previous_searchs = request.session.get('previous_searches', [])

        try:
            word_obj = Word.objects.get(word=word)
            '''meaning = word_obj.meaning.meaning
            synonym = word_obj.synonym.synonym
            antonym = word_obj.antonym.antonym'''
            meaning = word_obj.meaning.meaning if hasattr(word_obj, 'meaning') else ""
            synonym = word_obj.synonym.synonym if hasattr(word_obj, 'synonym') else ""
            antonym = word_obj.antonym.antonym if hasattr(word_obj, 'antonym') else ""
            context = {
                'word' : word,
                'meaning' : meaning,
                'synonym' : synonym,
                'antonym' : antonym,
                # 'previous_searches' : previous_searchs
            }
            previous_searchs.append((word,meaning))
            request.session['previous_searches'] = previous_searchs
            return render(request, 'search_result.html', context)
        except Word.DoesNotExist:
            return render(request, 'word_not_found.html')
        return render(request, 'search_result.html')
    
def search_history(request):
    # Fetch search history from session or database
    # history = request.session.get('previous_searches', [])
    # You can fetch search history from the database or wherever it's stored

    # Render the template with the search history
    # previous_searches = request.session.get('previous_searches', [])
    # context1= {
        # 'history': previous_searches
    # }
    # previous_searches.append((word,meaning,synonym,antonym))
    # request.session['previous_searches'] = previous_searches
#  return render(request, 'history.html', context1)
    previous_searches = request.session.get('previous_searches', [])
    return render(request, 'history.html', {'previous_searches': previous_searches})

def clear_search_history(request):
    if request.method == 'POST':
        if 'clear_history' in request.POST:
            if 'previous_searches' in request.session:
                del request.session['previous_searches']
    return redirect('home')
