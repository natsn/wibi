#!/usr/bin/env python

"""

    init_pop.py initializes and populates the database with dummy content.

    As of 6/11/15 dummy data includes:

    - 1 Agency
    - 10 Users (all three types)
    - 10 Profiles (in a hiearchy)
    - 1 Curriculum
    - 3 Levels
    - 12 total Pages
    - 20 random Messages between coaches and participants

    Trivia: `def double_link(list)` is a nifty function that applies all the lilnkage
            to an ordered list of Page objects.
"""
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
import django
django.setup()
from django.contrib.auth.models import User
from project.models import *
a = Agency.objects.create(name='ORI')
a.save()
cu = Curriculum.objects.create(title='ePALS1', agency=a)
cu.save()


# Create 10 users
usernames = ['p1','p2','p3','p4','p5','t1','t2','c1','c2','c3']
fullnames = ['Johnetta Herrig','Evette Shehan','Evangeline Bohney','Henry Rajtar','Shanel Kisch','Shaunda Santino','Francene Coxon','Roxy Breach','Ilana Trevis','Kathey Deignan']
emails = ['laparosalpingectomy@susceptible.net','physiatrical@centroacinar.com','bundlerooted@aranga.net','tarmac@autobiographical.co.uk','percentably@plenarium.edu','gripment@gastroesophageal.com','compulsion@unreligion.com','landholdership@syncerebral.org','drizzly@longicone.co.uk','dermatoskeleton@coppice.net']

for n,f,e in zip(usernames,fullnames,emails):
    u = User.objects.create_user(n,e,'123')
    u.first_name = f.split()[0]
    u.last_name = f.split()[1]
    u.save()
    p = Profile.objects.create(user=u,agency=a,higher_up=None,type=n[0].upper())
    p.save()
    cap = CurriculumAndProfile.objects.create(curriculum=cu,profile=p)
    cap.save()

# Establish Hiearchy
def belong_it(username,higher_up_username):
    p = Profile.objects.get(user__username=username)
    p.higher_up = Profile.objects.get(user__username=higher_up_username)
    p.save()

belong_it('p1','c1')
belong_it('p2','c1')
belong_it('p3','c3')
belong_it('p4','c2')
belong_it('p5','c2')
belong_it('c1','t1')
belong_it('c2','t1')
belong_it('c3','t2')

# Make some messages
for text in ['Hi how are you?','Nice seeing you','This is a test message', 'Testing 1,2,3', 'test','test','test','test','test','test','test']:
    p = User.objects.filter(profile__type='P').order_by('?').first().profile
    m1 = Message.objects.create(recipient=p.user, sender=p.higher_up.user, text=text, seen_by_recipient=False)
    m2 = Message.objects.create(recipient=p.higher_up.user, sender=p.user, text=text, seen_by_recipient=False)
    m1.save()
    m2.save()

# Make Level 1...
l1=Level.objects.create(title='Level One', position=1, curriculum=cu)
p1=Page.objects.create(level=l1, title='Page One', markdown='blah blah blah')
p2=Page.objects.create(level=l1, title='Page Two', markdown='blah blah blah')
p3=Page.objects.create(level=l1, title='Page Three', markdown='blah blah blah')

# Make Level 2...
l2=Level.objects.create(title='Level Two', position=2, curriculum=cu)
p4=Page.objects.create(level=l2, title='l2Page One', markdown='blah blah blah')
p5=Page.objects.create(level=l2, title='l2Page Two', markdown='blah blah blah')
p6=Page.objects.create(level=l2, title='l2Page Three', markdown='blah blah blah')
p7=Page.objects.create(level=l2, title='l2Page Four', markdown='blah blah blah')

l3=Level.objects.create(title='Level Three', position=3, curriculum=cu)
p8=Page.objects.create(level=l3, title='l3Page One', markdown='blah blah blah')
p9=Page.objects.create(level=l3, title='l3Page Two', markdown='blah blah blah')
p10=Page.objects.create(level=l3, title='l3Page Three', markdown='blah blah blah')
p11=Page.objects.create(level=l3, title='l3Page Four', markdown='blah blah blah')
p12=Page.objects.create(level=l3, title='l3Page Five', markdown='blah blah blah')


# Link them...
def double_link(list):
    if len(list) >= 2:
        prev = None
        for el in list:
            el.prv = prev
            el.save()
            prev = el
        nexty = None
        for el in reversed(list):
            el.nxt = nexty
            el.save()
            nexty = el

double_link([p1,p2,p3])
double_link([p4,p5,p6,p7])
double_link([p8,p9,p10,p11,p12])

print '\n-----\nUSERS\n-----\n', User.objects.all()
print '\n-------\nCONTENT\n-------\n'
print 'Level 1: ', l1.page_list
print 'Level 2: ', l2.page_list
print 'Level 3: ', l3.page_list
print '\n--------\nMESSAGES\n--------\n', Message.objects.all()

