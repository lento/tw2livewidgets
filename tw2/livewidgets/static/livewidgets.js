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

    /* utilities */
    lw.showUpdates = function(elem, callback) {
        $(elem).addClass('updated', 1500, function() {
            $(elem).removeClass("updated", 1500, function() {
                if (typeof(callback) != 'undefined')
                    callback();
            });
        });
    }

    /* Common */
    lw.render_content = function(widget_id, item, extra_data) {
        var layout_maker = lw.widgets[widget_id].layout_maker;
        var data = item;
        $.extend(data, extra_data);
        return layout_maker(data);
    }

    lw.add = function(update_topic, item, show_update, extra_data) {
        $('.update_on_' + update_topic).each(function(i, container) {
            $(lw.widgets[container.id].append_selector, $(container))
                .append(lw.render_content(container.id, item, extra_data));
            if (show_update) {
                lw.showUpdates($('.item-' + item.id, $(container)));
            }
        });
    }

    lw.update = function(update_topic, item, show_update, extra_data) {
        $('.update_on_' + update_topic).each(function(i, container) {
            $('.item-' + item.id, $(container)).each(function(i, element) {
                $(element).replaceWith(lw.render_content(container.id, item, extra_data));
            });
            if (show_update) {
                lw.showUpdates($('.item-' + item.id, $(container)));
            }
        });
    }

    lw.delete = function(update_topic, item, show_update, extra_data) {
        $('.update_on_' + update_topic).each(function(i, container) {
            $('.item-' + item.id, $(container)).each(function(i, element) {
                if (show_update)
                    lw.showUpdates(element, function() {$(element).remove()});
                else
                    $(element).remove();
            });
        });
    }
}

