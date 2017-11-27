from django.test import TestCase
from .models import Editor,Article,tags
import datetime as dt

# Create your tests here.

class EditorTestClass(TestCase):
    #setup method
    def setUp(self):
        self.James=Editor(first_name='James',last_name='Doe',email='james@moringa.com')

    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.James,Editor))

    def test_save_method(self):
        self.James.save_editor()
        editors=Editor.objects.all()
        self.assertTrue(len(editors)>0)

    def test_del_method(self):
        user=Editor.objects.filter(id = 1)
        # self.user.del_editor()
        editors=Editor.objects.all()
        self.assertTrue(len(editors)==0)

class ArticleTestClass(TestCase):
    # def setUp(self):
    #     self.James=Editor(first_name='James',last_name='Doe',email='james@moringa.com')
    #     self.art1=Article(title='the big bang theory',post='sdfsf ssdfsd fsfs d',editor=self.James,tag=1)
    #
    # def test_save(self):
    #     self.James.save_editor()
    #     self.art1.save_article()
    #     articles=Article.objects.all()
    #     self.assertTrue(len(articles)>0)
    def setUp(self):
        # Creating a new editor and saving it
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
        self.new_article.save()

        self.new_article.tag.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        today_news=Article.todays_news()
        self.assertTrue(len(today_news)>0)

    def test_get_news_by_date(self):
        test_date='2017-03-17'
        date=dt.datetime.strptime(test_date,'%Y-%m-%d').date()
        news_by_date=Article.days_news(date)
        self.assertTrue(len(news_by_date==0))
