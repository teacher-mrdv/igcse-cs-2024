def is_palindrome(word: str) -> bool:
    reverse: str = ''
    for c in range(len(word)-1, -1, -1):
        reverse = reverse + word[c]
    return word == reverse

print( 'is_palindrome(\'delved\') = ', is_palindrome('delved') )
print( 'is_palindrome(\'sells\') = ', is_palindrome('sells') )
print( 'is_palindrome(\'racecar\') = ', is_palindrome('racecar') )
print( 'is_palindrome(\'abcdcba\') = ', is_palindrome('abcdcba') )
print( 'is_palindrome(\'ada\') = ', is_palindrome('ada') )
print( 'is_palindrome(\'rotor\') = ', is_palindrome('rotor') )
print( 'is_palindrome(\'1234321\') = ', is_palindrome('1234321') )
print( 'is_palindrome(\'98766789\') = ', is_palindrome('98766789') )
