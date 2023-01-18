from rest_framework.test import APITestCase, force_authenticate, APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .models import Product, Comment
from django.urls import reverse
import json


class ProductsTests(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.username = 'aminm08'
        cls.email = 'maf081378@gmail.com'
        cls.password = 'testpass123'
        cls.user1 = get_user_model().objects.create_user(
            username=cls.username,
            email=cls.email,
            password=cls.password,
           
        )
        cls.token = Token.objects.create(user=cls.user1).key


        cls.product1 = Product.objects.create(
            title='jean pants',
            description='nothing new',
            price=100_000,
            discount=12,
            slug = 'jean-pants',

        )
        cls.comment1 = Comment.objects.create(
            author=cls.user1,
            product=cls.product1,
            body='first',
            rating='2'
        )


    def test_product_list_view_by_name(self):
        response = self.client.get(reverse('product_list'))
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['results'][0]['title'], 'jean pants')

    def test_product_list_view_by_url(self):
        
        response = self.client.get('/api/v1/products/')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['results'][0]['title'], 'jean pants')
    

    
    def test_product_detail_view_by_name(self):
        response = self.client.get(reverse('product_detail', args=[self.product1.pk]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['title'], 'jean pants')
    
    def test_product_detail_view_by_url(self):
        response = self.client.get('/api/v1/products/'+str(self.product1.pk)+'/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['title'], 'jean pants')
        
    def test_comment_create_view(self):
        client = APIClient()
        data = {'body':'comment 1','rating':'1'}
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        
        response = client.post(reverse('comment_create', args=[self.product1.pk]), data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(Comment.objects.count(), 2)
        self.assertEqual(Comment.objects.last().body, 'comment 1')
    
    def test_product_comments_view(self):
        response = self.client.get(reverse('product_comments', args=[self.product1.pk]))
        results = json.loads(response.content)['results'][0]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(results['body'], 'first')
        
        


        
