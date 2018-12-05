from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from accounts import views as accounts_views
from prmanage import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^projects/(?P<pk>\d+)/$', views.project_tasks, name='project_tasks'),
    url(r'^projects/(?P<pk>\d+)/new/$', views.new_task, name='new_task'),
    url(r'^admin/', admin.site.urls),
    url(r'^reset/$',
        auth_views.PasswordResetView.as_view(
            template_name='password_reset.html',
            email_template_name='password_reset_email.html',
            subject_template_name='password_reset_subject.txt'
        ),
        name='password_reset'),
    url(r'^reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),
    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
        name='password_change'),
    url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
        name='password_change_done'),
    url(r'^projects/(?P<pk>\d+)/tasks/(?P<task_pk>\d+)/$', views.task_employees, name='task_employees'),
    url(r'^employee/create/$', views.create_employee, name='create_employee'),
    url(r'^employee/$', views.list_employee, name='list_employee'),
    url(r'^employee/assign/$', views.assign_employee, name='assign_employee'),
    url(r'^projects/new/$', views.new_project, name='new_project'),
    url(r'^projects/assign/$', views.assign_pm, name='assign_pm'),
    url(r'^employee/assign/new$', views.save_employee_task, name='save_employee_task'),
    url(r'^tasks/(?P<pk>\d+)/edit/$', views.TaskUpdateView.as_view(), name='edit_task'),
    url(r'^tasks/(?P<pk>\d+)/delete/$', views.TaskDeleteView.as_view(), name='delete_task'),
]
