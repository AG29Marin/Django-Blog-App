from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post

# Create your tests here.

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user (
            username = "testuser",
            email= "test@email.com",
            password = "secret"
        ) 

        cls.post = Post.objects.create( 
            title = "Some title",
            body = "Some content",
            author = cls.user
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, "Some title")
        self.assertEqual(self.post.body, "Some content")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "Some title")
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")

    def test_url_exists_at_current_location_listview(self): # Change the name of the function because it's a pain
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
