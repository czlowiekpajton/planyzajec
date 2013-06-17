from django.http import HttpResponse
from django.template import RequestContext, loader
from models import Rooms
import SubjectList
from SubjectList.models import Subjects
from SubjectList.SearchForm import SearchingForm

# Create your views here.
def index(request):
    #print request.session['login']
    
    if request.method == 'POST':
        form = SearchingForm(request.POST)
        if form.is_valid():
            szukany_semestr = form.cleaned_data['semester']
            subjects = Subjects.objects.filter(semestersid = szukany_semestr)
           
    else:
        form = SearchingForm()
        subjects = Subjects.objects.filter(semestersid = 1)
    
    t = loader.get_template('SubjectList/index.html')
    c = RequestContext(request, {'subjects': subjects, 'search': form})
    return HttpResponse(t.render(c))
