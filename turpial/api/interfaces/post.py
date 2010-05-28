# -*- coding: utf-8 -*-

"""Módulo genérico para manejar los post de microblogging en Turpial"""
#
# Author: Wil Alvarez (aka Satanas)
# May 20, 2010

class Status:
    def __init__(self):
        self.id = None
        self.text = None
        self.username = None
        self.avatar = None
        self.source = None
        self.timestamp = None
        self.in_reply_to_id = None
        self.in_reply_to_user = None
        self.is_favorite = False
        self.retweeted_by = None
        self.datetime = None

class Response:
    def __init__(self, items=[], type='status', errmsg=''):
        self.items = items
        self.type = type #status/profile/rate/error/mixed
        self.errmsg = errmsg
        
class Profile:
    def __init__(self):
        self.id = None
        self.fullname = None
        self.username = None
        self.avatar = None
        self.location = None
        self.url = None
        self.bio = None
        self.following = None
        self.followers_count = None
        self.friends_count = None
        self.password = None
        self.profile_link_color = None
        
class RateLimit:
    def __init__(self):
        self.hourly_limit = None
        self.remaining_hits = None
        self.reset_time = None
        self.reset_time_in_seconds = None
