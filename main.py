#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import cgi
import datetime
import math
import os
import pytz
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from pytz.gae import pytz
from datetime import datetime, timedelta
from pytz import timezone

eastern = pytz.timezone('US/Eastern')

from google.appengine.dist import use_library
use_library('django', '1.2')

from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import util


from comp import reqs
class Advertising:
    # required ad sales
    TRADE_NUM = 0
    TRADE_AMT = 300.0
    
    SOLICITED_NUM = 3
    SOLICITED_AMT = 500.0
    
    UNSOLICITED_NUM = 3
    UNSOLICITED_AMT = 0.0
    
    # enumerated ad types
    TRADE = 2
    SOLICITED = 1
    UNSOLICITED = 0

class Comp:
    # weeks in the comp
    WEEKS = 12
    
    # passwords
    CPW = "newb"
    EPW = "rogerlee"
    APW = "rawfulkapter"
    RPW = "kjz1369cc"
    
    """
    DO NOT CHANGE ANYTHING BELOW
    """
    # user status
    COMPER = 0
    EDITOR = 1
    ADMIN = 2
    
    # event status
    VERIFIED = 1
    NEW = 0
    DENIED = -1
    
    # misc. constants
    YEAR = ['Freshman', 'Sophomore', 'Junior', 'Senior']

class Ad(db.Model):
    user = db.UserProperty()
    company = db.StringProperty()
    description = db.StringProperty()
    amount = db.FloatProperty()
    adtype = db.IntegerProperty()
    date = db.DateTimeProperty(auto_now=True)

class AdTotal(db.Model):
    user = db.UserProperty()
    unsolicited_number = db.IntegerProperty(default=0)
    unsolicited_amount = db.FloatProperty(default=0.0)
    solicited_number = db.IntegerProperty(default=0)
    solicited_amount = db.FloatProperty(default=0.0)
    trade_number = db.IntegerProperty(default=0)
    trade_amount = db.FloatProperty(default=0.0)

class Week(db.Model):
    user = db.UserProperty()
    week = db.IntegerProperty()
    date = db.StringListProperty()
    stime = db.StringListProperty()
    etime = db.StringListProperty()
    extra = db.FloatProperty()
    hours = db.FloatProperty()

class UserInfo(db.Model):
    user = db.UserProperty()
    name = db.StringProperty()
    email = db.EmailProperty()
    phone = db.PhoneNumberProperty()
    year = db.IntegerProperty()
    house = db.StringProperty()
    comper = db.IntegerProperty(default=0)
    active = db.BooleanProperty(default=True)
    verify = db.BooleanProperty(default=False)
    initials = db.StringProperty()

class Event(db.Model):
    user = db.UserProperty()
    index = db.IntegerProperty()
    boardtype = db.IntegerProperty()
    eventtype = db.IntegerProperty()
    status = db.IntegerProperty()
    submit_date = db.DateTimeProperty(auto_now_add=True)
    verify_date = db.DateTimeProperty()
    verify_name = db.StringProperty()
    verify_user = db.UserProperty()
    verify_init = db.StringProperty()
    notes = db.StringProperty()

class Main(webapp.RequestHandler):
    def get(self):
        # prompt for login if not logged in
        user = users.get_current_user()
        if not user:
            self.redirect(users.create_login_url(self.request.uri))
        else:
            # retrieve user info and redirect to user info page if info does not exist
            info = db.GqlQuery("SELECT * FROM UserInfo WHERE user = :1", user).get()
            if not info:
                self.redirect('/info')
            else:
                args = {'nav': getHTML(info.comper),
                        'name': info.name}
                self.response.out.write(template.render('main.html', args))

