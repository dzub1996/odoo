# -*- coding: utf-8 -*-

from odoo import models, fields, api

class courses(models.Model):
    _name = 'educenter.courses'

    name = fields.Char(string='Название курса')
    language_name = fields.Many2one('educenter.languages', string='Название языка')
    level_name = fields.Many2one('educenter.levels',string='Уровень обучения')
    price = fields.Integer(string='Цена')
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()

    # @api.depends('value')
    # def _value_pc(self):
    #     self.value2 = float(self.value) / 100
class languages(models.Model):
    _name = 'educenter.languages'

    name = fields.Char(string='Название языка')

    teacher = fields.Many2one('educenter.teacher',string='Преподаватель')

class group(models.Model):
    _name = 'educenter.group'

    name = fields.Char(string='Название группы')
    student_Name = fields.Char(string='Имя')
    student_Surname = fields.Char(string='Фамилия')
    student_Patronic = fields.Char(string='Отчество')
    course_name = fields.Many2one('educenter.courses',string='Название курса')

class teacher(models.Model):
    _name = 'educenter.teacher'

    teacher_name = fields.Char(string='Имя')
    surname = fields.Char(string='Фамилия')
    patronic = fields.Char(string='Отчество')
    # language_name = fields.Char(string='Название языка')
    name = fields.Text(compute="_get_fio", store=False)

    @api.depends('surname')
    def _get_fio(self):
        for rec in self:
            # rec.name = str('{0} {1} {2}'.format(rec.surname, rec.person_name, rec.patronim)
            # string=" "
            rec.name = str((rec.surname or '')+" "+(rec.teacher_name or '')+" "+(rec.patronic or ''))

class schedule(models.Model):
    _name = 'educenter.schedule'

    group_name = fields.Many2one('educenter.group',string='Название группы')
    course_name = fields.Many2one('educenter.courses',string='Название курса')
    language_name = fields.Many2one('educenter.languages',string='Название языка')
    time_begin = fields.Datetime(string='Время начала занятия')
    time_end = fields.Datetime(string='Время окончания занятия')

class levels(models.Model):
    _name = 'educenter.levels'

    name = fields.Char(string='Уровень обучения')