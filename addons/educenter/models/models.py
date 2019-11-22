# -*- coding: utf-8 -*-

from odoo import models, fields, api

class courses(models.Model):
    _name = 'educenter.courses'

    course_name = fields.Char()
    language_name = fields.Many2one('educenter.languages')
    price = fields.Integer()
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()

    # @api.depends('value')
    # def _value_pc(self):
    #     self.value2 = float(self.value) / 100
class languages(models.Model):
    _name = 'educenter.languages'

    name = fields.Char()
    teacher = fields.Char()

class group(models.Model):
    _name = 'educenter.group'

    group_name = fields.Char()
    student_Name = fields.Char()
    student_Surname = fields.Char()
    student_Patronic = fields.Char()
    course_name = fields.Char()

class teacher(models.Model):
    _name = 'educenter.teacher'

    teacher_Name = fields.Char()
    teacher_Surname = fields.Char()
    teacher_Patronic = fields.Char()
    language_name = fields.Char()

class schedule(models.Model):
    _name = 'educenter.schedule'

    group_name = fields.Char()
    course_name = fields.Char()
    language_name = fields.Char()
    time_begin = fields.Datetime()
    time_end = fields.Datetime()