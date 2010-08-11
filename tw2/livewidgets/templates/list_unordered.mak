<%inherit file="livecontainer.mak"/>
<ul id="${w.compound_id}">
    % for item in w.children:
        ${item.display() | n}
    % endfor
</ul>
