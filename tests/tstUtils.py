import itertools as it

from typing import TYPE_CHECKING, Any

import logseq_doctor as ld


if TYPE_CHECKING:
    IntCounter = it.count[int]
else:
    IntCounter = it.count
# https://github.com/python/mypy/issues/5264#issuecomment-399407428


def insert(what: str, into: str, at: int) -> str:
    """
    example:
    >>> insert('ab', '01234', 2)
    '01ab4'
    """
    (l:=list(into))[at:at+len(what)] = what
    return ''.join(l)


def rulerWrap(contents: object, heading: str='', width: int=30) -> str:
    bottomRuler='-'*width
    topRuler=insert(heading+':', bottomRuler, 2)
    contentsStr = contents if isinstance(contents, str) else f'{contents!r}'
    return '\n'.join(['', topRuler, contentsStr, bottomRuler, ''])
    

def debugPrint(in_md     : ld.MD_flat   |None = None,
               exp_md    : ld.MD_outline|None = None,
               actual_md : ld.MD_outline|None = None) -> None:
    docAst_str = ld.md_to_AST(in_md) if in_md else None
    toPrint: list[tuple[Any,str]]
    toPrint = [(in_md     , 'in'      ),
               (exp_md    , 'expected'),
               (actual_md , 'actual'  ),
               (docAst_str, 'docAst'  )]
    for var, name in toPrint:
        if var:
            print(rulerWrap(str(var), name))


def infCounter() -> IntCounter:
    return it.count(0)


