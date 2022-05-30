# Automata for EBNF

## Syntax

File should consist of lines of comments or rules.

Rule line has the following format:
`<non-terminal name> : <expression>`

Where:
* `<non-terminal name>` - is a capital letter
* `<expression>` - is regex expression, with following operators supported:
  * `<...> +` - one or more repetitions
  * `<...> *` - zero or more repetitions
  * `<...> ?` - zero or one repetition
  * `<...> | <...>` - alternative
  * `(<expression>)` - expression in parenthesis

Spaces in the syntax are ignored.

Comment line starts with `//`:
```
// Comment string
```

## Example of file format

```
S : AB? | (AB)*
A : abc
B : cba+
```

## Visualization of the syntax:

![](./scheme/scheme.png)
