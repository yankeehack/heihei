__author__ = 'yazhu'
from django.utils.translation import ugettext_lazy
from django.utils.html import escape
from oj.models import Auth, Member
from datetime import datetime
import binascii
import uuid
from django.utils.translation import get_language


class htmlMixin(object):
    _ = lambda self, text: ugettext_lazy(text) # i18n func
    xhtml_escape = lambda self, text: escape(text) if text else text # xhtml escape


class authMixin(object):
    cookies_to_set={}

    def create_auth(self, member):
        random = binascii.b2a_hex(uuid.uuid4().bytes)
        authNew = Auth(member=member, secret=random, create=datetime.now())
        authNew.save()
        self.cookies_to_set['auth'] = random
        self.cookies_to_set['uid'] = member.id
        return random


class userMixin(authMixin):

    def get_user_locale(self):

        '''Get user locale, first check cookie, then browser'''

        result = self.request.COOKIES.get('LANG', default = None)
        if result == None:
            result = get_language()

        return result

    def get_current_user(self):

        '''Check user is logined'''

        auth = self.request.COOKIES.get("auth")
        member_id = self.request.COOKIES.get("uid")
        member = None
        if auth and member_id:
            auth = Auth.objects.all().filter(secret=auth).filter(member_id=member_id).get()
            if auth:
                member = Member.objects.all().get(id=auth.member_id)
                if member:
                    #TODO will need to consider timezone difference in the future
                    delta = auth.create.replace(tzinfo=None) - datetime.now().replace(tzinfo=None)
                    if delta.days > 20:
                        """ Refresh Token """
                        auth.delete()
                        random = self.create_auth(member)
                        self.cookies_to_set['athu'] = random
                        self.cookies_to_set['uid'] = str(member_id)
                        auth.save()

        return member

    # This function is a shortcut for debug
    def clear_auth_cookies(self, response):
        auth = self.request.COOKIES.get("auth")
        member_id = self.request.COOKIES.get("uid")
        auth = Auth.objects.all().filter(secret=auth).filter(member_id=member_id).get()
        auth.delete() # always clear db's auth
        response.delete_cookie("auth")
        response.delete_cookie("uid")
