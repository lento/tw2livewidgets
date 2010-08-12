<%def name="render_subfields(subfields)">
    % for index, subfield in enumerate(subfields):
        if (${subfield.condition | n}) {
            var subfield_maker_${str(index)} = ${subfield.maker.display() | n};
            field += subfield_maker_${str(index)}(data, "${subfield.id}");
        };
    % endfor
</%def>

