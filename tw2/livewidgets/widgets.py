import tw2.core as twc


class Livewidgets(twc.Widget):
    template = "genshi:tw.livewidgets.templates.livewidgets"

    # declare static resources here
    # you can remove either or both of these, if not needed
    resources = [
        twc.JSLink(modname=__name__, filename='static/livewidgets.js'),
        twc.CSSLink(modname=__name__, filename='static/livewidgets.css'),
    ]

    @classmethod
    def post_define(cls):
        pass
        # put custom initialisation code here

    def prepare(self):
        super(Livewidgets, self).prepare()
        # put code here to run just before the widget is displayed
