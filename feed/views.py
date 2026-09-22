from django.views.generic import TemplateView
from .models import Post
# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'
    objects = Post.objects.all()
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['objects']=self.objects
        return context