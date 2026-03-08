from django.db import models
# 
# define student and course modles

class Student(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

class Course(models.Model):
    title = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, related_name="courses")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"


class Book(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    number_of_pages = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publiched_date = models.DateField()

    def save(self, *args, **kwargs):
        self.slug = self.title.lower().replace(" ", "-")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    class Meta:
        db_table = "library_books"
        verbose_name = "Book"
        indexing = ["title"]
        verbose_name_plural = "Books"
        constraints = [
            models.CheckConstraint(check=models.Q(number_of_pages__gt=0), name="number_of_pages_gt_0"),
            models.CheckConstraint(check=models.Q(price__gt=0), name="price_gt_0")
        ]
        ordering = ["-publiched_date"]


class Author(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    buirth_date = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"




class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        # constrin
        constraints = [
            models.UniqueConstraint(fields=["slug"], name="unique_slug")
        ]

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    status = models.CharField(max_length=20, choices=[("draft", "Draft"), ("published", "Published"), ("archived", "Archived")], default="draft")
    views_count = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, related_name="posts")
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    # published_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        constraints = [
            models.UniqueConstraint(fields=["slug"], name="unique_slug"),
            models.UniqueConstraint(fields=["slug", "author"], name="unique_slug_author"),
            models.CheckConstraint(check=models.Q(views_count__gte=0), name="views_count_gte_0")
        ]
        ordering = ["-created_at"]
        indexs = [
            models.Index(fields=["slug"]),
            models.Index(fields=["status", "created_at"])
        ]
    # get_absolute_url = models.URLField()
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("post_detail", kwargs={"slug": self.slug})

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="comments")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"
    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ["created_at"]