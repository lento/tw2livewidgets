/* This file is part of tw2.livewidgets.
 *
 * tw2.livewidgets is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * tw2.livewidgets is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with tw2.livewidgets.  If not, see <http://www.gnu.org/licenses/>.
 * 
 * Original Copyright (c) 2010, Lorenzo Pierfederici <lpierfederici@gmail.com>
 * Contributor(s): 
 */

/* livewidgets namespace */
if (typeof(lw)=='undefined') {
    lw = new(Object);
    lw.widgets = new(Object);
    lw.ANISPEED = 1250;

    /* Common */
    lw.render_content = function(widget_id, data) {
        var layout_maker = lw.widgets[widget_id].layout_maker;
        return layout_maker(data);
    }

    lw.added = function(container, data, show_updates) {
        $(lw.widgets[container.id].append_selector, $(container)).each(function(i, parent) {
            var new_element = $(lw.render_content(container.id, data));
            new_element.addClass('updated').appendTo($(parent))
                .fadeIn(lw.ANISPEED, function() {
                    new_element.removeClass('updated', lw.ANISPEED);
                });
        });
    }

    lw.updated = function(container, data, show_updates) {
        $('.item-' + data.id, $(container)).each(function(i, element) {
            $(element).replaceWith(lw.render_content(container.id, data));
            if (show_updates) {
                $('.item-' + data.id, $(container)).addClass('updated', lw.ANISPEED, function() {
                    $('.item-' + data.id, $(container)).removeClass('updated', lw.ANISPEED);
                });
            }
        });
    }

    lw.deleted = function(container, data, show_updates) {
        $('.item-' + data.id, $(container)).each(function(i, element) {
            if (show_updates) {
                $(element).addClass('updated', lw.ANISPEED, function() {
                    $('.item-' + data.id, $(container)).fadeOut(lw.ANISPEED, function() {
                        $(element).remove();
                    });
                });
            }
        });
    }

    /* lwWidget prototype */
    lw.Widget = function() {
        this.layout_maker = function() {};
        this.append_selector = '';
        this.callbacks = {
            'added': lw.added,
            'updated': lw.updated,
            'deleted': lw.deleted,
        }
    }

    /* API */
    lw.update = function(topic, type, item, show_updates, extra_data, filter) {
        filter = (typeof(filter)!='undefined' && filter) ? '.update_filter_' + filter : '';
        $('.update_on_' + topic + filter).each(function(i, container) {
            var data = item;
            $.extend(data, extra_data);
            if (type in lw.widgets[container.id].callbacks) {
                lw.widgets[container.id].callbacks[type](container, data, show_updates);
            }
        });
    }
}

