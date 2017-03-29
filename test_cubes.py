import cubes


def test_int():
    x3 = cubes.Int(3, (1, 2), "foo")
    assert x3 == 3


def test_int_comparison():
    x1 = cubes.Int(1, (1, 1), "a")
    x2 = cubes.Int(2, (9, 9), "z")
    x3 = cubes.Int(3, (3, 3), "b")
    assert x1 < x2 < x3


def test_int_equality():
    assert cubes.Int(123, None, None) == cubes.Int(123, 67, "foo")


def test_int_large():
    x = cubes.Int(3 ** 237, None, None)
    assert x == 3 ** 237


def test_solutions_2_way_finds_hardy_ramanujan():
    assert 1729 in list(cubes.solutions_2_way(2000))


def test_solutions_2_way_discards_identical():
    assert list(cubes.solutions_2_way(2000)) == [1729]


def test_solutions_2_way_exact_bound():
    assert not list(cubes.solutions_2_way(1729))
    assert list(cubes.solutions_2_way(1730))


# oeis.org The On-Line Encyclopedia of Integer Sequences

ONE_WAY = {2, 9, 16, 28, 35, 54, 65, 72, 91, 126, 128, 133, 152, 189, 217,
           224, 243, 250, 280, 341, 344, 351, 370, 407, 432, 468, 513,
           520, 539, 559, 576, 637, 686, 728, 730, 737, 756, 793, 854,
           855, 945, 1001, 1008, 1024, 1027, 1064, 1072, 1125, 1216,
           1241, 1332, 1339, 1343}

TWO_WAY = {1729, 4104, 13832, 20683, 32832, 39312, 40033, 46683,
           64232, 65728, 110656, 110808, 134379, 149389, 165464,
           171288, 195841, 216027, 216125, 262656, 314496, 320264,
           327763, 373464, 402597, 439101, 443889, 513000, 513856,
           515375, 525824, 558441, 593047, 684019, 704977}

THREE_WAY = {87539319, 119824488, 143604279, 175959000, 327763000,
             700314552, 804360375, 958595904, 1148834232,
             1407672000, 1840667192, 1915865217, 2363561613,
             2622104000, 3080802816, 3235261176, 3499524728,
             3623721192, 3877315533, 4750893000, 5544709352,
             5602516416}

FOUR_WAY = {6963472309248, 12625136269928, 21131226514944,
            26059452841000, 55707778473984, 74213505639000,
            95773976104625, 101001090159424, 159380205560856,
            169049812119552, 174396242861568, 188013752349696}

FIVE_WAY = {48988659276962496, 391909274215699968,
            490593422681271000, 1322693800477987392,
            3135274193725599744, 3924747381450168000,
            6123582409620312000, 6355491080314102272,
            10581550403823899136}

SIX_WAY = {24153319581254312065344}


def test_solutions_at_least_one_way():
    # OEIS includes a^3 + a^3 solutions :(
    # assert cubes.solutions_at_least_n_way(max(ONE_WAY) + 1, 1) == ONE_WAY
    pass


def test_solutions_at_least_two_way():
    assert cubes.solutions_at_least_n_way(max(TWO_WAY) + 1, 2) == TWO_WAY


def test_solutions_at_least_three_way():
    assert cubes.solutions_at_least_n_way(max(THREE_WAY) + 1, 3) == THREE_WAY

def test_solutions_at_least_six_way():
    # way over available RAM
    # assert cubes.solutions_at_least_n_way(max(SIX_WAY) + 1, 6) == SIX_WAY
    pass


def test_resource_usage():
    import resource
    N = 9000000000
    before = resource.getrusage(resource.RUSAGE_SELF)
    list(cubes.solutions_2_way(N))
    after = resource.getrusage(resource.RUSAGE_SELF)
    print("N used", N)
    print("time used", after.ru_utime - before.ru_utime)
    print("memory used", after.ru_maxrss - before.ru_maxrss)
