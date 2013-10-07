import functools
import itertools
import operator

from .recipes import grouper


__all__ = ('chunks',)


def chunks(iterable, size=20):
    """Generator that iterates over an iterable in size chunks

    Example::
        >>> list(chunks('ABCDEFG', size=3))
        [('A', 'B', 'C'), ('D', 'E', 'F'), ('G',)]

        >>> list(chunks('ABCDEFG', size=3))
        [('A', 'B', 'C'), ('D', 'E', 'F'), ('G',)]
    """
    stop = object()
    for chunk in grouper(size, iterable, fillvalue=stop):
        if chunk[-1] is stop:
            is_not_stop = functools.partial(operator.is_not, stop)
            yield tuple(itertools.takewhile(is_not_stop, chunk))
            break

        yield chunk
