from django.shortcuts import render, redirect
# import login_required decorator
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.utils.decorators import method_decorator
from django.views import View

# Create your views here.
from .models import Announcement
from .forms import AnnouncementForm

# our test function here.
def is_teacher(user):
    # the user object is passed in here by the decorator
    return user.role == 'teacher'

# @login_required
@method_decorator(login_required, name="dispatch")
class AnnouncementListView(View):
    def get(self, request):
        announcements = Announcement.objects.all().order_by('-created_at')
        return render(
            request,
            'announcements/announcement_list.html',
            {'announcements': announcements}
        )

# this will restrict access to only users that pass the is_teacher test
# it will redirect to the login page if the user does not have permission.
@method_decorator(login_required, name="dispatch")
@method_decorator(user_passes_test(is_teacher, login_url='login'), name="dispatch")
# @permission_required('announcements.add_announcement', raise_exception=True) # the optional section
class CreateAnnouncementView(View):
    template_name = 'announcements/create_announcement.html'
    form_class = AnnouncementForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            announcement = form.save(commit=False)
            # the commit false will prevent the form from saving to the database
            # set the created_by field to the current user
            announcement.created_by = request.user
            announcement.save()
            # save the announcement to the database.
            return redirect('announcement_list')
        return render(request, self.template_name, {'form': form})