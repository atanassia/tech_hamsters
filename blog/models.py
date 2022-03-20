from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

from django.utils import timezone


# class PublishedManager(models.Manager):
# 	def get_queryset(self):
# 		return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
	# STATUS_CHOICES = (
	# 	('draft', 'Черновик'),
	# 	('published', 'Опубликовано'),
	# )
	title = models.CharField(max_length=250, verbose_name='Название')
	slug = models.SlugField(max_length=250, unique_for_date='publish', verbose_name='Слаг')
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name='Автор')
	body = RichTextField(blank=True, null=True, verbose_name='Тело')
	publish = models.DateTimeField(default=timezone.now, verbose_name='Опубликовано')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	# status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name='Статус')
	# objects = models.Manager()
	# published = PublishedManager()
	# tags = TaggableManager()


	class Meta:
		verbose_name_plural = "Посты"
		verbose_name = "Пост"
		ordering = ('-publish',)
	
	def __str__(self):
		return self.title

	# def get_absolute_url(self):
	# 	return reverse('blog:post_detail',
	# 		args=[self.publish.year,
	# 			  self.publish.month,
	# 			  self.publish.day,
	# 			  self.slug])
