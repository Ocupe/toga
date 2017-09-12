from rubicon.objc import *
from .base import Widget
from ..libs import *


class TogaWebView(WKWebView):
    @objc_method
    def webView_didFinishNavigation_(self, sender, frame) -> None:
        self.interface._impl.update_dom()
        if self.interface.on_webview_load:
            self.interface.on_webview_load(self.interface)

    @objc_method
    def acceptsFirstResponder(self) -> bool:
        return True

    @objc_method
    def keyDown_(self, event) -> None:
        if self.interface.on_key_down:
            self.interface.on_key_down(event.keyCode, event.modifierFlags)


class WebView(Widget):
    def create(self):
        self.native = TogaWebView.alloc().init()
        self.native.interface = self.interface
        self.native.delegate = self.native
        self.native.navigationDelegate = self.native
        self.native.allowsBackForwardNavigationGestures = True

        # Add the layout constraints
        self.add_constraints()

        self._dom = None

    def update_dom(self):
        # fixme this code produces a race condition due to the fact that the callback is invoked from the
        # obj-c side. If we request the dom imidiatly after the page has loaded,
        # it is possible that self.dom has not been updated yet.
        def callback(result: ObjCInstance) -> None:
            self._dom = str(ObjCInstance(result)).encode('utf-8')

        self.native.evaluateJavaScript_completionHandler_('document.documentElement.outerHTML', callback)

    @property
    def get_dom(self):
        return self._dom

    def set_url(self, value):
        if value:
            self._dom = None
            request = NSURLRequest.requestWithURL_(NSURL.URLWithString_(self.interface.url))
            self.native.loadRequest_(request)

    def set_content(self, root_url, content):
        self.native.loadHTMLString_baseURL_(content, NSURL.URLWithString_(root_url))

    def set_user_agent(self, value):
        if value:
            self.native.customUserAgent = value

    def evaluate(self, javascript):
        return self.native.stringByEvaluatingJavaScriptFromString_(javascript)

