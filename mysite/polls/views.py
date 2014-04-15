from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User, Group


def foo(request):
    import threading
    from time import time
    print 'Inside foo view (%s) at %s' % (threading.currentThread(), time())
    params = {}
    if request.method == 'POST':
        foo_group = Group.objects.create(name='Foo')
        Group.objects.get(name='student')
        user = User(email='testa@ccc.com')
        user.set_password('test123')
        user.save()
        group = Group.objects.get(name='student')
        user.groups.add(group)
        params['did_it'] = user
    return render_to_response('polls/foo.html', params, context_instance=RequestContext(request))