class Compers(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if not user:
            self.redirect(users.create_login_url(self.request.uri))
        else:
            info = db.GqlQuery("SELECT * FROM UserInfo WHERE user = :1", user).get()
            if not info:
                self.redirect('/info')
            else:
                active = []
                banned = []
                all_users = db.GqlQuery("SELECT * FROM UserInfo WHERE comper = :1 ORDER BY name ASC", 0)
                for user in all_users:
                    data = {'info': user,
                            'year': Comp.YEAR[user.year - 1]}
                    if user.active:
                        active.append(data)
                    else:
                        banned.append(data)
                
                args = {'nav': getHTML(info.comper),
                        'active': active,
                        'banned': banned}
                self.response.out.write(template.render('compers.html', args))

class Events(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if not user:
            self.redirect(users.create_login_url(self.request.uri))
        else:
            info = db.GqlQuery("SELECT * FROM UserInfo WHERE user = :1", user).get()
            if not info:
                self.redirect('/info')
            else:
                marks = [0, 0, 0, 0, 0]
                sheet = [[],[],[],[],[]]
                for req in reqs:
                    dt = dict(desc=req, objs=[], num=0)
                    sheet[req['board']].append(dt)
                    marks[req['board']] += 1
                
                events = db.GqlQuery("SELECT * FROM Event WHERE user = :1 ORDER BY submit_date ASC", user)
                for event in events:
                    if event.submit_date:
                        event.submit_date = event.submit_date.replace(tzinfo=pytz.utc).astimezone(eastern)
                    if event.verify_date:
                        event.verify_date = event.verify_date.replace(tzinfo=pytz.utc).astimezone(eastern)                   
                    
                    i = 0

                    while marks[i] <= event.index:
                        event.index -= marks[i]
                        i += 1
                    
                    dt = sheet[event.boardtype]
                    dt[event.index]['objs'].append(event)
                    
                for xgroup in sheet:
                    for yevent in xgroup:
                        for x in yevent['objs']:
                            if x.status == 1:
                                yevent['num'] += 1
                
                args = {'ads': sheet[0],
                        'cm': sheet[1],
                        'cp': sheet[2],
                        'ops': sheet[3],
                        'gen': sheet[4],
                        
                        'nav': getHTML(info.comper),
                        'reqs': reqs,
                        'sheet': sheet}
                self.response.out.write(template.render('reqs.html', args))

class AddEvent(webapp.RequestHandler):
    def post(self):
        user = users.get_current_user()
        if not user:
            self.redirect(users.create_login_url(self.request.uri))
        else:
            event_type = self.request.get('event_key')
            
            index = 0
            
            i = 0
            for req in reqs:
                if req['name'] == event_type:
                    index = i
                i += 1

            event_info = reqs[index]
            
            new_event = Event(user = user,
                              index = index,
                              boardtype = event_info['board'],
                              eventtype = event_info['event'],
                              status = Comp.NEW,
                              )
            
            new_event.put()
            self.redirect('/reqs')

class DelEvent(webapp.RequestHandler):
    def post(self):
        user = users.get_current_user()
        if not user:
            self.redirect(users.create_login_url(self.request.uri))
        else:
            event_key = self.request.get('del_key')
            event = db.get(event_key)
            event.delete()
            self.redirect('/reqs')

class EventDump(webapp.RequestHandler):
    def get(self):
        length = len(reqs)
        for i in range(length):
            req = reqs[i]
            out = '#%02d' % i
            out += ' ' + req['name']
            self.response.out.write(out)
            self.response.out.write("<br>")
            out = 'Quantity: %d' % req['quantity']
            out += ' Board: %d' % req['board'] + ' Type: %d' % req['event']
            self.response.out.write(out)
            self.response.out.write('<br>')

""" Advertisements """
class Ads(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if not user:
            self.redirect(users.create_login_url(self.request.uri))
        
        info = db.GqlQuery("SELECT * FROM UserInfo WHERE user = :1", user).get()
        if not info:
            self.redirect('/info')
        else:
            ads = db.GqlQuery("SELECT * FROM Ad WHERE user = :1 ORDER BY date ASC", user)
            
            solicited = [];
            unsolicited = [];
            trade = [];
            
            for ad in ads:
                if ad.adtype == Advertising.SOLICITED:
                    solicited.append(ad)
                elif ad.adtype == Advertising.UNSOLICITED:
                    unsolicited.append(ad)
                elif ad.adtype == Advertising.TRADE:
                    trade.append(ad)
                    
            adtotal = db.GqlQuery("SELECT * FROM AdTotal WHERE user = :1", user).get()
            if not adtotal:
                adtotal = AdTotal(user = user)
                adtotal.put()
                
            diff = {'u_num': max(0, Advertising.UNSOLICITED_NUM - adtotal.unsolicited_number),
                    'u_amt': max(0, Advertising.UNSOLICITED_AMT - adtotal.unsolicited_amount),
                    's_num': max(0, Advertising.SOLICITED_NUM - adtotal.solicited_number),
                    's_amt': max(0, Advertising.SOLICITED_AMT - adtotal.solicited_amount),
                    't_num': max(0, Advertising.TRADE_NUM - adtotal.trade_number),
                    't_amt': max(0, Advertising.TRADE_AMT - adtotal.trade_amount)
                    }
                    
            args = {'nav': getHTML(info.comper),
                    'solicited': solicited,
                    'unsolicited': unsolicited,
                    'trade': trade,
                    'adtotal': adtotal,
                    'diff': diff
                    }
            
            self.response.out.write(template.render('ads.html', args))

class AddAd(webapp.RequestHandler):
    def post(self):
        user = users.get_current_user()
        if not user:
            self.redirect(users.create_login_url(self.request.uri))

        # retrieve ad details
        company = cgi.escape(self.request.get('Field102'))
        description = cgi.escape(self.request.get('Field104'))
        adtype = int(cgi.escape(self.request.get('adtype')))

        # calculate amount of ad, return if failure
        amount_d = 0.0
        amount_c = 0.0
        try:
            amount_d = float(cgi.escape(self.request.get('Field105')))
            amount_c = float(cgi.escape(self.request.get('Field105-1')))
        except ValueError:
            self.redirect('/ads')
        amount = amount_d + 0.01 * amount_c
        
        # create and insert new ad into database if valid
        if amount > 0.0:
            new_ad = Ad(user=user,
                        company=company,
                        description=description,
                        amount=amount,
                        adtype=adtype
                        )
            new_ad.put()
            
            # calculate total number and value of ads
            ads = db.GqlQuery("SELECT * FROM Ad WHERE user = :1", user)
            u_num = 0;
            u_amt = 0.0;
            s_num = 0;
            s_amt = 0.0;
            t_num = 0;
            t_amt = 0.0;
            for ad in ads:
                if ad.adtype == Advertising.SOLICITED:
                    s_num += 1
                    s_amt += ad.amount
                elif ad.adtype == Advertising.UNSOLICITED:
                    u_num += 1
                    u_amt += ad.amount
                elif ad.adtype == Advertising.TRADE:
                    t_num += 1
                    t_amt += ad.amount
            
            # update adtotal in db
            adtotal = db.GqlQuery("SELECT * FROM AdTotal WHERE user = :1", user).get()
            if not adtotal:
                adtotal = AdTotal(user = user)
            adtotal.unsolicited_number = u_num
            adtotal.unsolicited_amount = u_amt
            adtotal.solicited_number = s_num
            adtotal.solicited_amount = s_amt
            adtotal.trade_number = t_num
            adtotal.trade_amount = t_amt
            adtotal.put()
            
        self.redirect('/ads')

class DelAd(webapp.RequestHandler):
    def post(self):
        user = users.get_current_user()
        if not user:
            self.redirect(users.create_login_url(self.request.uri))
        
        ad_key = self.request.get('del_key')
        
        try:
            ad = db.get(ad_key)
            ad.delete()
            
            # calculate total number and value of ads
            ads = db.GqlQuery("SELECT * FROM Ad WHERE user = :1", user)
            u_num = 0;
            u_amt = 0.0;
            s_num = 0;
            s_amt = 0.0;
            t_num = 0;
            t_amt = 0.0;
            for ad in ads:
                if ad.adtype == Advertising.SOLICITED:
                    s_num += 1
                    s_amt += ad.amount
                elif ad.adtype == Advertising.UNSOLICITED:
                    u_num += 1
                    u_amt += ad.amount
                elif ad.adtype == Advertising.TRADE:
                    t_num += 1
                    t_amt += ad.amount
            
            # update adtotal in db
            adtotal = db.GqlQuery("SELECT * FROM AdTotal WHERE user = :1", user).get()
            if not adtotal:
                adtotal = AdTotal(user = user)
            adtotal.unsolicited_number = u_num
            adtotal.unsolicited_amount = u_amt
            adtotal.solicited_number = s_num
            adtotal.solicited_amount = s_amt
            adtotal.trade_number = t_num
            adtotal.trade_amount = t_amt
            adtotal.put()
        except:
            self.redirect('/ads')

        self.redirect('/ads')

""" Time Sheets """
class Hours(webapp.RequestHandler):
    def get(self):
        # get current user, send to login page if not logged in
        user = users.get_current_user()
        if not user:
            self.redirect(users.create_login_url(self.request.uri))
        else:
            info = db.GqlQuery("SELECT * FROM UserInfo WHERE user = :1", user).get()
            if not info:
                self.redirect('/info')
            else:
                week_data = []
                week_info = []
                week_keys = []
                
                weeks = db.GqlQuery("SELECT * FROM Week WHERE user = :1 ORDER BY week ASC", user)
                if not weeks.get():
                    # create weeks if not present
                    for i in range(1, Comp.WEEKS + 1):
                        week = Week(user=user,
                                    week=i,
                                    date=["","","","",""],
                                    stime=["","","","",""],
                                    etime=["","","","",""],
                                    extra=0.0,
                                    hours=0.0
                                    )
                        week.put()
                    # retrieve the new weeks
                    weeks = db.GqlQuery("SELECT * FROM Week WHERE user = :1 ORDER BY week ASC", user)
                
                total = 0.0
                for week in weeks:            
                    hour_info = []
                    for i in range(5):
                        hour_info.append({'date': week.date[i],
                                          'stime': week.stime[i],
                                          'etime': week.etime[i]}
                                         )
                    
                    temp = {'obj': week,
                            'inf': hour_info}
                        
                    week_data.append(temp)
                    week_info.append(hour_info)
                    week_keys.append(week.key())
                    total += week.hours
                
                args = {'nav': getHTML(info.comper),
                        'week_data': week_data,
                        'week_info': week_info,
                        'week_keys': week_keys,
                        'total_hours': total}
        
                self.response.out.write(template.render('hours.html', args))        

class ClearHours(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if not user:
            self.redirect(users.create_login_url(self.request.uri))
        
        weeks = db.GqlQuery("SELECT * FROM Week WHERE user = :1", user)
        if weeks.get():
            for week in weeks:
                week.delete()

class AddHours(webapp.RequestHandler):
    def post(self):
        user = users.get_current_user()
        if not user:
            self.redirect(users.create_login_url(self.request.uri))
        
        week_key = self.request.get('week_key')
        day = int(self.request.get('day'))
        
        try:
            h_date = datetime.date(int(self.request.get('Field5')),
                                 int(self.request.get('Field5-1')),
                                 int(self.request.get('Field5-2')))
            
            s_time_str = (cgi.escape(self.request.get('Field6')) + ":" +
                          cgi.escape(self.request.get('Field6-1')) + ":" +
                          cgi.escape(self.request.get('Field6-2')) + " " +
                          cgi.escape(self.request.get('Field6-3')))
            s_time = datetime.datetime.strptime(s_time_str, "%I:%M:%S %p")
    
            e_time_str = (cgi.escape(self.request.get('Field7')) + ":" +
                          cgi.escape(self.request.get('Field7-1')) + ":" +
                          cgi.escape(self.request.get('Field7-2')) + " " +
                          cgi.escape(self.request.get('Field7-3')))
            e_time = datetime.datetime.strptime(e_time_str, "%I:%M:%S %p")
    
            week = db.get(week_key)
            week.date[day] = h_date.strftime("%a, %b %d %Y")
            week.stime[day] = s_time.strftime("%I:%M %p")
            week.etime[day] = e_time.strftime("%I:%M %p")
            
            # recalculate total hours in the week
            total = 0.0
            for i in range(5):
                if week.stime[i] != "" and week.etime[i] != "":
                    stime = datetime.datetime.strptime(week.stime[i], "%I:%M %p")
                    etime = datetime.datetime.strptime(week.etime[i], "%I:%M %p")
                    dtime = etime - stime
                    hours = math.fabs(dtime.seconds) / 3600
                    total += hours
            week.hours = round(total + week.extra, 2)
            
            week.put()
        except ValueError:
            print "Error: You failed to input a valid date or time."
        except:
            print "Error: Unknown"
        
        self.redirect('/hours')

class DelHours(webapp.RequestHandler):
    def post(self):
        user = users.get_current_user()
        if not user:
            self.redirect(users.create_login_url(self.request.uri))
        
        week_key = self.request.get('week_key')
        day = int(self.request.get('day'))
        
        week = db.get(week_key)
        
        if week.date[day] != "":
            week.date[day] = ""
            week.stime[day] = ""
            week.etime[day] = ""
            
            # recalculate total hours in the week
            total = 0.0
            for i in range(5):
                if week.stime[i] != "" and week.etime[i] != "":
                    stime = datetime.datetime.strptime(week.stime[i], "%I:%M %p")
                    etime = datetime.datetime.strptime(week.etime[i], "%I:%M %p")
                    dtime = etime - stime
                    hours = math.fabs(dtime.seconds) / 3600
                    total += hours
            week.hours = total + week.extra
    
            week.put()
        
        self.redirect('/hours')

""" User Information"""
class Info(webapp.RequestHandler):
    def get(self):
        # get current user, send to login page if not logged in
        user = users.get_current_user()
        if not user:
            self.redirect(users.create_login_url(self.request.uri))
        
        # retrieve user info from datastore
        info = db.GqlQuery("SELECT * FROM UserInfo WHERE user = :1", user).get()
        
        if info:
            # info already exists, print existing info on page
            phone = str(info.phone)
            phone_split = phone.split('-')
            phone0 = phone_split[0]
            phone1 = phone_split[1]
            phone2 = phone_split[2]
            
            year = ['Freshman', 'Sophomore', 'Junior', 'Senior'][info.year - 1] 
            comper = 'Comper' if info.comper == Comp.COMPER else 'Editor'
            
            args = {'nav': getHTML(info.comper),
                    'name': info.name,
                    'email': info.email,
                    'phone': phone,
                    'phone0': phone0,
                    'phone1': phone1,
                    'phone2': phone2,
                    'year': year,
                    'house': info.house,
                    'comper': comper
                    }
        else:
            args = {'nav': getHTML(Comp.COMPER)}
        
        self.response.out.write(template.render('info.html', args))

    def post(self):
        user = users.get_current_user()
        info = db.GqlQuery("SELECT * FROM UserInfo WHERE user = :1", user).get()
        
        name = cgi.escape(self.request.get('name'))
        email = db.Email(self.request.get('email'))
        phone = db.PhoneNumber(self.request.get('phone-0') + '-' +
                               self.request.get('phone-1') + '-' +
                               self.request.get('phone-2'))
        year = int(self.request.get('year'))
        house = cgi.escape(self.request.get('house'))
            
        if not info:
            info = UserInfo(user = user,
                            name = name,
                            email = email,
                            phone = phone,
                            year = year,
                            house = house,
                            comper = 0
                            )
            info.put()
        else:
            info.name = name
            info.email = email
            info.phone = phone
            info.year = year
            info.house = house
            
            info.put()
        
        self.redirect('/')

""" Admin """
class RequestAdmin(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if not user:
            self.redirect(users.create_login_url(self.request.uri))
        else:
            info = db.GqlQuery("SELECT * FROM UserInfo WHERE user = :1", user).get()
            if not info:
                self.redirect('/info')
            else:
                initials = info.initials
                status = info.comper
                
                sstr = "Comper"
                if status == 1:
                    sstr = "Editor"
                if status == 2:
                    sstr = "Admin"
                
                args = {'initials': initials,
                        'status': sstr,
                        'nav': getHTML(info.comper)}
                self.response.out.write(template.render('request.html', args))
    def post(self):
        user = users.get_current_user()
        info = db.GqlQuery("SELECT * FROM UserInfo WHERE user = :1", user).get()
        
        initials = cgi.escape(self.request.get('initials'))
        epw = cgi.escape(self.request.get('pw0'))
        apw = cgi.escape(self.request.get('pw1'))
        
        status = info.comper
        if epw == Comp.CPW:
            status = 0
        if epw == Comp.EPW:
            status = 1
        if apw == Comp.APW:
            status = 2
        
        info.initials = initials
        info.comper = status
        
        info.put()
        
        self.redirect('/request-admin')

class EventFeed(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if not user:
            self.redirect(users.create_login_url(self.request.uri))
        else:
            info = db.GqlQuery("SELECT * FROM UserInfo WHERE user = :1", user).get()
            if not info:
                self.redirect('/info')
            else:
                if info.comper == Comp.COMPER:
                    self.redirect('/')
                else:
                    events_list = db.GqlQuery("SELECT * FROM Event WHERE status = :1 ORDER BY submit_date ASC", Comp.NEW)
                    events = []
                    for event in events_list:
                        
                        if event.submit_date:
                            event.submit_date = event.submit_date.replace(tzinfo=pytz.utc).astimezone(eastern)
                        if event.verify_date:
                            event.verify_date = event.verify_date.replace(tzinfo=pytz.utc).astimezone(eastern)
                        
                        person = db.GqlQuery("SELECT * FROM UserInfo WHERE user = :1", event.user).get()
                        if person.active:
                            events.append(dict(obj=event, username=person.name, type=reqs[event.index]['name']))
                    
                    args = {'events': events,
                            'nav': getHTML(info.comper)}
                    self.response.out.write(template.render('approve.html', args))

    def post(self):
        user = users.get_current_user()
        if not user:
            self.redirect(users.create_login_url(self.request.uri))
        else:
            info = db.GqlQuery("SELECT * FROM UserInfo WHERE user = :1", user).get()
            if not info:
                self.redirect('/info')
            else:
                if info.comper == Comp.COMPER:
                    self.redirect('/')
                else:
                    keys = self.request.get_all('event_key')
                    submit = self.request.get('submit')
                    
                    action = 0
                    if submit == "Approve":
                        action = 1
                    if submit == "Deny":
                        action = -1
                        event.notes = self.request.get("notes")
                    
                    for key in keys:
                        event = db.get(key)
                        event.status = action
                        
                        if action == 1:
                            event.verify_user = user
                            event.verify_init = info.initials
                            event.verify_date = datetime.utcnow()
                            event.notes = self.request.get("notes")
                            
                        
                        event.put()
                    self.redirect('/approve')

class UserAccess(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if not user:
            self.redirect(users.create_login_url(self.request.uri))
        else:
            info = db.GqlQuery("SELECT * FROM UserInfo WHERE user = :1", user).get()
            if not info:
                self.redirect('/info')
            else:
                if info.comper == Comp.COMPER:
                    self.redirect('/')
                else:
                    compers = db.GqlQuery("SELECT * FROM UserInfo WHERE comper = :1 ORDER BY name ASC", Comp.COMPER)
                    args = {'compers': compers,
                            'nav': getHTML(info.comper)}
                    self.response.out.write(template.render('admin-user-access.html', args))
    def post(self):
        user = users.get_current_user()
        if not user:
            self.redirect(users.create_login_url(self.request.uri))
        else:
            info = db.GqlQuery("SELECT * FROM UserInfo WHERE user = :1", user).get()
            if not info:
                self.redirect('/info')
            else:
                if info.comper == Comp.COMPER:
                    self.redirect('/')
                if info.comper != Comp.ADMIN:
                    self.redirect('/user-access')
                else:
                    pw = self.request.get('pw')
                    if pw != Comp.APW:
                        self.redirect('user-access')
                    else:
                        keys = self.request.get_all('comper_key')
                        submit = self.request.get('submit')
                        
                        if submit == "Drop":
                            for key in keys:
                                comper = db.get(key)
                                comper.active = False
                                comper.put()
                        elif submit == "Recover":
                            for key in keys:
                                comper = db.get(key)
                                comper.active = True
                                comper.put()
                        self.redirect('/user-access')





""" View """

class ViewReqs(webapp.RequestHandler):
    def get(self):
        # get current user, send to login page if not logged in
        user = users.get_current_user()
        if not user:
            self.redirect(users.create_login_url(self.request.uri))
        else:
            info = db.GqlQuery("SELECT * FROM UserInfo WHERE user = :1", user).get()
            if not info:
                self.redirect('/info')
            else:
                if info.comper == Comp.COMPER:
                    self.redirect('/')
                else:
                    key = self.request.get('key')
                    comperinfo = db.get(key)
                    comper = comperinfo.user
                    
                    marks = [0, 0, 0, 0, 0]
                    sheet = [[],[],[],[],[]]
                    for req in reqs:
                        dt = dict(desc=req, objs=[], num=0)
                        sheet[req['board']].append(dt)
                        marks[req['board']] += 1
                    
                    events = db.GqlQuery("SELECT * FROM Event WHERE user = :1 ORDER BY submit_date ASC", comper)
                    for event in events:
                        if event.submit_date:
                            event.submit_date = event.submit_date.replace(tzinfo=pytz.utc).astimezone(eastern)
                        if event.verify_date:
                            event.verify_date = event.verify_date.replace(tzinfo=pytz.utc).astimezone(eastern)                   
                        
                        i = 0
    
                        while marks[i] <= event.index:
                            event.index -= marks[i]
                            i += 1
                        
                        dt = sheet[event.boardtype]
                        dt[event.index]['objs'].append(event)
                        
                    for xgroup in sheet:
                        for yevent in xgroup:
                            for x in yevent['objs']:
                                if x.status == 1:
                                    yevent['num'] += 1
                    
                    args = {'ads': sheet[0],
                            'cm': sheet[1],
                            'cp': sheet[2],
                            'ops': sheet[3],
                            'gen': sheet[4],
                            
                            'nav': getHTML(info.comper),
                            'comper': comperinfo,
                            'reqs': reqs,
                            'sheet': sheet}
                    self.response.out.write(template.render('view-reqs.html', args))                    

class ViewAds(webapp.RequestHandler):
    def get(self):
        # get current user, send to login page if not logged in
        user = users.get_current_user()
        if not user:
            self.redirect(users.create_login_url(self.request.uri))
        else:
            info = db.GqlQuery("SELECT * FROM UserInfo WHERE user = :1", user).get()
            if not info:
                self.redirect('/info')
            else:
                if info.comper == Comp.COMPER:
                    self.redirect('/')
                else:
                    key = self.request.get('key')
                    comperinfo = db.get(key)
                    comper = comperinfo.user
                    
                    ads = db.GqlQuery("SELECT * FROM Ad WHERE user = :1 ORDER BY date ASC", comper)
            
                    solicited = [];
                    unsolicited = [];
                    trade = [];
                    
                    for ad in ads:
                        if ad.adtype == Advertising.SOLICITED:
                            solicited.append(ad)
                        elif ad.adtype == Advertising.UNSOLICITED:
                            unsolicited.append(ad)
                        elif ad.adtype == Advertising.TRADE:
                            trade.append(ad)
                            
                    adtotal = db.GqlQuery("SELECT * FROM AdTotal WHERE user = :1", comper).get()
                    if not adtotal:
                        self.redirect('/user-access')
                    else:
                        diff = {'u_num': max(0, Advertising.UNSOLICITED_NUM - adtotal.unsolicited_number),
                                'u_amt': max(0, Advertising.UNSOLICITED_AMT - adtotal.unsolicited_amount),
                                's_num': max(0, Advertising.SOLICITED_NUM - adtotal.solicited_number),
                                's_amt': max(0, Advertising.SOLICITED_AMT - adtotal.solicited_amount),
                                't_num': max(0, Advertising.TRADE_NUM - adtotal.trade_number),
                                't_amt': max(0, Advertising.TRADE_AMT - adtotal.trade_amount)
                                }
                                
                        args = {'nav': getHTML(info.comper),
                                'comper': comperinfo,
                                'solicited': solicited,
                                'unsolicited': unsolicited,
                                'trade': trade,
                                'adtotal': adtotal,
                                'diff': diff
                                }
                        
                        self.response.out.write(template.render('view-ads.html', args))

class ViewHours(webapp.RequestHandler):
    def get(self):
        # get current user, send to login page if not logged in
        user = users.get_current_user()
        if not user:
            self.redirect(users.create_login_url(self.request.uri))
        else:
            info = db.GqlQuery("SELECT * FROM UserInfo WHERE user = :1", user).get()
            if not info:
                self.redirect('/info')
            else:
                if info.comper == Comp.COMPER:
                    self.redirect('/')
                else:
                    key = self.request.get('key')
                    comperinfo = db.get(key)
                    comper = comperinfo.user
                    
                    week_data = []
                    week_info = []
                    week_keys = []
                    
                    weeks = db.GqlQuery("SELECT * FROM Week WHERE user = :1 ORDER BY week ASC", comper)
                    if not weeks.get():
                        self.redirect('/user-access')
                    else:
                        total = 0.0
                        for week in weeks:            
                            hour_info = []
                            for i in range(5):
                                hour_info.append({'date': week.date[i],
                                                  'stime': week.stime[i],
                                                  'etime': week.etime[i]}
                                                 )
            
                            temp = {'obj': week,
                                    'inf': hour_info}
                                
                            week_data.append(temp)
                            week_info.append(hour_info)
                            week_keys.append(week.key())
                            total += week.hours
                        
                        args = {'nav': getHTML(info.comper),
                                'comper': comperinfo,
                                'week_data': week_data,
                                'week_info': week_info,
                                'week_keys': week_keys,
                                'total_hours': total}
                
                        self.response.out.write(template.render('view-hours.html', args))

                    
""" Other """
class Logout(webapp.RequestHandler):
    def get(self):
        self.redirect(users.create_logout_url('/'))

"""
class GraphTemp(webapp.RequestHandler):
    def get(self):
        values = {'nav': getHTML(info.comper)}
        self.response.out.write(template.render('graphs.html', values))
"""

def main():
    application = webapp.WSGIApplication([('/', Main),
                                          ('/logout', Logout),
                                          ('/info', Info),
                                          ('/compers', Compers),
                                          
                                          ('/reqs', Events),
                                          ('/add-event', AddEvent),
                                          ('/del-event', DelEvent),
                                          
                                          ('/hours', Hours),
                                          ('/addhours', AddHours),
                                          ('/delhours', DelHours),
                                          
                                          ('/ads', Ads),
                                          ('/addad', AddAd),
                                          ('/delad', DelAd),
                                          
                                          ('/request-admin', RequestAdmin),
                                          ('/approve', EventFeed),
                                          ('/user-access', UserAccess),
                                          
                                          ('/view-hours', ViewHours),
                                          ('/view-ads', ViewAds),
                                          ('/view-reqs', ViewReqs),
                                          
                                          #('/dump-reqs', EventDump),
                                          #('/graphs', GraphTemp)
                                          ],
                                         debug=True)
    util.run_wsgi_app(application)

def getHTML(access):
    if access == Comp.COMPER:
        return header + comper + footer
    elif access == Comp.EDITOR:
        return header + editor + footer
    elif access == Comp.ADMIN:
        return header + comper + editor + footer
    return header + footer

# navigation bar html constant
header = """<div id="navigation">        
                <header id="header-nav" class="info">
                    <h2 class="notranslate">Crimson Comp</h2>
                    <div>
                        &nbsp;
                    </div>
                    <div>
                        General Information:&nbsp;
                        <a href="/">Main</a>
                        &nbsp;|&nbsp;
                        <a href="/compers">Compers</a>
                    </div>"""

comper = """    <div>
                     Compers:&nbsp;
                     <a href="/hours">Time Sheet</a>
                     &nbsp;|&nbsp;
                     <a href="/ads">Advertisements</a>
                     &nbsp;|&nbsp;
                     <a href="/reqs">Requirements</a>
                 </div>"""

editor = """     <div>
                     Editors:&nbsp;
                     <a href="/approve">Event Feed</a>
                     &nbsp;|&nbsp;
                     <a href="/user-access">User Access</a>
                 </div>"""

footer = """     <div>
                     &nbsp;
                 </div>
                 <div>
                     <a href="/info">Personal Info</a>
                     &nbsp;|&nbsp;
                     <a href="/request-admin">Request Access</a>
                     &nbsp;|&nbsp;
                     <a href="/logout">Logout</a>
                 </div>
             </header>
         </div>"""

if __name__ == '__main__':
    main()
