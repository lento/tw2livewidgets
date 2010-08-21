<div class="${w.widget_class} ${w.css_class % w.data}" title="${w.label % w.data}">
    % for c in w.children:
        ${c.display() | n }
    % endfor
</div>
