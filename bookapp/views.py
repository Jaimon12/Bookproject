from django.shortcuts import redirect, render
from bookapp.models import Book
from bookapp.forms import BookForm
# Create your views here.
def add_book(request):
    if request.method=="POST":
        title=request.POST.get('title')
        author=request.POST.get('author')
        desc=request.POST.get('desc')
        published_year=request.POST.get(' published_year')
        img=request.FILES['img']
        book=Book(title=title,desc=desc,author=author,published_year= published_year,img=img)
        book.save()
    return render(request,'add.html')
def index(request):
    # Retrieve all books from the database
    book_list = Book.objects.all()
    context = {'book_list': book_list}
    return render(request, 'book.html', context)

def detail(request,book_id):
    book=Book.objects.get(id=book_id)
    return render(request,"detail.html",{'book':book})

def delete(request,id):
    if request.method=="POST":
       book=Book.objects.get(id=id)
       book.delete()
       return redirect('/')
    return render(request, 'delete.html')
def update(request,id):
    book=Book.objects.get(id=id)
    form=BookForm(request.POST or None, request.FILES,instance=book)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form,'book': book})