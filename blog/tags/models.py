from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify


class Tag(models.Model):
    slug = models.SlugField(max_length=100, verbose_name=_('slug'), blank=True)
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s" % self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)