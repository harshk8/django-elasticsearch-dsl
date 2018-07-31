# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from elastic_app.documents import PostDocument

def search(request):

	s_key = request.GET.get('abc')

	if s_key:
		posts = PostDocument.search().query("multi_match", query=s_key, type='cross_fields', fields=['title', 'description'])
	else:
		posts = ''

	return render(request, 'elastic_app/search.html', {'posts': posts})