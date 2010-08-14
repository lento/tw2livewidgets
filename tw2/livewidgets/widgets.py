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
def get_data(widget):
    parent = widget.parent
    if parent:
        if isinstance(parent, ItemLayout) and hasattr(parent, 'value'):
            if isinstance(parent.value, dict):
                return parent.value
            else:
                return getattr(parent.value, '__dict__', {})
        else:
            return getattr(parent, 'data', {})
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
    data = twc.Variable('A dictionary used to expand formatting strings in '
        'templates', default = {})

    def prepare(self):
        super(LiveWidget, self).prepare()

        # get the ItemLayout value as a dictionary to use in string formatting
        self.data = get_data(self)

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
    """Base class for compound LiveWidgets

    If the ``key`` of the compound widget corresponds to an element
    in its parent ``data``, the widget will exted ``data`` with the subelements
    prefixing their names with its ``key``
    """
    children = []

    @classmethod
    def post_define(cls):
        # a compound widget must have id=None to propagate the object or
        # dictionary received from its ItemLayout parent as "value" to its
        # children, so if "id" is set we copy it to "key" (if "key" is not
        # already set) and then reset it
        id = getattr(cls, 'id', None)
        cls.key = cls.key or id or ''
        if id:
            cls.id = None

    def prepare(self):
        # extend data with subelements
        self.data = get_data(self)
        newdata = {}
        if self.key in self.data:
            if isinstance(self.data[self.key], dict):
                for k, v in self.data[self.key].iteritems():
                    newdata['%s_%s' % (self.key, k)] = v
            else:
                for k, v in self.data[self.key].__dict__.iteritems():
                    newdata['%s_%s' % (self.key, k)] = v
        self.data.update(newdata)

        # call CompoundWidget.prepare() to prepare children. We do this after
        # extending "data" so children will get the new extended dictionary
        # when calling "get_data()"
        super(LiveCompoundWidget, self).prepare()


class Box(LiveCompoundWidget):
    """A simple container widget

    Box is a compound widget, and can contain other widgets like ``Text``,
    ``Image`` or ``Icon``
    """
    template = 'mako:tw2.livewidgets.templates.box'
    maker_template = 'mako:tw2.livewidgets.templates.box_maker'


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


class Icon(LiveWidget):
    """An icon widget"""
    template = 'mako:tw2.livewidgets.templates.icon'
    maker_template = 'mako:tw2.livewidgets.templates.icon_maker'
    icon_class = twc.Param('The css class identifying this icon', default='')


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

