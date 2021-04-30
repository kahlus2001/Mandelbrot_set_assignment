def mandel_seq(x: float, y: float, n: int = 100) -> Sequence[Point]:
    """Return the mandel sequence for the input point (x, y), using n as upper bound.

    Assumptions:

    * start the sequence at (u_0, v_0) = (0, 0)
    * The coordinate (x, y) will have mandel number n,
      when the sequence starts diverging at (u_n,  v_n)

    :param x: x-coordinate of the point for which the sequence is computed
    :param y: y-coordinate of the point for which the sequence is computed
    :param n: upper bound to detect divergence
    :return: the mandel sequence for the point (x, y)

    :examples:

    >>> mandel_seq(1, 0)
    [(0.0, 0.0), (1.0, 0.0), (2.0, 0.0), (5.0, 0.0)]
    >>> mandel_seq(1, -1)
    [(0.0, 0.0), (1.0, -1.0), (1.0, -3.0)]
    >>> mandel_seq(0, 0, n = 1)
    [(0.0, 0.0), (0.0, 0.0)]
    """
    # TODO Exercise c
    u, v = 0, 0
    m = 1
    values = [(u, v)]
    while m <= n:
        u, v = x + u**2 - v**2, y + 2*u*v
        values.append((u, v))
        if (u**2 + v**2) > 4:
            break
        m+=1
    return values

print(mandel_seq(1, 0))