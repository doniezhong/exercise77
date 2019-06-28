# -*- coding: utf-8 -*-
from django.db import models


class Test(models.Model):

    create_name = models.CharField(max_length=20)
    update_name = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def to_dic(self):
        result_dict = dict([(f.name, getattr(self, f.name)) for f in self._meta.fields if f.name != "name"])
        result_dict["name_dict"] = self.name.to_dic()
        return result_dict