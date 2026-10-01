from anagrams import anagrams


def normalize(groups):
    return sorted(sorted(group) for group in groups)


def test_example():
    result = anagrams(
        ["eat", "tea", "tan", "ate", "nat", "bat"]
    )
    expected = [
        ["bat"],
        ["nat", "tan"],
        ["ate", "eat", "tea"],
    ]
    assert normalize(result) == normalize(expected)


def test_empty_list():
    assert anagrams([]) == []


def test_single_word():
    assert anagrams(["eat"]) == [["eat"]]


def test_empty_strings():
    result = anagrams(["", "", "eat"])
    expected = [["", ""], ["eat"]]
    assert normalize(result) == normalize(expected)


def test_repeated_words():
    result = anagrams(["eat", "eat", "tea"])
    expected = [["eat", "eat", "tea"]]
    assert normalize(result) == normalize(expected)