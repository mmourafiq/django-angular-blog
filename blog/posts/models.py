from django.db import models
from django.template.defaultfilters import slugify


class Post(models.Model):
    """
    An item created by a user.
    """
    author = models.ForeignKey('auth.User', related_name='posts')
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField(blank=True, help_text=(
        "If omitted, the description will be the post's title."))
    is_active = models.BooleanField(default=True, blank=True)
    tags = models.ManyToManyField('tags.Tag', related_name='posts')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.do_unique_slug()
        if not self.description:
            self.description = self.title
        super(Post, self).save(*args, **kwargs)

    def do_unique_slug(self):
        """
        Ensures that the slug is always unique for this post
        """
        if not self.id:
            # make sure we have a slug first
            if not len(self.slug.strip()):
                self.slug = slugify(self.title)

            self.slug = self.get_unique_slug(self.slug)
            return True

        return False

    def get_unique_slug(self, slug):
        """
        Iterates until a unique slug is found
        """
        orig_slug = slug
        counter = 1

        while True:
            posts = Post.objects.filter(slug=slug)
            if not posts.exists():
                return slug

            slug = '%s-%s' % (orig_slug, counter)
            counter += 1