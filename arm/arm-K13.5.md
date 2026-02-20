## K13.5 Statements and control structures

This section describes the statements and program structures available in the pseudocode:

- Statements and Indentation.
- Function and procedure calls.
- Conditional control structures.
- Loop control structures.
- Special statements.
- Comments.

## K13.5.1 Statements and Indentation

Asimple statement is either an assignment, a function call, or a procedure call. Each statement must be terminated with a semicolon.

Indentation normally indicates the structure in compound statements. The statements contained in structures such as if . . . then . . . else . . . or procedure and function definitions are indented more deeply than the statement structure itself. The end of a compound statement structure and their end is indicated by returning to the original indentation level or less.

Indentation is normally done by four spaces for each level. Standard indentation uses four spaces for each level of indent.

## K13.5.2 Function and procedure calls

This section describes how functions and procedures are defined and called in the pseudocode.

## K13.5.2.1 Procedure and function definitions

Aprocedure definition has the form:

```
<procedure name>(<argument <statement 1>; <statement 2>; ... <statement n>;
```

```
prototypes>)
```

where &lt;argument prototypes&gt; consists of zero or more argument definitions, separated by commas. Each argument definition consists of a type name followed by the name of the argument.

## Note

This first definition line is not terminated by a semicolon. This distinguishes it from a procedure call.

Afunction definition is similar, but also declares the return type of the function:

```
<return type> <function name>(<argument <statement 1>; <statement 2>; ... <statement n>;
```

## Note

A function or procedure name can include a ' . '. This is a convention used for functions that have similar but different behaviors in AArch32 and AArch64 states.

Array-like functions are similar, but are written with square brackets and have two forms. These two forms exist because reading from and writing to an array element require different functions. They are frequently used in memory operations. An array-like function definition with a return type is equivalent to reading from an array. For example:

```
<return type> <function name>[<argument prototypes>] <statement 1>; <statement 2>; ... <statement n>;
```

Its related function definition with no return type is equivalent to writing to an array. For example:

```
<function name>[<argument prototypes>] = <value prototype> <statement 1>; <statement 2>; ... <statement n>;
```

The value prototype determines what data type can be written to the array. The two related functions must share the same name, but the value prototype and return type can be different.

## K13.5.2.2 Procedure calls

Aprocedure call has the form:

```
<procedure_name>(<arguments>);
```

## K13.5.2.3 Return statements

Aprocedure return has the form:

return;

## Afunction return has the form:

```
return <expression>;
```

where &lt;expression&gt; is of the type declared in the function prototype line.

```
prototypes>)
```

## K13.5.3 Conditional control structures

This section describes how conditional control structures are used in the pseudocode.

```
K13.5.3.1 if . . . then . . . else . . .
```

In addition to being a ternary operator, a multi-line if . . . then . . . else . . . structure can act as a control structure and has the form:

```
if <boolean_expression> then <statement 1>; <statement 2>; ... <statement n>; elsif <boolean_expression> then <statement a>; <statement b>; ... <statement z>; else <statement A>; <statement B>; ... <statement Z>;
```

The block of lines consisting of elsif and its indented statements is optional, and multiple elsif blocks can be used.

The block of lines consisting of else and its indented statements is optional.

Abbreviated one-line forms can be used when the then part, and in the else part if it is present, contain only simple statements such as:

```
if <boolean_expression> then <statement 1>; if <boolean_expression> then <statement 1>; else <statement A>; if <boolean_expression> then <statement 1>; <statement 2>; else <statement A>;
```

Note

In these forms, &lt;statement 1&gt; , &lt;statement 2&gt; , and &lt;statement A&gt; must be terminated by semicolons. This, and the fact that the else part is optional, distinguish its use as a control structure from its use as a ternary operator.

## K13.5.3.2 case . . . of . . .

A case . . . of . . . structure has the form:

```
case <expression> of when <literal values1> <statement 1>; <statement 2>; ... <statement n>; when <literal values2> <statement 1>; <statement 2>; ... <statement n>; ... more "when" groups if required ... otherwise <statement A>; <statement B>; ... <statement Z>;
```

