# -*- coding: utf-8 -*-

from edi.search import _
from Products.Five.browser import BrowserView

from zopyx.typesense.api import API

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class CustomSearchView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('custom_search_view.pt')

    def __call__(self):
        import pdb; pdb.set_trace()
        if self.request.method == "POST":
            pass
        else:
            pass

        import pdb; pdb.set_trace()
        # Implement your own actions:
        self.msg = _(u'A small message')
        return self.index()

    def search(self):
        ts_api = API()
        query = self.request.get("search")
        if (query == ""):
            return None
        result = ts_api.search(query)
        hits = result["found"]

