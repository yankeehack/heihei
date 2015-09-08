__author__ = 'yazhu'
from oj.base.mixins import htmlMixin, userMixin
from django.views import generic
from oj.models import Member
from oj.base import unauthenticated



class EntryView(userMixin, htmlMixin, generic.CreateView):
    model = Member

    def set_cookies(self, response):
        for key, value in self.cookies_to_set.iteritems():
            response.set_cookie(key, value)
        return response

    def get_context_data(self, **kwargs):
        context = super(generic.CreateView, self).get_context_data(**kwargs)
        context['_'] = self._
        return context

    @unauthenticated
    def get(self, request, *args, **kwargs):
        return super(generic.CreateView, self).get(request, *args, **kwargs)

    @unauthenticated
    def post(self, request, *args, **kwargs):
        '''Overriding rendering part to add cookies'''
        return super(generic.CreateView, self).post(request, *args, **kwargs)


class BaseTemplateView(userMixin, htmlMixin, generic.TemplateView):

    def get_page_count(self, count, pre = 10):

        '''Return page num by input item num'''

        return count / pre + (1 if count % pre else 0)

    def sendmail(self):
        '''Send mail func, send mail to someone'''
        pass

    def render_to_response(self, context, **args):
        if "self" in args.keys():
            args.pop("self")
        context['_'] = self._
        response = super(BaseTemplateView, self).render_to_response(context, **args)

        return response

        # def write_error(self, status_code, **kwargs):
        #     '''Rewrite write_error for custom error page'''
        #     if status_code == 404:
        #         self.render_to_response("404.html")
        #         return
        #     elif status_code == 500:
        #         error = []
        #         for line in traceback.format_exception(*kwargs['exc_info']):
        #             error.append(line)
        #         error = "\n".join(error)
        #         self.render_to_response("500.html", locals())
        #         return
        #     msg = httplib.responses[status_code]
        #     self.render_to_response("error.html", locals())

        # def check_text_value(self, value, valName, required = False, max = 65535, min = 0, regex = None, regex_msg = None, is_num = False, vaild = []):
        #     ''' Common Check Text Value Function '''
        #     error = []
        #     if not value:
        #         if required:
        #             error.append(self._("%s is required") % valName)
        #         return error
        #     if is_num:
        #         try:
        #             tmp = int(value)
        #         except ValueError:
        #             return [self._("%s must be a number.") % valName]
        #         else:
        #             if vaild and tmp not in vaild:
        #                 return [self._("%s is invalid.") % valName]
        #             return []
        #     if len(value) > max:
        #         error.append(self._("%s is too long.") % valName)
        #     elif len(value) < min:
        #         error.append(self._("%s is too short.") % valName)
        #     if regex:
        #         if not regex.match(value):
        #             if regex_msg:
        #                 error.append(regex_msg)
        #             else:
        #                 error.append(self._("%s is invalid.") % valName)
        #     elif vaild and value not in vaild:
        #         error.append(self._("%s is invalid.") % valName)
        #     return error
        #
        # def check_username(self, usr, queryDB = False):
        #     error = []
        #     error.extend(self.check_text_value(usr, self._("Username"), required = True, max = 20, min = 3, \
        #                                        regex = re.compile(r'^([\w\d]*)$'), \
        #                                        regex_msg = self._("A username can only contain letters and digits.")))
        #     if not error and queryDB:
        #         try:
        #             query = self.select_member_by_username_lower(usr.lower())
        #         except NoResultFound:
        #             pass
        #         else:
        #             error.append(self._("That username is taken. Please choose another."))
        #     return error
        #
        # def check_password(self, pwd):
        #     return self.check_text_value(pwd, self._("Password"), required = True, max = 32, min = 6)
        #
        # def check_email(self, email, queryDB = False):
        #     error = []
        #     error.extend(self.check_text_value(email, self._("E-mail"), required = True, max = 100, min = 3, \
        #                                        regex = re.compile(r"(?:^|\s)[-a-z0-9_.+]+@(?:[-a-z0-9]+\.)+[a-z]{2,6}(?:\s|$)", re.IGNORECASE), \
        #                                        regex_msg = self._("Your Email address is invalid.")))
        #     if not error and queryDB:
        #         try:
        #             query = self.select_member_by_email(email)
        #         except NoResultFound:
        #             pass
        #         else:
        #             error.append(self._("That Email is taken. Please choose another."))
        #     return error
        #
        # def get_gravatar_url(self, email):
        #     gravatar_id = hashlib.md5(email.lower()).hexdigest()
        #     return "http://www.gravatar.com/avatar/%s?d=mm" % (gravatar_id)
        #
        # def post_to_judger(self, query, judger, callback = None):
        #     query["time"] = time.time()
        #     query["code"] = query["code"].decode("utf-8")
        #     query = dict(sorted(query.iteritems(), key=itemgetter(1)))
        #     jsondump = json.dumps(query)
        #     sign = hashlib.sha1(jsondump + judger.pubkey.strip()).hexdigest()
        #     query["sign"] = sign
        #     http_client = AsyncHTTPClient()
        #     http_client.fetch(judger.path, method = "POST", body = urllib.urlencode({"query" : json.dumps(query)}), callback = callback)
        #
        # def highlight_code(self, code, lang):
        #     #return highlight(code, CODE_LEXER[lang](), HtmlFormatter(linenos = True))
        #     codestr = highlight(code, CODE_LEXER[lang](), HtmlFormatter(nowrap = True))
        #     table = '<div class="highlight"><table><tr><td class="gutter"><pre class="line-numbers">'
        #     code = ''
        #     lines = codestr.split("\n")
        #     for index, line in zip(range(len(lines)), lines):
        #         table  +=  "<span class='line-number'>%d</span>\n" % (index + 1)
        #         code   +=  "<span class='line'>%s</span>\n" % line
        #     table  +=  "</pre></td><td class='code'><pre><code class='%s'>%s</code></pre></td></tr></table></div>" % (CODE_LANG[lang], code)
        #     return table
        #
        # @property
        # def db(self):
        #     return self.application.db
        # @property
        # def jinja2(self):
        #     return self.application.jinja2