 <div id="${w.compound_id}" class="${w.container_class} ${w.update_topic and 'update_on_%s' % w.update_topic or ''}">
    ${self.body()}
</div>

<script type="text/javascript">
    $(function() {
        lw.widgets["${w.compound_id}"] = new(Object);
        lw.widgets["${w.compound_id}"].layout_maker = ${w.child.maker() | n};
    });
</script>

