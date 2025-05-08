from apps.category.models import Category, Tag


def global_context(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        'categories': categories,
        'tags': tags,
    }

    return context
