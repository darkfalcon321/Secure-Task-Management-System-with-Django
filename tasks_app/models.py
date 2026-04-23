from django.db import models

# Create your models here.

status_choice = [
    ('Pending', 'Pending'),
    ('In Progress', 'In Progress'),
    ('Completed', 'Completed')
]

priority_choice = [
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High')
]

class Task(models.Model):
    
    title = models.CharField(max_length = 255)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(choices=status_choice, max_length = 12)
    priority = models.CharField(choices=priority_choice, max_length = 12)
    category = models.ForeignKey('category', on_delete = models.CASCADE)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(blank = True, null = True)
    
    def __str__(self):
        return self.name