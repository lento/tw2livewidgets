<%inherit file="livecontainer.mak"/>
<ul>
    % for item in w.children:
        ${item.display() | n}
    % endfor
</ul>
