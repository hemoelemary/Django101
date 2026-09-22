from django.contrib import messages
from django.views.generic import TemplateView,DetailView,FormView
from .models import Post
from .forms import PostForm

# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'
    #descending order by id newest
    objects = Post.objects.all().order_by('-id')
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['objects']=self.objects
        return context

class Details(DetailView):
    template_name='details.html'
    model=Post

class AddPost(FormView):
    template_name='add.html'
    form_class=PostForm
    success_url='/'
    def dispatch(self, request, *args, **kwargs):
        #when it is about to render
        self.request=request
        return super().dispatch(request, *args, **kwargs)
    def form_valid(self,form):
        # print(form.cleaned_data['image'])
        new_object=Post.objects.create(
            text=form.cleaned_data['text'],
            image=form.cleaned_data['image']
        )
        messages.add_message(self.request,messages.SUCCESS,'Succed post')
        return super().form_valid(form)