from knuth_morris_pratt import zalgorithm


class KMP:
    @staticmethod
    def __map_j_to_i(zvalues, spi_primes):
        for j in reversed(range(len(zvalues))):
            i = j + zvalues[j] - 1
            if i > 0:
                spi_primes[i] = zvalues[j]

    @staticmethod
    def __kmp_algorithm(text, pattern, spi_primes):
        occurrences = []
        c = 0
        p = 0
        print('text', len(text))
        print('pattern', len(pattern))
        while c + len(pattern) - p <= len(text):
            while p < len(pattern) and pattern[p] is text[c]:
                p += 1
                c += 1
            # If position p is equal to the lenght of the pattern, then
            # an occurrence of p was found.
            if p is len(pattern):
                occurrences.append(c - len(pattern))
            # Otherwise, if p is 0, then the first character of the pattern
            # was a mismatch with the current position in the text, c. Thus,
            # we increment c by one and continue
            # TODO: Ask about when there is an occurence, so p > 0 but c doesn't increment. It should I think
            elif p is 0:
                c += 1
            p = KMP.__failure(p, spi_primes)
        return occurrences

    @staticmethod
    def find_pattern(text, pattern):
        if len(text) < len(pattern):
            return []
        # Get Z-values of pattern
        zvalues = []
        zalgorithm.ZAlgorithm.getzvalues(pattern, zvalues)
        print('zvalues: ', zvalues)

        # Compute spi prime values of the pattern
        spi_primes = [0] * len(zvalues)
        KMP.__map_j_to_i(zvalues, spi_primes)
        print('spi_primes: ', spi_primes)

        # find pattern
        return KMP.__kmp_algorithm(text, pattern, spi_primes)

    @staticmethod
    def spi_to_spi_prime(spivalues):
        for i, c in list(enumerate(spivalues))[:-1]:
            if spivalues[i + 1] > spivalues[i]:
                spivalues[i] = 0

        return spivalues

    @staticmethod
    def spiprime_to_spi(spiprimevalues):
        for i, c in reversed(list(enumerate(spiprimevalues))[:-1]):
            spiprimevalues[i] = max(spiprimevalues[i + 1] - 1, spiprimevalues[i])

        return spiprimevalues

    @staticmethod
    def __failure(i, spi_primes):
        return spi_primes[i - 1]
