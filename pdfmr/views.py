from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
import sys


# Create your views here.
def top(request):
    #post = get_object_or_404(Post, pk=pk)
    all_posts = Post.objects.filter(published_date__lte=timezone.now())
    posts = all_posts.order_by('created_date').reverse()[:5]
    return render(request, 'pdfmr/top.html', {'posts': posts}) 

def link(request):
    #post = get_object_or_404(Post, pk=pk)
    return render(request, 'pdfmr/link.html', {}) 
def about(request):
    #post = get_object_or_404(Post, pk=pk)
    return render(request, 'pdfmr/contact.html', {}) 
def post(request):
    #post = get_object_or_404(Post, pk=pk)
    all_posts = Post.objects.filter(published_date__lte=timezone.now())
    posts = all_posts.order_by('created_date').reverse()
    return render(request, 'pdfmr/post_list.html', {'posts': posts}) 
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'pdfmr/post_detail.html', {'post': post})


def giants(request):
    #post = get_object_or_404(Post, pk=pk)
    return render(request, 'pdfmr/giants.html', {}) 
def tigers(request):
    #post = get_object_or_404(Post, pk=pk)
    return render(request, 'pdfmr/tigers.html', {}) 
def baystars(request):
    #post = get_object_or_404(Post, pk=pk)
    return render(request, 'pdfmr/baystars.html', {}) 
def dragons(request):
    #post = get_object_or_404(Post, pk=pk)
    return render(request, 'pdfmr/dragons.html', {}) 
def carp(request):
    #post = get_object_or_404(Post, pk=pk)
    return render(request, 'pdfmr/carp.html', {}) 
def swallows(request):
    #post = get_object_or_404(Post, pk=pk)
    return render(request, 'pdfmr/swallows.html', {}) 
def hawks(request):
    #post = get_object_or_404(Post, pk=pk)
    return render(request, 'pdfmr/hawks.html', {}) 
def lions(request):
    #post = get_object_or_404(Post, pk=pk)
    return render(request, 'pdfmr/lions.html', {}) 
def eagles(request):
    #post = get_object_or_404(Post, pk=pk)
    return render(request, 'pdfmr/eagles.html', {}) 
def buffaloes(request):
    #post = get_object_or_404(Post, pk=pk)
    return render(request, 'pdfmr/buffaloes.html', {}) 
def marines(request):
    #post = get_object_or_404(Post, pk=pk)
    return render(request, 'pdfmr/marines.html', {}) 
def fighters(request):
    #post = get_object_or_404(Post, pk=pk)
    return render(request, 'pdfmr/fighters.html', {}) 