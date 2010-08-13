${self.body()}

<script type="text/javascript">
    $(function() {
        lw.widgets["${w.compound_id}"] = new(Object);
        lw.widgets["${w.compound_id}"].field_makers = [];
        % for index, field in enumerate(w.child.children):
            lw.widgets["${w.compound_id}"].field_makers.push(
                {"css_class": "${field.css_class}",
                 "condition": function(data) {return (${field.condition | n});},
                 "maker": ${field.maker().replace('\n', '') | n},
                });
        % endfor
    });
</script>

