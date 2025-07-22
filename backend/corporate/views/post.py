from django.views.generic import DetailView, ListView
from sage_blog.models import Post, PostCategory, PostTag
from sage_blog.views.mixins import PaginatedMixin, SageBlogContextMixin, SearchableMixin
from sage_blog.filters.post import PostFilter


class PostListView(SageBlogContextMixin, PaginatedMixin, SearchableMixin, ListView):
    model = Post
    template_name = "pages/blog/list.html"
    context_object_name = "blog_posts"
    paginate_by = 10
    page_title = "Blog Posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blog_recent_posts"] = Post.objects.filter_actives().filter_recent_posts()
        context["blog_categories"] = PostCategory.objects.filter(is_published=True).annotate_total_posts()
        context["blog_trend_tags"] = PostTag.objects.annotate_total_posts().filter_trend_tags(
            days_ago=0, min_count=1, limit=5
        )
        return context

    def get_queryset(self):
        """
        Method docstring: Describe what this method does.
        """
        qs = super().get_queryset().filter_actives()
        query_params = self.request.GET.copy()
        search_query = query_params.pop("search", "")

        if search_query:
            qs = qs.heavy_search(search_query[0])

        qs = self.filter_by_query_params(query_params, qs)
        return qs

    def filter_by_query_params(self, query_params, qs):
        """
        Method docstring: Describe what this method does.
        """
        if query_params:
            filtered_qs = PostFilter(query_params, queryset=qs)
            qs = filtered_qs.qs.filter_actives()
        return qs


class PostDetailView(SageBlogContextMixin, DetailView):
    model = Post
    template_name = "pages/blog/detail.html"
    context_object_name = "post"
    page_title = "Blog Posts"

    def get_queryset(self):
        # Customize the queryset to show only active posts
        queryset = super().get_queryset().filter_actives().annotate_next_and_prev()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blog_recent_posts"] = Post.objects.filter_actives().filter_recent_posts()
        context["blog_categories"] = PostCategory.objects.filter(is_published=True).annotate_total_posts()
        context["blog_trend_tags"] = PostTag.objects.filter_trend_tags(
            days_ago=0, min_count=1, limit=5
        )
        return context
