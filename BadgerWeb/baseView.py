# coding=utf-8
"""
Created by 'badger' on '16/6/15'
"""

from django.shortcuts import render_to_response
from BadgerWeb import settings


def cus_render(template, context={}):
    siteTitle = 'Badger'

    # merge the dic of context and sit info, update default info.
    loc_dic = locals().copy()
    del loc_dic['context']
    loc_dic.update(context)
    print(loc_dic)

    return render_to_response(template, loc_dic)
