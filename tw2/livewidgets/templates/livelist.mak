<%inherit file="livecontainer.mak"/>
<ul id="${w.compound_id}" class="${w.container_class or ''}">
    % for item in w.children:
        ${item.display() | n}
    % endfor
</ul>
