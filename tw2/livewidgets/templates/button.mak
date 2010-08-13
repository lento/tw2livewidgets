<a class="${w.css_class % w.data}" title="${w.label % w.data}"
   href="${w.action % w.data}" rel="#overlay">
    % for c in w.children:
        ${c.display() | n }
    % endfor
</a>
