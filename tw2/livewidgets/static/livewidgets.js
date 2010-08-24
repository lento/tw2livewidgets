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
        $(elem).addClass('updated', "slow", function() {
            $(elem).removeClass("updated", "slow", function() {
                if (typeof(callback) != 'undefined')
                    callback();
            });
        });
    }

    lw.activateOverlays = function(elem) {
        $(elem).overlay({
            onBeforeLoad: function(event) { 
                trigger = this.getTrigger();
                target = trigger.attr("href");
                iframe = $("#overlay iframe")[0];
                iframe.src = target
            },
            expose: {
                color: '#333'
            }
        });
    }

    /* Common */
    lw.render_content = function(widget_id, item, extra_data) {
        var layout_maker = lw.widgets[widget_id].layout_maker;
        var data = item;
        $.extend(data, extra_data);
        return layout_maker(data);
    }

    lw.update = function(update_topic, item, show_update, extra_data) {
        $('.update_on_' + update_topic).each(function(i, container) {
            $('.item-' + item.id, $(container)).each(function(i, element) {
                $(element).html(lw.render_content(container.id, item, extra_data));
                if (show_update) {
                    lw.showUpdates(element);
                }
                lw.activateOverlays($(".overlay", element));
            });
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

