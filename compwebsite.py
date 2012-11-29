import cgi
import datetime
import urllib
import webapp2

from google.appengine.ext import db
from google.appengine.api import users

class Person(db.Model):
  """Models an individual Person entry with a first name, last name, email address, and phone number"""
  
  author = db.UserProperty()
  first_name = db.StringProperty()
  last_name = db.StringProperty()
  email = db.EmailProperty()
  phone = db.PhoneNumberProperty()
  room = db.StringProperty()
  date = db.DateTimeProperty(auto_now_add=True)
  
def userbook_key(userbook_name=None):
    return db.Key.from_path('Userbook', userbook_name or 'default_userbook')


class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.out.write('<html><body>')
    userbook_name=self.request.get('userbook_name')
    persons = db.GqlQuery("SELECT * "
                          "FROM Person "
                          "WHERE ANCESTOR IS :1 "
                          "ORDER BY last_name ASC LIMIT 10",
                          userbook_key(userbook_name))

    for person in persons:
      if person.first_name:
        self.response.out.write('<p>%s %s is in the data base. Email: %s. Phone Number: %s. Dorm Room: %s</p>\n' % (person.first_name, person.last_name, person.email, person.phone, person.room))
        self.response.out.write('<p>%s was registered at %s' % (person.first_name, person.date))
     
    if users.get_current_user():
      url = users.create_logout_url(self.request.uri)
      self.response.out.write('<a href="%s">Logout</a>' % url)
    else:
      url = users.create_login_url(self.request.uri)
      self.response.out.write('<a href="%s">Login</a>' % url)
      
    self.response.out.write("""
           <form action="/sign?%s" method="post">
             <p>First Name:</p>
             <div><textarea name="first_name" rows="1" cols="40"></textarea></div>
             <p>Last Name:</p>
             <div><textarea name="last_name" rows="1" cols="40"></textarea></div>
             <p>Phone Number:</p>
             <div><textarea name="phone" rows="1" cols="40"></textarea></div>
             <p>Dorm Address:</p>
             <div><textarea name="room" rows="1" cols="40"></textarea></div>
             <div><input type="submit" value="Register User"></div>
           </form>
           <hr>
           <form><input value="%s" name="userbook_name"></form>
        </body>
    </html>""" % (urllib.urlencode({'userbook_name': userbook_name}),
                          cgi.escape(userbook_name)))
    
class Userbook(webapp2.RequestHandler):
  def post(self):
    userbook_name=self.request.get('userbook_name')  
    person = Person(parent=userbook_key(userbook_name))

    if users.get_current_user():
      person.author = users.get_current_user()
    person.first_name = self.request.get('first_name')
    person.last_name = self.request.get('last_name')
    person.email = person.author.email()
    person.phone = self.request.get('phone')
    person.room = self.request.get('room')
    person.put()
    self.redirect('/?' + urllib.urlencode({'userbook_name': userbook_name}))

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/sign', Userbook)],
                              debug=True)
