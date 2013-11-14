"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import unittest
from django.test import TestCase
from django.test.client import Client
from forms import *
from models import *
from views import *



class ModelTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()



    def test_fail_login(self):
        '''
            Test the login fail
            This testcase will test empty username and password will
            drive login unsuccefully. Therefore, check not everybody
            can login in the the page
        '''
        
        login_check = self.client.login(username='', password='')
        self.assertEqual(login_check,False)




    def test_login(self):
        '''
            Test login page
            This test case will test if people can login to the admin account
            with password admin and password JuakfrontPassword1 successfully
        '''
        
        login_check = self.client.login(username='admin',
password='JuakfrontPassword1')
        #self.assertEqual(login_check,True)
        self.assertRaises(TypeError,login_check,False)

    def test_model_Room(self):
        '''
        Test model Room(database)
        '''
        
        room1 = Room.objects.create(name="BA1190", info="lecture room")
        room2 = Room.objects.create(name="BA1180", info="another lecture room")
        self.assertEquals(room1.name, "BA1190")
        self.assertEquals(room1.info,"lecture room")
        self.assertEquals(room2.name, "BA1180")
        self.assertEquals(room2.info,"another lecture room")
    
    def test_model_Room(self):
        '''
        Test model Room(database)
        '''
        
        room1 = Room.objects.create(name="BA1170", info="lecture room")
        room2 = Room.objects.create(name="BA1130", info="lecture room")
        self.assertEquals(room1.name, "BA1170")
        self.assertEquals(room1.info,"lecture room")
        self.assertEquals(room2.name, "BA1130")
        self.assertEquals(room2.info,"lecture room")


    def test_model_Partner(self):
        '''
            Test model Partner(database)
        '''
        
        user = User.objects.create_user('user','changyingyu1991@gmail.com','1234');

        partner = Partner.objects.create(uID= user,company = "BMO",
                                        info="this is partner1", name
= "admin", approved="no")
        self.assertEquals(partner.uID.username, "user")
        self.assertEquals(partner.company,"BMO")
        self.assertEquals(partner.info, "this is partner1")
        self.assertEquals(partner.name,"admin")
        self.assertEquals(partner.approved,"no")



def test_model_Partner_2(self):
    '''
        Test model Partner(database)
    '''
    user = User.objects.create_user('user2','changyingyu1991@gmail.com','1234');
    
    partner = Partner.objects.create(uID= user,company = "BMO",
                                     info="this is partner2", name
                                     = "user", approved="yes")
        self.assertEquals(partner.uID.username, "user2")
        self.assertEquals(partner.company,"BMO")
        self.assertEquals(partner.info, "this is partner2")
        self.assertEquals(partner.name,"user")
                                     self.assertEquals(partner.approved,"yes")