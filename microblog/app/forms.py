#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 17:20
# @Author  : wangyunchuan
# @File    : forms.py
# @Project : microblog
# @Software: PyCharm

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
