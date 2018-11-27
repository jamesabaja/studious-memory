from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect

class HomePageView(TemplateView):
    template_name = "index.html"

class UserPageView(TemplateView):
    template_name = "user.html"

'''def UserPageView(TemplateView):
     #return HttpResponseRedirect("https://www.dropbox.com")
     return redirect("/user.html")'''

'''
# Add this view
class DataPageView(TemplateView):
    def get(self, request, **kwargs):
        context = {
            'data': [
                {
                    'name': 'Celeb 1',
                    'worth': '3567892'
                },
                {
                    'name': 'Celeb 2',
                    'worth': '23000000'
                },
                {
                    'name': 'Celeb 3',
                    'worth': '1000007'
                },
                {
                    'name': 'Celeb 4',
                    'worth': '456789'
                },
                {
                    'name': 'Celeb 5',
                    'worth': '7890000'
                },
                {
                    'name': 'Celeb 6',
                    'worth': '12000456'
                },
                {
                    'name': 'Celeb 7',
                    'worth': '896000'
                },
                {
                    'name': 'Celeb 8',
                    'worth': '670000'
                }
            ]
        }

        return render(request, 'data.html', context)'''