from django.urls import reverse, resolve
from django.test import TestCase
from .views import home, project_tasks, new_task
from .models import Project

class HomeTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(name='Django', description='Django board.')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_home_view_contains_link_to_tasks_page(self):
        project_tasks_url = reverse('project_tasks', kwargs={'pk': self.project.pk})
        self.assertContains(self.response, 'href="{0}"'.format(project_tasks_url))


class ProjectTasksTests(TestCase):
    def setUp(self):
        Project.objects.create(name='Django', description='Django Project.')

    def test_project_tasks_view_success_status_code(self):
        url = reverse('project_tasks', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_project_tasks_view_not_found_status_code(self):
        url = reverse('project_tasks', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_project_tasks_url_resolves_project_tasks_view(self):
        view = resolve('/projects/1/')
        self.assertEquals(view.func, project_tasks)

    def test_project_tasks_view_contains_link_back_to_homepage(self):
        project_tasks_url = reverse('project_tasks', kwargs={'pk': 1})
        response = self.client.get(project_tasks_url)
        homepage_url = reverse('home')
        self.assertContains(response, 'href="{0}"'.format(homepage_url))

    def test_project_tasks_view_contains_navigation_link(self):
        project_tasks_url = reverse('project_tasks', kwargs={'pk': 1})
        homepage_url = reverse('home')
        new_task_url = reverse('new_task', kwargs={'pk': 1})

        response = self.client.get(project_tasks_url)

        self.assertContains(response, 'href="{0}"'.format(homepage_url))
        self.assertContains(response, 'href="{0}"'.format(new_task_url))

class NewTaskTests(TestCase):
    def setUp(self):
        Project.objects.create(name='Django', description='Django board.')

    def test_new_task_view_success_status_code(self):
        url = reverse('new_task', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_new_task_view_not_found_status_code(self):
        url = reverse('new_task', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_new_task_url_resolves_new_topic_view(self):
        view = resolve('/projects/1/new/')
        self.assertEquals(view.func, new_task)

    def test_new_task_view_contains_link_back_to_project_tasks_view(self):
        new_task_url = reverse('new_task', kwargs={'pk': 1})
        project_tasks_url = reverse('project_tasks', kwargs={'pk': 1})
        response = self.client.get(new_task_url)
        self.assertContains(response, 'href="{0}"'.format(project_tasks_url))
