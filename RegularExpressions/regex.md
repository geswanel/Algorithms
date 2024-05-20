# Regex tutorial
- **USE raw strings with patterns so `\\` no needed to escape escape character**
- [tutorial](https://www.w3resource.com/python/python-regular-expression.php#re1)
- [exercises](https://www.w3resource.com/python-exercises/re/)

## RE patterns
- patterns
    - `.` matches any char except newline
    - `^` `$` - matches beginning and end of the string '^A' 'e$'
    - `*` 0 or more times for prev character 'b*' matches 'bbbbb'
    - `+` 1 or more
    - `?` 0 or 1 times
    - `+?` `??` `*?` not making them greedy. f.e. `<.*>` will match all string `<a> b <c>`
        but with `<.*?>` will only match `<a>` from the string
    - `{m}` matches exactly m prev, `{m, n}` maches from m to n characters, `{m, n}?` non greedy
    - `\` escape character or **special sequence**
    - `[]` indicate charset. Special character lose their special meaning inside. `-` used for range. `\w` `\S` - character classes accepted. `^` complementing the set. for `\]` or at beginning
    - `|` or between re
    - `(...)` - start and and of group of re inside => **Content can be retrieved with \num special sequence**
        - `(?...)` - extension to groups
            - `(?aiLmsux)` a(ascii), i(ignore case), L(locale), M(multiline), s(dot matches all), u(unicode), x(verbose)  
            - `(?:...)` non-capturing. Cannot be retrieved or used later
            - `(?ismx-ismx:...)` set or removes flags ismx (lock at ailmsux)
            - `(?P<name>...)` - group can be retrieved by name
                - example `(?P<quote>['"]).*?(?P=quote)` text between quote
                    - references `(?P=quote)` `\1`
                    - **Match object** `m.group("quote") or m.end('quote')`
                    - `re.sub` in a repl argument `\g<quote>, \g<1> \1`
            - `(?P=name)` - backreference to a named group
            - `(?#...)` comment - ignored
            - assertions
                - `(?=...)` - matches if `Isaac (?=Asimov)` matches Isaac only if it followed by Asimov
                - `(?!...)` - matches if ... doesn't match next. Same as top but if it's not followed by asimov
                - `(?<=...)` - look behind `(?<=abc)def` matches `abcdef`. `m.group(0) = abcdef`
                    ```shell
                    >>> m = re.search(r'(?<=-)\w+', 'spam-egg')
                    >>> m.group(0)
                    'egg'
                    ```
                - `(?<!...)` same as top but not behind
                - `(?(id/name)yes-pattern|no-patter)` if group with id/name exist => yes pattern, no otherwise
                    - `(<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$)`
                        - `(<)?` - 0 or 1 of `<` - group 1
                        - `(\w+@\w+(...)+)` `\w = [a-zA-Z0-9_]` => (1 or more \w)@(1 or more \w) (1 or more insdie(...))
                            - `(?:\.\w+)` - `?:` not captured, `\.` - dot symbol (not special). 1 or more characters. f.e. `.com`
                        - `(?(1)>|$)` if \1 captured => `>` else `$` 
        - `\number` - matches the **content** of group `(.+) \1` matches `the the`
    - special sequences
        - `\A` - only at the start
        - `\b` - matches empty string at the beginning or end of a word.
        - `\B` - opposite to `\b`
        - `\d` = `[0-9]`. `\D` = `[^0-9]`
        - `\s` = `[ \t\n\r\f\v]` - space characters. `\S` opposite
        - `\w` = `[a-zA-Z0-9_]`. `\W` opposite
        - `\Z` - matches only at the end of the string
- Nesting groups
## RE functions
- search - search for first location and return Match
- findall - return all matches as a list of strings or tuples
- Match
    - `groups` - return tuple
    - `group() group(num)` - return group(num) content
- compile - compile patter to re object

