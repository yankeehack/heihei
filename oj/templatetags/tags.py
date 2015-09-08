__author__ = 'yazhu'
from django import template
from datetime import  datetime

register = template.Library()

CONTEST_STATUS = {
    1 : ("success", "Running"),
    2 : ("info", "Waiting"),
    3 : ("default", "Finished"),
    4 : ("warning", "Invisible"),
    5 : ("important", "Unknown"),
    }

SUBMIT_STATUS  = {
    0 : ("info", "Pending"),
    1 : ("success", "Accepted"),
    2 : ("important", "Wrong Answer"),
    3 : ("warning", "Time Limit Exceeded"),
    4 : ("warning", "Memory Limit Exceeded"),
    5 : ("inverse", "Runtime Error"),
    6 : ("default", "Compile Error"),
    7 : ("default", "No Output"),
    }


@register.filter(name='avatar_img')
def avatar_img(link, size = 45):
    if link != "/static/img/avatar.png":
        link = link + "&s=100"
    return "<img src=\"%s\" width=\"%d\" height=\"%d\" />" % (link, size, size)

@register.filter(name='lang2humantext')
def lang2humantext(lang):
    if lang == 1:
        return "Pascal"
    elif lang == 2:
        return "C"
    elif lang == 3:
        return "C++"

@register.filter(name='get_submit_status')
def get_submit_status(submit):
    if not submit:
        return "-"
    cla, status = SUBMIT_STATUS[submit.status]
    return "<span class=\"label label-%s\">%s</span>" % (cla, status)

@register.filter(name='get_contest_status')
def get_contest_status(contest):
    return "<span class=\"label label-%s\">%s</span>" % (CONTEST_STATUS[contest.status])

@register.inclusion_tag('macros/show_error_list.html')
def show_error_list(error):
    return {'error': error}

@register.inclusion_tag('macros/show_problem_list.html')
def show_problem_list(problem):
    return {'problem': problem}

@register.inclusion_tag('macros/show_contest_list.html')
def show_contest_list(contest):
    return {'contest': contest}
