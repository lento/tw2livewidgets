<%inherit file="item_layout_maker.mak"/>
    $.each(field_makers, function() {
        if (this.condition(data)) {
            var css_class = this.css_class;
            var field_maker = this.maker;
            content += '<td>' + field_maker(data) + '</td>';
        }
    });
