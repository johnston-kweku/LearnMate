from django.contrib.sitemaps import Sitemap
from learning_logs.models import Topic

class TopicSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return Topic.objects.all()

    def lastmod(self, obj):
        return obj.date_added
