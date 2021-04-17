# WikiTextParser
A simple to use WikiText parsing library for MediaWiki.

The purpose is to allow users easily extract and/or manipulate templates, template parameters, parser functions, tables, external links, wikilinks, lists, etc. found in wikitexts.

## Table of Contents

- WikiTextParser
   - Installation
   - Usage
     - Templates
     - WikiLinks
     - Sections
     - Tables
     - Lists
     - Tags
     - Miscellaneous
   - Compared with mwparserfromhell
   - Known issues and limitations
   - Credits

# Installation
- Python 3.5+ is required
- `pip install 'setuptools>=36.2.1'`
- `pip install wikitextparser`

# Usage
```Python
>>> import wikitextparser as wtp
```

WikiTextParser can detect sections, parser functions, templates, wiki links, external links, arguments, tables, wiki lists, and comments in your wikitext. The following sections are a quick overview of some of these functionalities.

You may also want to have a look at the test modules for more examples and probable pitfalls (expected failures).

## Templates
```Python
>>> parsed = wtp.parse("{{text|value1{{text|value2}}}}")
>>> parsed.templates
[Template('{{text|value1{{text|value2}}}}'), Template('{{text|value2}}')]
>>> parsed.templates[0].arguments
[Argument("|value1{{text|value2}}")]
>>> parsed.templates[0].arguments[0].value = 'value3'
>>> print(parsed)
{{text|value3}}
```

The pformat method returns a pretty-print formatted string for templates:
```Python
>>> parsed = wtp.parse('{{t1 |b=b|c=c| d={{t2|e=e|f=f}} }}')
>>> t1, t2 = parsed.templates
>>> print(t2.pformat())
{{t2
    | e = e
    | f = f
}}
>>> print(t1.pformat())
{{t1
    | b = b
    | c = c
    | d = {{t2
        | e = e
        | f = f
    }}
}}
```

