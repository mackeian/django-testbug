from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

Usr = get_user_model()


def foo(request):
    import threading
    from time import time
    print 'Inside foo view (%s) at %s' % (threading.currentThread(), time())
    params = {}
    if request.method == 'POST':
        Group.objects.get(name='student')
        user = Usr(email='testa@ccc.com')
        user.set_password('test123')
        user.save()
        group = Group.objects.get(name='student')
        user.groups.add(group)
        params['did_it'] = user.email
    return render_to_response('polls/foo.html', params, context_instance=RequestContext(request))
