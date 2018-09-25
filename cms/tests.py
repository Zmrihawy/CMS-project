from django.contrib.auth.models import Permission, User
from django.test import TestCase
from django.urls import reverse

from django.contrib.auth.models import Group
from cms.models import Post


class PostTest(TestCase):
    def add_permission(self, codename, user=None):
        user = self.user if not user else user
        permission = Permission.objects.get(codename=codename)
        user.user_permissions.add(permission)

    def setUp(self):
        self.post = Post.objects.create(
            title='TITLE',
            content='CONTENT',
        )
        self.username = 'TEST_USER'
        self.password = 'TEST_PASS'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.client.login(username=self.username, password=self.password)

    def test_str(self):
        self.assertEqual(str(self.post), self.post.title)

    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)

    #def test_add_permissions(self):
     #   response = self.client.get(reverse('resource_form'))
      #  self.assertNotEqual(response.status_code, 200)
       # self.add_permission('add_resource')
        #self.assertEqual(response.status_code, 200)

    def test_draft_list_view(self):
        response = self.client.get(reverse('draft_list'))
        self.assertEquals(response.status_code, 200)

    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 200)

    def test_publish_post_view(self):
        response = self.user.groups.filter(name='editor').exists()
        self.assertEquals(response, False)
        Group.objects.create(name='editor')
        group = Group.objects.get(name='editor')
        self.user.groups.add(group)
        response = self.user.groups.filter(name='editor').exists()
        self.assertEquals(response, True)

