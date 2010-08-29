<div id="${w.compound_id}" class="${w.container_class}
 ${w.update_topic and 'update_on_%s' % w.update_topic or ''}
 ${w.update_filter and 'update_filter_%s' % w.update_filter or ''}">
    ${self.body()}
</div>

<script type="text/javascript">
    $(function() {
        var widget = new(lw.Widget);
        widget.append_selector = "${w.child.append_selector}";
        widget.layout_maker = ${w.child.maker() | n};
        $.extend(widget.callbacks, ${w.callbacks});
        lw.widgets["${w.compound_id}"] = widget
    });
</script>

