import unittest
from app.models import Articles


class TestArticles(unittest.TestCase):
    '''
    Test class to test the behavior of the articles class
    '''
    def setUp(self):
        '''
        Test class to run before other tests
        '''
        self.new_article = Articles(1,'habiba','Kenyan Man breaks world record','Kipchoge breaks the world record on 2 hour marathon','https://techtoday.com','https://marathons.com/images','2019-010-21T14:50:05Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.author,'habiba')
        self.assertEquals(self.new_article.title,'Kenyan Man breaks world record')
        self.assertEquals(self.new_article.description,'Kipchoge breaks the world record on 2 hour marathon')
        self.assertEquals(self.new_article.url,'https://techtoday.com')
        self.assertEquals(self.new_article.urlToImage,'https://marathons.com/images')
        self.assertEquals(self.new_article.publishedAt,'2019-010-21T14:50:05Z')


# class SourceTest(unittest.TestCase):
#    '''
#    Test case to test the behavior of the NewsSource class
#    '''
#    def setUp(self):
#        '''
#        Setup function that will run before every test
#        '''
#        self.new_source = Sources('KNYS','BBC','Latest news today','https://newscenteer.com','Sports','Kenya')
#    def test_instance(self):
#        self.assertTrue(isinstance(self.new_source,Sources))
#    def test_to_check_instance_variables(self):
#        '''
#        Test function to check instance variables
#        '''
#        self.assertEquals(self.new_source.id,'KNYS')
#        self.assertEquals(self.new_source.name,'BBC')
#        self.assertEquals(self.new_source.description,'Latest news today')
#        self.assertEquals(self.new_source.url,'https://newscenteer.com')
#        self.assertEquals(self.new_source.category,'Sports')
#        self.assertEquals(self.new_source.country,'Kenya')


if __name__ == '__main__':
    unittest.main()