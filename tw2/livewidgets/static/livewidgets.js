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

/* jQuery utils */
$.fn.showUpdates = function(callback) {
    return this.each(function() {
        $(this).addClass('updated', "slow", function() {
            $(this).removeClass("updated", "slow", function() {
                if (typeof(callback) != 'undefined')
                    callback();
            });
        });
    });
}

$.fn.activateOverlays = function() {
    return this.each(function() {
        $(this).overlay({
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
    });
}

/* livewidgets namespace */
if (typeof(lw)=='undefined') {
    lw = new(Object);
    lw.widgets = new(Object);

    /* Common */
    lw.content_maker = function(widget_id, item, extra_data) {
        var field_makers = lw.widgets[widget_id].field_makers;
        var content = "";
        
        if (field_makers != null && typeof(field_makers) != "undefined") {
            $.each(field_makers, function() {
                if (this.condition(item)) {
                    var css_class = this.css_class;
                    var field_maker = this.maker;
                    var data = item;
                    $.extend(data, extra_data);
                    content += field_maker(data);
                }
            });
        };
        return content;
    }
}

