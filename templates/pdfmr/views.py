from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

# Create your views here.
def top(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'pdfmr/top.html', {'post': post}) 