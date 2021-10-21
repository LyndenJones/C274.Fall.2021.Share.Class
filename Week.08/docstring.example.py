# https://pandas.pydata.org/docs/development/contributing_docstring.html

# https://github.com/pandas-dev/pandas/blob/master/pandas/core/arrays/boolean.py

def add(num1, num2):
    """
    Add up two integer numbers.

    This function simply wraps the ``+`` operator, and does not
    do anything interesting, except for illustrating what
    the docstring of a very simple function looks like.

    Parameters
    ----------
    num1 : int
        First number to add.
    num2 : int
        Second number to add.

    Returns
    -------
    int
        The sum of ``num1`` and ``num2``.

    See Also
    --------
    subtract : Subtract one integer from another.

    Examples
    --------
    >>> add(2, 2)
    4
    >>> add(25, 0)
    25
    >>> add(10, -10)
    0
    """
    return num1 + num2

# Paul Lu
def example():
    """
    Prose summary.

    Parameters
    ----------
    param1 : type
        Prose
    param2 : type
        Prose

    Returns
    -------
    type
        Prose

    See Also
    --------
    Prose

    Examples
    --------
    doctest
    """

class C274:
    """
    Prose summary.

    Attributes
    ----------

    Methods
    -------

    See Also
    --------
    Prose

    Examples
    --------
    doctest
    """

    def my_method():
        """
        Prose summary.

        Parameters
        ----------
        param1 : type
            Prose
        param2 : type
            Prose

        Returns
        -------
        type
            Prose

        See Also
        --------
        Prose

        Examples
        --------
        doctest
        """