In this structure, &lt;literal values1&gt; and &lt;literal values2&gt; consist of literal values of the same type as &lt;expression&gt; , separated by commas. There can be additional when groups in the structure. Abbreviated one line forms of when and otherwise parts can be used when they contain only simple statements.

If &lt;expression&gt; has a bitstring type, the literal values can also include bitstring literals containing 'x' bits, known as bitmasks. For details, see Equality and non-equality.

## K13.5.4 Loop control structures

This section describes the three loop control structures used in the pseudocode.

## K13.5.4.1 repeat . . . until . . .

```
A repeat . . . until . . . structure has the form: repeat <statement 1>; <statement 2>; ... <statement n>; until <boolean_expression>;
```

It executes the statement block at least once, and the loop repeats until &lt;boolean expression&gt; evaluates to TRUE . Variables explicitly declared inside the loop body have scope local to that loop and might not be accessed outside the loop body.

## K13.5.4.2 while . . . do

```
A while . . . do structure has the form: while <boolean_expression> do <statement 1>; <statement 2>; ... <statement n>;
```

It begins executing the statement block only if the Boolean expression is true. The loop then runs until the expression is false.

## K13.5.4.3 for . . .

## A for . . . structure has the form:

```
for <assignable_expression> = <integer_expr1> to <integer_expr2> <statement 1>; <statement 2>; ... <statement n>;
```

The &lt;assignable\_expression&gt; is initialized to &lt;integer\_expr1&gt; and compared to &lt;integer\_expr2&gt; . If &lt;assignable\_expression&gt; is less than or equal to &lt;integer\_expr2&gt; , the loop body is executed and the &lt;assignable\_expression&gt; incremented by one. The comparison, execution of the loop body, and increment is repeated until &lt;assignable\_expression&gt; is greater than &lt;integer\_expr2&gt; .

## There is an alternate form:

```
for <assignable_expression> = <integer_expr1> downto <integer_expr2>
```

where &lt;assignable\_expression&gt; is decremented after the comparison, execution of the loop body, and decrement repeats until &lt;assignable\_expression&gt; is less than &lt;integer\_expr2&gt; .

## K13.5.5 Special statements

This section describes statements with particular architecturally defined behaviors.

## K13.5.5.1 UNDEFINED

This subsection describes the statement:

UNDEFINED;

This statement indicates a special case that replaces the behavior defined by the current pseudocode, apart from behavior required to determine that the special case applies. The replacement behavior is that the Undefined Instruction exception is taken.

## K13.5.5.2 UNPREDICTABLE

This subsection describes the statement:

UNPREDICTABLE;

This statement indicates a special case that replaces the behavior defined by the current pseudocode, apart from behavior required to determine that the special case applies. The replacement behavior is UNPREDICTABLE.

## K13.5.5.3

SEE . . .

This subsection describes the statement:

SEE &lt;reference&gt;;

This statement indicates a special case that replaces the behavior defined by the current pseudocode, apart from behavior required to determine that the special case applies. The replacement behavior is that nothing occurs as a result of the current pseudocode because some other piece of pseudocode defines the required behavior. The &lt;reference&gt; indicates where that other pseudocode can be found.

It usually refers to another instruction, but can also refer to another encoding or note of the same instruction.

## K13.5.5.4 IMPLEMENTATION\_DEFINED

This subsection describes the statement:

IMPLEMENTATION\_DEFINED {'&lt;text&gt;'};

This statement indicates a special case that replaces the behavior defined by the current pseudocode, apart from behavior required to determine that the special case applies. The replacement behavior is IMPLEMENTATION DEFINED. An optional &lt;text&gt; field can give more information.

## K13.5.6 Comments

The pseudocode supports two styles of comments:

- // starts a comment that is terminated by the end of the line.

- /* starts a comment that is terminated by */ .

/**/ statements might not be nested, and the first */ ends the comment.

Note

Comment lines do not require a terminating semicolon.