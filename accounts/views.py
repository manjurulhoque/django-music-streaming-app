import json
from django.http import JsonResponse, HttpResponse
from .forms import RegistrationForm


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        data = {'email': email, 'password2': password2, 'password1': password1}
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(password1)
            form.save()
            return JsonResponse({"status": True, "message": "Registration confirm"})
        else:
            errors = []
            for field in form:
                for error in field.errors:
                    errors.append(error)
            return JsonResponse({"status": False, "errors": errors})
    else:
        return HttpResponse(json.dumps({"message": "Denied"}), content_type="application/json")
