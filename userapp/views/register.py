from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect

from userapp.forms import RegisterForm


class RegisterView(FormView):
    form_class = RegisterForm
    success_url = "/login"
    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/bookslist')
        else:
            return super(RegisterFormView, self).dispatch(
                request, *args, **kwargs)
