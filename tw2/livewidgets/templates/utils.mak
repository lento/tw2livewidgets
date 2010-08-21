<%def name="render_subfields(subfields)">
    % for index, subfield in enumerate(subfields):
        if (${subfield.update_condition | n}) {
            var subfield_maker_${str(index)} = ${subfield.maker() | n};
            field += subfield_maker_${str(index)}(data);
        };
    % endfor
</%def>

<%def name="render_subitems(subfields)">
    % for index, subfield in enumerate(subfields):
        if (${subfield.update_condition | n}) {
            var subfield_maker_${str(index)} = ${subfield.maker() | n};
            if (typeof(data["${w.key}"])=='object') {
                $.each(data["${w.key}"], function(i, item) {
                    var newdata = data;
                    $.each(item, function(key, value) {newdata['${w.key}_'+key] = value;});
                    field += subfield_maker_${str(index)}(newdata);
                });
            } else {
                field += subfield_maker_${str(index)}(data);
            }
        }
    % endfor
</%def>
