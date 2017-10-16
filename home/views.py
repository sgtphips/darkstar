from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView

class HomeTemplateView(TemplateView):
	context_object_name = 'home'
	template_name = 'home/home.html'

	# def get_context_data(self, **kwargs):
	#     context = super(HomeTemplateView, self).get_context_data(**kwargs)
	#     context['summaries'] = Summary.objects.all()
	#     context['experiences'] = Experience.objects.all()
	#     context['schools'] = School.objects.all()
	#     context['skills'] = Skill.objects.all()
	#     context['certifications'] = Certification.objects.all()

	#     return context