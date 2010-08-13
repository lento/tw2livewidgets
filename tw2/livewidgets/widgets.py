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

# utils
def get_item_dict(widget):
    parent = widget.parent
    if parent:
        if isinstance(parent, ItemLayout) and hasattr(parent, 'value'):
            if isinstance(parent.value, dict):
                return parent.value
            else:
                return getattr(parent.value, '__dict__', {})
        else:
            return get_item_dict(parent)
    else:
        return {}


# Widgets
class LiveWidget(twc.Widget):
    """Base class for LiveWidgets"""
    maker_template = twc.Param('A mako template rendering a javascript function'
        ' with prototype: ``function(data){}`` that returns the HTML for this '
        'field', default='mako:tw2.livewidgets.templates.default_maker')
    label = twc.Param('Tooltip text', default='')
    condition = twc.Param('Javascript condition', default='true')
    css_class = twc.Param('CSS class', default='')

    def prepare(self):
        super(LiveWidget, self).prepare()

        # get the ItemLayout value as a dictionary to use in string formatting
        self.data = get_item_dict(self)

    @twc.util.class_or_instance
    def maker(self, cls, displays_on=None, **kw):
        """Render a javascript function with prototype: ``function(data) {}``
        that returns the HTML for this field
        """
        if not self:
            return cls.req(**kw).maker(displays_on)
        else:
            if not self.parent:
                self.prepare()
            mw = twc.core.request_local().get('middleware')
            if displays_on is None:
                if self.parent is None:
                    displays_on = mw and mw.config.default_engine or 'string'
                else:
                    displays_on = twc.template.get_engine_name(
                                                    self.parent.template, mw)
            v = {'w':self}
            if mw and mw.config.params_as_vars:
                for p in self._params:
                    if hasattr(self, p):
                        v[p] = getattr(self, p)
            eng = mw and mw.engines or twc.template.global_engines
            return eng.render(self.maker_template, displays_on, v)


class LiveCompoundWidget(LiveWidget, twc.CompoundWidget):
    """Base class for compound LiveWidgets"""
    children = []

    @classmethod
    def post_define(cls):
        # a compound widget must have id=None to propagate the object or
        # dictionary received from its ItemLayout parent as "value" to its
        # children
        cls.id = None


class Text(LiveWidget):
    """A simple text widget"""
    template = 'mako:tw2.livewidgets.templates.text'
    maker_template = 'mako:tw2.livewidgets.templates.text_maker'
    text = twc.Param('A formatting string the will be expanded with the '
        'widget\'s ItemLayout value as a dictionary, ``None`` defaults to the '
        'widget\'s value', default=None)

    def prepare(self):
        super(Text, self).prepare()

        # use widget value if "text" was not given
        self.text = self.text or self.value or ''


class Link(LiveCompoundWidget):
    """A link widget

    Link is a compound widget, and can contain other widgets like ``Text``,
    ``Image`` or ``Icon``
    """
    template = 'mako:tw2.livewidgets.templates.link'
    maker_template = 'mako:tw2.livewidgets.templates.link_maker'
    dest = twc.Param('A formatting string the will be expanded with the '
        'widget\'s ItemLayout value as a dictionary and used as "href" '
        'attribute', default='')


class Image(LiveWidget):
    """An image widget"""
    template = 'mako:tw2.livewidgets.templates.image'
    maker_template = 'mako:tw2.livewidgets.templates.image_maker'
    src = twc.Param('A formatting string the will be expanded with the '
        'widget\'s ItemLayout value as a dictionary, ``None`` defaults to the '
        'widget\'s value', default=None)

    def prepare(self):
        super(Image, self).prepare()

        # use widget value if "src" was not given
        self.src = self.src or self.value or ''


class Button(LiveCompoundWidget):
    """An overlay button widget

    Button is a compound widget, and can contain other widgets like ``Text``,
    ``Image`` or ``Icon``
    """
    template = 'mako:tw2.livewidgets.templates.button'
    maker_template = 'mako:tw2.livewidgets.templates.button_maker'
    action = twc.Param('A formatting string the will be expanded with the '
        'widget\'s ItemLayout value as a dictionary and used as "href" '
        'attribute', default='')


# Layouts
class ItemLayout(twc.CompoundWidget):
    """Base class for LiveWidget layouts"""

    def prepare(self):
        super(ItemLayout, self).prepare()

        # set item_id
        self.item_id = '%s-%s' % (getattr(self.parent, 'compound_id', None),
                                                getattr(self.value, 'id', None))


class ListItemLayout(ItemLayout):
    """A compound widget that wraps its children in a <li> element"""
    template = 'mako:tw2.livewidgets.templates.list_item_layout'


# Containers
class LiveContainer(twc.RepeatingWidget):
    """Base class for LiveWdigets containers"""

    resources = [
        twc.JSLink(modname=__name__, filename='static/livewidgets.js'),
        twc.JSLink(modname=__name__, filename='static/jquery.js'),
    ]


class List(LiveContainer):
    """A repeating widget that render its values as an <ul> element"""
    template = 'mako:tw2.livewidgets.templates.list'
    child = ListItemLayout


# DEBUG stuff
class Dummy(object):
    def __init__(self, **kw):
        for k, v in kw.iteritems():
            setattr(self, k, v)

