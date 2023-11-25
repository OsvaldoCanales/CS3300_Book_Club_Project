from django.test import TestCase
from django.contrib.auth.models import User
from book_app.models import Member, Book, Catalog

#This tests whether if the member's name is returned properly
class MemberModelTest(TestCase):
    def setUp(self):
        #Create a member for testing
        self.user = User.objects.create_user(username ='testuser', email= 'testuser@gmail.com', password= 'Colorado123' )
        self.member = Member.objects.create(name = 'test Member100', email = 'testuser@gmail.com', user = self.user) 
       
    def test_member_str(self):
        #Test that the _str_method returns the name of the member
        self.assertEqual(str(self.member), 'test Member100')

class BookModelTest(TestCase):
    def setUp(self):
        # Create a user 
        self.user = User.objects.create_user(username='testuser', email='testuser@gmail.com', password='Colorado123')
        #Create a catalog
        self.catalog = Catalog.objects.create(title='Test Catalog', genre='Test Genre', about='Test About', member=self.user)
        #Create a member
        self.member = Member.objects.create(name='Test Member', email='testmember@gmail.com', catalog=self.catalog, user=self.user)

    def test_book_creation(self):
        # Create a book instance
        book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            publication_date='2022-01-01',
            description='Test Description',
            is_active=True,
            review='Test Review',
            catalog=self.catalog
        )

        # Retrieve the book from the database
        saved_book = Book.objects.get(title='Test Book')

        # Test whether the saved book matches the created book
        self.assertEqual(saved_book.title, 'Test Book')
        self.assertEqual(saved_book.author, 'Test Author')
        # Add more assertions based on your model fields

    def test_book_str(self):
        # Create a book instance
        book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            publication_date='2022-01-01',
            description='Test Description',
            is_active=True,
            review='Test Review',
            catalog=self.catalog
        )

        # Test the __str__ method of the Book model
        self.assertEqual(str(book), 'Test Book')