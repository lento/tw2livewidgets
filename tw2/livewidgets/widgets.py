# -*- coding: utf-8 -*-
#
# This file is part of tw2.livewidgets.
#
# tw2.livewidgets is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# tw2.livewidgets is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with tw2.livewidgets.  If not, see <http://www.gnu.org/licenses/>.
#
# Original Copyright (c) 2010, Lorenzo Pierfederici <lpierfederici@gmail.com>
# Contributor(s): 
#
"""A collection of ToscaWidget2 that can update in realtime"""

import tw2.core as twc


# Containers
class LiveContainer(twc.RepeatingWidget):
    """Base class for LiveWdigets containers"""
    child = twc.Required
    children = twc.Required

    resources = [
        twc.JSLink(modname=__name__, filename='static/livewidgets.js'),
        twc.JSLink(modname=__name__, filename='static/jquery.js'),
    ]


class ItemLayout(twc.CompoundWidget):
    """Base class for LiveWidget layouts"""
    children = twc.Required

    def prepare(self):
        super(ItemLayout, self).prepare()
        
        # set item_id
        self.item_id = '%s-%s' % (self.parent.compound_id,
                                                getattr(self.value, 'id', ''))


class ListItemLayout(ItemLayout):
    """A compund widget that wraps its children in a <li> element"""
    template = 'mako:tw2.livewidgets.templates.list_item_layout'


class UnorderedList(LiveContainer):
    """A repeating widget that render its values as an <ul> element"""
    template = 'mako:tw2.livewidgets.templates.list_unordered'
    child = ListItemLayout


# Widgets
class FieldMaker(twc.Widget):
    """Default field maker for LiveWidget objects"""
    template = 'mako:tw2.livewidgets.templates.default_maker'


class LiveWidget(twc.CompoundWidget):
    """Base class for LiveWidgets"""
    maker = twc.Variable(default=FieldMaker())
    maker_template = twc.Param('A mako template rendering a javascript function'
        ' with prototype: function(data, id){} that returns the HTML for this '
        'field', default='mako:tw2.livewidgets.templates.default_maker')
    label = twc.Param('Tooltip text', default='')
    condition = twc.Param('Javascript condition', default='true')
    css_class = twc.Param('CSS class', default='')


    @classmethod
    def post_define(cls):
        # set the field maker template and link it to its parent widget
        cls.maker.template = cls.maker_template
        cls.maker.parent = cls

    def prepare(self):
        super(LiveWidget, self).prepare()
        
        # get the parent's value as a dictionary to use in string formatting
        if hasattr(self.parent, 'value'):
            self.data = getattr(self.parent.value, '__dict__', {})
        else:
            self.data = {}


class Text(LiveWidget):
    """A simple text widget"""
    template = 'mako:tw2.livewidgets.templates.text'
    text = twc.Param('A formatting string the will be expanded with the '
        'widget parent\'s value attributes, ``None`` defaults to the widget\'s '
        'value', default=None)
    maker_template = 'mako:tw2.livewidgets.templates.text_maker'
    children = []

    def prepare(self):
        super(Text, self).prepare()
        
        # use widget value if "text" was not given
        self.text = self.text or self.value or ''


# DEBUG stuff
class Dummy(object):
    def __init__(self, **kw):
        for k, v in kw.iteritems():
            setattr(self, k, v)

