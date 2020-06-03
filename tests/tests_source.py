from app.models import Sources

class TestSources(unittest.TestCase):
   '''
   Test case to test the behavior of the NewsSource class
   '''
   def setUp(self):
       '''
       Setup function that will run before every test
       '''
       self.new_source = Sources('KNYS','BBC','Latest news today','https://newscenteer.com','Sports','Kenya')
   def test_instance(self):
       self.assertTrue(isinstance(self.new_source,Sources))
   def test_to_check_instance_variables(self):
       '''
       Test function to check instance variables
       '''
       self.assertEquals(self.new_source.id,'KNYS')
       self.assertEquals(self.new_source.name,'BBC')
       self.assertEquals(self.new_source.description,'Latest news today')
       self.assertEquals(self.new_source.url,'https://newscenteer.com')
       self.assertEquals(self.new_source.category,'Sports')
       self.assertEquals(self.new_source.country,'Kenya')


if __name__ == '__main__':
    unittest.main()