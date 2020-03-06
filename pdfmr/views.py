from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
import sys


# Create your views here.
def top(request):
    #post = get_object_or_404(Post, pk=pk)
    return render(request, 'pdfmr/top.html', {}) 

def link(request):
    #post = get_object_or_404(Post, pk=pk)
    return render(request, 'pdfmr/link.html', {}) 
def about(request):
    #post = get_object_or_404(Post, pk=pk)
    return render(request, 'pdfmr/contact.html', {}) 

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