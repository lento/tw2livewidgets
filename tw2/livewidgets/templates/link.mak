<div class="${w.css_class % w.data}" title="${w.label % w.data}">
<a href="${w.dest % w.data}">
    % for c in w.children:
        ${c.display() | n }
    % endfor
</a>
</div>
