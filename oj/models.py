from django.db import models
from datetime import datetime
# Create your models here.


class Problem(object):
    ''' COUNT '''
    def __str__(self):
        return "problem" + str(self.id)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    shortname = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    timelimit = models.IntegerField(default=0)
    memlimit = models.IntegerField(default=0)
    testpoint = models.IntegerField(default=0)
    invisible = models.BooleanField(default=False)
    create = models.TimeField


class Submit(object):
    def __str__(self):
        return "submit" + str(self.id)
    id = models.AutoField(primary_key=True)
    problem = models.ForeignKey(Problem)
    member = models.ForeignKey(Member)
    code = models.CharField(default="", max_length=200)
    status = models.IntegerField(default=0)
    testpoint = models.CharField(default="", max_length=200)
    testpoint_time = models.CharField(default="", max_length=200)
    testpoint_memory = models.CharField(default="", max_length=200)
    score = models.IntegerField(default=0)
    costtime = models.IntegerField(default=0)
    costmemory = models.IntegerField(default=0)
    timestamp = models.CharField(default="", max_length=200)
    lang = models.IntegerField(default=0)
    msg = models.CharField(default="", max_length=200)
    user_agent = models.CharField(default="", max_length=200)
    ip = models.CharField(default="", max_length=200)
    create = models.DateTimeField(default=datetime.now, )


class Question(models.Model):
    def __str__(self):              # __unicode__ on Python 2
        return self.question_text
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    def __str__(self):              # __unicode__ on Python 2
        return self.choice_text
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Member(models.Model):
    def __str__(self):
        return "member" + str(self.id)
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    username_lower = models.CharField
    password = models.CharField(max_length=200)
    email = models.EmailField(default="")
    website = models.CharField(default="", max_length=200)
    tagline = models.CharField(default="", max_length=200)
    bio = models.CharField(default="", max_length=200)
    gravatar_link = models.CharField(default="", max_length=200)
    create = models.DateTimeField(default=datetime.now, )
    admin = models.IntegerField(default=0)
    lang = models.IntegerField(default=1)


class Auth(models.Model):
    def __str__(self):
        return "auth" + self.secret
    member = models.OneToOneField(Member)
    secret = models.CharField(default="", max_length=200)
    create = models.DateTimeField(default=datetime.now)


class Author(models.Model):
    name = models.CharField(max_length=200)

    # def get_absolute_url(self):
    #     return reverse('author-detail', kwargs={'pk': self.pk})