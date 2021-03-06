#!/usr/bin/env python
# Copyright (c) 2012, Fog Creek Software, Inc.
# Copyright (c) 2016-2018, Red Hat, Inc.
#   License: 2-clause BSD; see LICENSE.txt for details
import json
import requests


class Tokens(object):
    __module__ = 'trollo'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def get(self, token, fields=None):
        resp = requests.get("https://trello.com/1/tokens/%s" % (token), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_field(self, field, token):
        resp = requests.get("https://trello.com/1/tokens/%s/%s" % (token, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_member(self, token, fields=None):
        resp = requests.get("https://trello.com/1/tokens/%s/member" % (token), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_member_field(self, field, token):
        resp = requests.get("https://trello.com/1/tokens/%s/member/%s" % (token, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)
