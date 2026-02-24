from django.db import models


# our model for the client
class Company(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    location = models.CharField(max_length=100, null=True)
    industry = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True, null=True, default="")
    created_at = models.DateTimeField(auto_now_add=True) # Automatically set the field to the current date and time
    updated_at = models.DateTimeField(auto_now=True) # Automatically sets the field to the current datetime when updated
    url = models.URLField(null=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True, default="")

    created_at = models.DateTimeField(auto_now_add=True) # Automatically set the field to the current date and time
    updated_at = models.DateTimeField(auto_now=True) # Automatically sets the field to the current datetime when updated

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)

    created_at = models.DateTimeField(auto_now_add=True) # Automatically set the field to the current date and time
    updated_at = models.DateTimeField(auto_now=True) # Automatically sets the field to the current datetime when updated

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees') # plural and references this table
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, blank=True, null=True, related_name='employees')

    def __str__(self):
        return f"{self.first_name} {self.last_name} works at {self.company.name} as a {self.role.name}"


'''

    # date fields
    # the auto_now_add Automatically set the date when the record is created
    date_joined = models.DateField(auto_now_add=True)
    # the
    updated_at = models.DateField(auto_now=True)

'''