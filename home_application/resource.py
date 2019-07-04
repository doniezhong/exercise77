# -*- coding: utf-8 -*-
import copy

import xlrd
import xlwt
from django.http import FileResponse


def get_search_dict(query_dict):
    '''
    将reuqest的querydict转化为dict
    '''
    search_dict = query_dict.dict()
    for k, v in search_dict.items():
        if 'time' in k:
            continue

        new_key = "%s__icontains" % k
        search_dict[new_key] = search_dict.pop(k)

    return search_dict


def download_response(file_data, file_name):
    '''
    用于文件下载
    :param file_data:
    :param file_name:
    :return:
    '''
    response = FileResponse(file_data)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="%s"' % file_name
    return response


def read_excel(file_content):
    excel = xlrd.open_workbook(file_contents=file_content)
    sheet = excel.sheets()[0]
    # 获取所有行
    excel_rows = []
    for index in xrange(0, sheet.nrows):
        row = sheet.row_values(index)
        excel_rows.append(row)

    # 获取所有列
    excel_cols = []
    for index in xrange(0, sheet.ncols):
        col = sheet.col_values(index)
        excel_cols.append(col)

    return excel_rows, excel_cols


def write_excel():
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('sheet1')
    for i in xrange(1, 10):
        for j in xrange(1, i + 1):
            sheet.write((i - 1), (j - 1), "%s * %s = %s" % (i, j, i * j))

    book.save('test')


def simple_get_list(query_dict, db_model):
    search_dict = get_search_dict(query_dict)
    model_list = db_model.objects.filter(**search_dict)
    return [m.to_dict() for m in model_list]


class LineChart(object):
    type = 'line'

    def __init__(self, axis, series, title='', sub_title=''):
        self.axis = axis
        self.series = []
        for s in series:
            self.series.append(dict(s, type=self.type))

        self.title = {
            "text": title,
            "sub_text": sub_title
        }

    @property
    def chart_data(self):
        return {
            "title": self.title,
            "xAxis": self.axis,
            "series": self.series,
        }


class BarChart(LineChart):
    type = 'bar'


class HorBarChart(object):
    def __init__(self, axis, series, title='', sub_title=''):
        self.axis = axis
        self.series = []
        for s in series:
            self.series.append(dict(s, type='bar'))

        self.title = {
            "text": title,
            "sub_text": sub_title
        }

    @property
    def chart_data(self):
        return {
            "title": self.title,
            "yAxis": self.axis,
            "series": self.series,
        }


class PieChart(object):
    def __init__(self, series, title='', sub_title=''):
        self.series =series
        self.title = {
            "text": title,
            "sub_text": sub_title
        }

    @property
    def chart_data(self):
        return {
            "title": self.title,
            "series": self.series,
        }


class FunnelChart(PieChart):
    pass


class Chart(object):
    CHARTMAP = {
        'line': LineChart,
        'bar': BarChart,
        'hor_bar': HorBarChart,
        'pie': PieChart,
        'funnel': FunnelChart,
    }

    def __new__(cls, type, *args, **kwargs):
        type_cls = cls.CHARTMAP.get(type)
        return type_cls(*args, **kwargs)


class CCTopoTreeHandle(object):

    @staticmethod
    def get_inst_key(inst):
        try:
            return "%s|%s" % (inst['bk_obj_id'], inst['bk_inst_id'])
        except KeyError:
            return None

    def foreach_topo_tree(self, topo, func=None, topo_link=[]):
        # 从上到下遍历topo树
        if isinstance(topo, dict):
            # 记录层级
            inst_key = self.get_inst_key(topo)
            if not inst_key:
                return None

            c_topo_link = copy.deepcopy(topo_link)
            c_topo_link.append(inst_key)
            # 执行操作
            if func:
                func(topo, c_topo_link)

            child = topo.get('child')
            if child:
                self.foreach_topo_tree(child, func, c_topo_link)

        if isinstance(topo, list):
            for item in topo:
                c_topo_link = copy.deepcopy(topo_link)
                self.foreach_topo_tree(item, func, c_topo_link)
