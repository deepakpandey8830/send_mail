from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import send_contact_email

@csrf_exempt
def send_email_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        if send_contact_email(name, email, subject, message):
            return JsonResponse({"message": "Email sent successfully!"}, status=200)
        else:
            return JsonResponse({"error": "Failed to send email."}, status=500)

    return render(request, "send-mail.html")