`Template.rm_dup_args_safe` and `Template.rm_first_of_dup_args` methods can be used to clean-up [pages using duplicate arguments in template calls](https://en.wikipedia.org/wiki/Category:Pages_using_duplicate_arguments_in_template_calls):

```Python
>>> t = wtp.Template('{{t|a=a|a=b|a=a}}')
>>> t.rm_dup_args_safe()
>>> t
Template('{{t|a=b|a=a}}')
>>> t = wtp.Template('{{t|a=a|a=b|a=a}}')
>>> t.rm_first_of_dup_args()
>>> t
Template('{{t|a=a}}')
```
Template parameters:
```Python
>>> param = wtp.parse('{{{a|b}}}').parameters[0]
>>> param.name
'a'
>>> param.default
'b'
>>> param.default = 'c'
>>> param
Parameter('{{{a|c}}}')
>>> param.append_default('d')
>>> param
Parameter('{{{a|{{{d|c}}}}}}')
```

## WikiLinks
```Python
>>> wl = wtp.parse('... [[title#fragmet|text]] ...').wikilinks[0]
>>> wl.title = 'new_title'
>>> wl.fragment = 'new_fragmet'
>>> wl.text = 'X'
>>> wl
WikiLink('[[new_title#new_fragmet|X]]')
>>> del wl.text
>>> wl
WikiLink('[[new_title#new_fragmet]]')
```

All WikiLink properties support get, set, and delete operations.

## Sections
```Python
>>> parsed = wtp.parse("""
... == h2 ==
... t2
... === h3 ===
... t3
... === h3 ===
... t3
... == h22 ==
... t22
... {{text|value3}}
... [[Z|X]]
... """)
>>> parsed.sections
[Section('\n'),
 Section('== h2 ==\nt2\n=== h3 ===\nt3\n=== h3 ===\nt3\n'),
 Section('=== h3 ===\nt3\n'),
 Section('=== h3 ===\nt3\n'),
 Section('== h22 ==\nt22\n{{text|value3}}\n[[Z|X]]\n')]
>>> parsed.sections[1].title = 'newtitle'
>>> print(parsed)

==newtitle==
t2
=== h3 ===
t3
=== h3 ===
t3
== h22 ==
t22
{{text|value3}}
[[Z|X]]
>>> del parsed.sections[1].title
>>>> print(parsed)

t2
=== h3 ===
t3
=== h3 ===
t3
== h22 ==
t22
{{text|value3}}
[[Z|X]]
```

## Tables
Extracting cell values of a table:

>>> p = wtp.parse("""{|
... |  Orange    ||   Apple   ||   more
... |-
... |   Bread    ||   Pie     ||   more
... |-
... |   Butter   || Ice cream ||  and more
... |}""")
>>> p.tables[0].data()
[['Orange', 'Apple', 'more'],
 ['Bread', 'Pie', 'more'],
 ['Butter', 'Ice cream', 'and more']]
By default, values are arranged according to colspan and rowspan attributes:

>>> t = wtp.Table("""{| class="wikitable sortable"
... |-
... ! a !! b !! c
... |-
... !colspan = "2" | d || e
... |-
... |}""")
>>> t.data()
[['a', 'b', 'c'], ['d', 'd', 'e']]
>>> t.data(span=False)
[['a', 'b', 'c'], ['d', 'e']]
Calling the cells method of a Table returns table cells as Cell objects. Cell objects provide methods for getting or setting each cell's attributes or values individually:

>>> cell = t.cells(row=1, column=1)
>>> cell.attrs
{'colspan': '2'}
>>> cell.set('colspan', '3')
>>> print(t)
{| class="wikitable sortable"
|-
! a !! b !! c
|-
!colspan = "3" | d || e
|-
|}
HTML attributes of Table, Cell, and Tag objects are accessible via get_attr, set_attr, has_attr, and del_attr methods.

Lists
The get_lists method provides access to lists within the wikitext.

>>> parsed = wtp.parse(
...     'text\n'
...     '* list item a\n'
...     '* list item b\n'
...     '** sub-list of b\n'
...     '* list item c\n'
...     '** sub-list of b\n'
...     'text'
... )
>>> wikilist = parsed.get_lists()[0]
>>> wikilist.items
[' list item a', ' list item b', ' list item c']
The sublists method can be used to get all sub-lists of the current list or just sub-lists of specific items:

>>> wikilist.sublists()
[WikiList('** sub-list of b\n'), WikiList('** sub-list of b\n')]
>>> wikilist.sublists(1)[0].items
[' sub-list of b']
It also has an optional pattern argument that works similar to lists, except that the current list pattern will be automatically added to it as a prefix:

>>> wikilist = wtp.WikiList('#a\n#b\n##ba\n#*bb\n#:bc\n#c', '\#')
>>> wikilist.sublists()
[WikiList('##ba\n'), WikiList('#*bb\n'), WikiList('#:bc\n')]
>>> wikilist.sublists(pattern='\*')
[WikiList('#*bb\n')]
Convert one type of list to another using the convert method. Specifying the starting pattern of the desired lists can facilitate finding them and improves the performance:

>>> wl = wtp.WikiList(
...     ':*A1\n:*#B1\n:*#B2\n:*:continuing A1\n:*A2',
...     pattern=':\*'
... )
>>> print(wl)
:*A1
:*#B1
:*#B2
:*:continuing A1
:*A2
>>> wl.convert('#')
>>> print(wl)
#A1
##B1
##B2
#:continuing A1
#A2
Tags
Accessing HTML tags:

>>> p = wtp.parse('text<ref name="c">citation</ref>\n<references/>')
>>> ref, references = p.get_tags()
>>> ref.name = 'X'
>>> ref
Tag('<X name="c">citation</X>')
>>> references
Tag('<references/>')
WikiTextParser is able to handle common usages of HTML and extension tags. However it is not a fully-fledged HTML parser and may fail on edge cases or malformed HTML input. Please open an issue on github if you encounter bugs.

Miscellaneous
parent and ancestors methods can be used to access a node's parent or ancestors respectively:

>>> template_d = parse("{{a|{{b|{{c|{{d}}}}}}}}").templates[3]
>>> template_d.ancestors()
[Template('{{c|{{d}}}}'),
 Template('{{b|{{c|{{d}}}}}}'),
 Template('{{a|{{b|{{c|{{d}}}}}}}}')]
>>> template_d.parent()
Template('{{c|{{d}}}}')
>>> _.parent()
Template('{{b|{{c|{{d}}}}}}')
>>> _.parent()
Template('{{a|{{b|{{c|{{d}}}}}}}}')
>>> _.parent()  # Returns None
Use the optional type_ argument if looking for ancestors of a specific type:

>>> parsed = parse('{{a|{{#if:{{b{{c<!---->}}}}}}}}')
>>> comment = parsed.comments[0]
>>> comment.ancestors(type_='ParserFunction')
[ParserFunction('{{#if:{{b{{c<!---->}}}}}}')]
To delete/remove any object from its parents use del object[:] or del object.string.

The remove_markup function or plain_text method can be used to remove wiki markup:

>>> from wikitextparser import remove_markup, parse
>>> s = "'''a'''<!--comment--> [[b|c]] [[d]]"
>>> remove_markup(s)
'a c d'
>>> parse(s).plain_text()
'a c d'
Compared with mwparserfromhell
mwparserfromhell is a mature and widely used library with nearly the same purposes as wikitextparser. The main reason leading me to create wikitextparser was that mwparserfromhell could not parse wikitext in certain situations that I needed it for. See mwparserfromhell's issues 40, 42, 88, and other related issues. In many of those situation wikitextparser may be able to give you more acceptable results.

Also note that wikitextparser is still using 0.x.y version meaning that the API is not stable and may change in the future versions.

The tokenizer in mwparserfromhell is written in C. Tokenization in wikitextparser is mostly done using the regex library which is also in C. I have not rigorously compared the two libraries in terms of performance, i.e. execution time and memory usage. In my limited experience, wikitextparser has a decent performance in realistic cases and should be able to compete and may even have little performance benefits in some situations.

If you have had a chance to compare these libraries in terms of performance or capabilities please share your experience by opening an issue on github.

Some of the unique features of wikitextparser are: Providing access to individual cells of each table, pretty-printing templates, a WikiList class with rudimentary methods to work with lists, and a few other functions.

Known issues and limitations
The contents of templates/parameters are not known to offline parsers. For example an offline parser cannot know if the markup [[{{z|a}}]] should be treated as wikilink or not, it depends on the inner-workings of the {{z}} template. In these situations wikitextparser tries to use a best guess. [[{{z|a}}]] is treated as a wikilink (why else would anyone call a template inside wikilink markup, and even if it is not a wikilink, usually no harm is done).
Localized namespace names are unknown, so for example [[File:...]] links are treated as normal wikilinks. mwparserfromhell has similar issue, see #87 and #136. As a workaround, Pywikibot can be used for determining the namespace.
Linktrails are language dependant and are not supported. Also not supported by mwparserfromhell. However given the trail pattern and knowing that wikilink.span[1] is the ending position of a wikilink, it is possible to compute a WikiLink's linktrail.
Templates adjacent to external links are never considered part of the link. In reality, this depends on the contents of the template. Example: parse('http://example.com{{dead link}}').external_links[0].url == 'http://example.com'
List of valid extension tags depends on the extensions intalled on the wiki. The tags method currently only supports the ones on English Wikipedia. A configuration option might be added in the future to address this issue.
wikitextparser currently does not provide an ast.walk-like method yielding all descendant nodes.
Parser functions and magic words are not evaluated.