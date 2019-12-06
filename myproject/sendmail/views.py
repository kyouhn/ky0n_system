from django.core.mail import EmailMessage
from django.http import HttpResponse


def index(request):
   EmailMessage(u'メールテスト', u'Hello World', to=['kzk0802kazuki@gmail.com', 'kzk0802kazuki@gmail.com']).send()
   return HttpResponse('Send your register email')