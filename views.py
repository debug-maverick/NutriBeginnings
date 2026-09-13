from django.contrib import messages
from django.db.models import Avg, Min, Max
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProgressForm, BlogForm
from .models import Progress, Blog


def dashboard(request):
    progress = list(Progress.objects.order_by("date"))
    recent_progress = Progress.objects.all()[:5]
    blogs = Blog.objects.all()[:3]

    context = {
        "progress_count": Progress.objects.count(),
        "blog_count": Blog.objects.count(),
        "avg_weight": Progress.objects.aggregate(v=Avg("weight"))["v"],
        "latest": Progress.objects.first(),
        "recent_progress": recent_progress,
        "blogs": blogs,
        "chart_labels": [p.date.strftime("%d %b") for p in progress],
        "chart_weights": [float(p.weight) for p in progress],
        "chart_calories": [p.calories for p in progress],
    }
    return render(request, "dashboard.html", context)


def progress_list(request):
    query = request.GET.get("q", "").strip()
    items = Progress.objects.all()
    if query:
        items = items.filter(notes__icontains=query)
    return render(request, "progress/list.html", {"items": items, "query": query})


def progress_create(request):
    form = ProgressForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Progress entry added successfully.")
        return redirect("progress_list")
    return render(request, "progress/form.html", {"form": form, "title": "Add Progress"})


def progress_update(request, pk):
    item = get_object_or_404(Progress, pk=pk)
    form = ProgressForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        messages.success(request, "Progress entry updated.")
        return redirect("progress_list")
    return render(request, "progress/form.html", {"form": form, "title": "Edit Progress"})


def progress_delete(request, pk):
    item = get_object_or_404(Progress, pk=pk)
    if request.method == "POST":
        item.delete()
        messages.success(request, "Progress entry deleted.")
        return redirect("progress_list")
    return render(request, "progress/delete.html", {"item": item})


def blog_list(request):
    query = request.GET.get("q", "").strip()
    posts = Blog.objects.all()
    if query:
        posts = posts.filter(title__icontains=query) | posts.filter(content__icontains=query)
    return render(request, "blogs/list.html", {"posts": posts, "query": query})


def blog_detail(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    return render(request, "blogs/detail.html", {"post": post})


def blog_create(request):
    form = BlogForm(request.POST or None)
    if form.is_valid():
        post = form.save()
        messages.success(request, "Blog published.")
        return redirect("blog_detail", pk=post.pk)
    return render(request, "blogs/form.html", {"form": form, "title": "Create Blog"})


def blog_update(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    form = BlogForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, "Blog updated.")
        return redirect("blog_detail", pk=post.pk)
    return render(request, "blogs/form.html", {"form": form, "title": "Edit Blog"})


def blog_delete(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        post.delete()
        messages.success(request, "Blog deleted.")
        return redirect("blog_list")
    return render(request, "blogs/delete.html", {"post": post})
