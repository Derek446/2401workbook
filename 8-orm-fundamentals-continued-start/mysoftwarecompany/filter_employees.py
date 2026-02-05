import os
import django

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysoftwarecompany.settings')
django.setup()

# Note place your imports below and do not remove the above lines
##### YOUR CODE BELOW THIS LINE #####


# in the shell, this will find employees created after cutoff
from clients.models import Employee
from datetime import datetime, date
# from django.utils import timezone

all_employees = Employee.objects.all()
employees_filtered = Employee.objects.filter(created_at__date__gt=date(2026, 2, 3))
print(employees_filtered)

# cutoff = timezone.make_aware(datetime(2026, 2, 3))
# adding date causes it to ignore other stuff

# employees = Employee.objects.filter(created_at__gt=cutoff)
# print(employees)