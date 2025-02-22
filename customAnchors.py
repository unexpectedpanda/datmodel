# From https://github.com/mh166/mkdocs-custom-anchors/blob/main/customAnchors.py
# Looks for <code> tags with IDs, and adds them to the TOC. This doesn't assign children
# properly and uses CSS to fake the indent, so be careful with heading order.

from mkdocs.structure.toc import AnchorLink
from html import unescape, escape
from html.parser import HTMLParser
import re

class CustomHeadings(HTMLParser):
    _targetTag = 'code'
    _linkDepth = 2
    _linkCounter = 0
    _isHeading = False
    _id = ''
    _content = ''
    targetLink = None

    def handle_starttag(self, tag: str, attrs: list):
        if re.match(r"h[2-6]", tag):
            if 'id' in dict(attrs):
                self._linkCounter += 1
        if self._isHeading or tag != self._targetTag:
            return
        # print(self.get_starttag_text())
        for (attr, val) in attrs:
            if attr == 'id':
                self._linkCounter += 1
                self._isHeading = True
                self._id = val

    def handle_data(self, data: str):
        if not self._isHeading:
            return
        self._content += '<code class="toc-code">' + data + '</code>'

    def handle_endtag(self, tag: str):
        if not self._isHeading or tag != self._targetTag:
            return
        # print('Add link for heading...')
        # print('  > ' + self._content)
        # print(f'  --> targetLink != None: {not self.targetLink is None}')
        if not self.targetLink is None:
            self.targetLink.children.insert(
                self._linkCounter - 1,
                AnchorLink(self._content, self._id, self._linkDepth)
            )
        self._isHeading = False
        self._content = ''


def on_page_content(html, page, **kwargs):
    if page.file.src_uri == 'releases.md':
        print('\n=====< PAGE >=====')
        print('src: ' + page.file.src_uri)
        print('title: ' + page.title)
        print('-----< PAGE.toc >-----')

    for link in page.toc:
        parser = CustomHeadings()
        parser.targetLink = link
        parser.feed(html)

    if page.file.src_uri == 'releases.md':
        dump_links(link)
        print('\n======= // =======\n')


def dump_links(link, depth=0):
    padding = ' ' * 2 * (depth + 1)
    # link.title = escape(unescape(link.title).title())
    print(f'{padding}- [{link.level}] {link.title} => {link.url}')
    if len(link.children) > 0:
        print(f'{padding}  -> {len(link.children)} children')
        for child in link.children:
            dump_links(child, depth+1)