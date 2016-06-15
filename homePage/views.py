from BadgerWeb.baseView import cus_render
from django.shortcuts import render_to_response

def default(request):
    msg = 'nothing'
    return cus_render('homePage/default.html',locals())