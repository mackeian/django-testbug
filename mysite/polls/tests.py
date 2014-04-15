from django.conf import settings
from django.core.urlresolvers import reverse
from django.test import LiveServerTestCase
from splinter import Browser
from pyvirtualdisplay import Display
import threading
from time import time
from django.contrib.auth.models import Group

class LoginTests(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super(LoginTests, cls).setUpClass()
        # A virtual display is needed for build-server etc to run the tests
        cls.display = Display(visible=0, size=(1024, 768))
        cls.display.start()
        cls.browser = Browser('firefox')

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        cls.display.stop()
        super(LoginTests, cls).tearDownClass()

    def test_signup(self):
        Group.objects.create(name='student')
        url = reverse('polls.views.foo')
        print 'Accessing %s... (%s) at %s' % (url, threading.currentThread(), time())
        self.browser.visit('%s%s' % (self.live_server_url, url))
        self.browser.find_by_name('submit').first.click()
	assert 'Do it' in self.browser.html
	assert 'testa@ccc.com' in self.browser.html
