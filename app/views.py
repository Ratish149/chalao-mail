from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import EmailSerializer
from .models import Mail
# Create your views here.

class SendEmailView(generics.ListCreateAPIView):
    queryset = Mail.objects.all()
    serializer_class = EmailSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        full_name = data.get('full_name')
        email = data.get('email')
        message = render_to_string('email.html')
        
        try:
            send_mail(
                subject='Chalao',
                message='',
                html_message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False
            )
            mail = Mail.objects.create(full_name=full_name, email=email)
            mail.save()

            return Response({"message": "Email sent successfully"}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": f"Failed to send email: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)








