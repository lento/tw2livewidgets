<%def name="render_subfields(subfields)">
    % for index, subfield in enumerate(subfields):
        if (${subfield.condition | n}) {
            var subfield_maker_${str(index)} = ${subfield.maker() | n};
            field += subfield_maker_${str(index)}(data);
        };
    % endfor
</%def>

