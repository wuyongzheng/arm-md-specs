## K13.4 Operators

This section describes:

- Relational operators.
- Boolean operators.
- Bitstring operators.
- Arithmetic operators.
- The assignment operator.
- Precedence rules.
- Conditional expressions.
- Operator polymorphism.

## K13.4.1 Relational operators

The following operations yield results of type boolean .

## K13.4.1.1 Equality and non-equality

If two variables x and y are of the same type, their values can be tested for equality by using the expression x == y and for non-equality by using the expression x != y . In both cases, the result is of type boolean .

Both x and y must be of type bits(N) , real , enumeration , boolean , or integer . Named values from an enumeration can only be compared if they are both from the same enumeration . An exception is that a bitstring can be tested for equality with an integer to allow a d==15 test.

Aspecial form of comparison is defined with a bitstring literal that can contain bit values '0' , '1' , and 'x' . Any bit with value 'x' is ignored in determining the result of the comparison. For example, if opcode is a 4-bit bitstring, the expression opcode == '1x0x' matches the values '1000' , '1100' , '1001', and '1101' . This is known as a bitmask.

Note

This special form is permitted in the implied equality comparisons in the when parts of case . . . of . . . structures.

## K13.4.1.2 Comparisons

If x and y are integers or reals, then x &lt; y , x &lt;= y, x &gt; y , and x &gt;= y are less than, less than or equal, greater than, and greater than or equal comparisons between them, producing Boolean results.

## K13.4.1.3 Set membership with IN

&lt;expression&gt; IN {&lt;set&gt;} produces TRUE if &lt;expression&gt; is a member of &lt;set&gt; . Otherwise, it is FALSE . &lt;set&gt; must be a list of expressions separated by commas.

## K13.4.2 Boolean operators

If x is a Boolean expression, then !x is its logical inverse.

If x and y are Boolean expressions, then x &amp;&amp; y is the result of ANDing them together. As in the C language, if x is FALSE , the result is determined to be FALSE without evaluating y .

Note

This is known as short circuit evaluation.

If x and y are boolean s, then x || y is the result of ORing them together. As in the C language, if x is TRUE , the result is determined to be TRUE without evaluating y .

Note

If x and y are boolean s or Boolean expressions, then the result of x != y is the same as the result of exclusive-ORing x and y together. The operator EOR only accepts bitstring arguments.

## K13.4.3 Bitstring operators

The following operations can be applied only to bitstrings.

## K13.4.3.1 Logical operations on bitstrings

If x is a bitstring, NOT(x) is the bitstring of the same length obtained by logically inverting every bit of x .

If x and y are bitstrings of the same length, x AND y , x OR y , and x EOR y are the bitstrings of that same length obtained by logically ANDing, logically ORing, and exclusive-ORing corresponding bits of x and y together.

## K13.4.3.2 Bitstring concatenation and slicing

If x and y are bitstrings of lengths N and M respectively, then x:y is the bitstring of length N+M constructed by concatenating x and y in left-to-right order.

The bitstring slicing operator addresses specific bits in a bitstring. This can be used to create a new bitstring from extracted bits or to set the value of specific bits. Its syntax is x&lt;integer\_list&gt; , where x is the integer or bitstring being sliced, and &lt;integer\_list&gt; is a comma-separated list of integers enclosed in angle brackets. The length of the resulting bitstring is equal to the number of integers in &lt;integer\_list&gt; . In x&lt;integer\_list&gt; , each of the integers in &lt;integer\_list&gt; must be:

- &gt;= 0 .
- &lt; Len(x) if x is a bitstring.

The definition of x&lt;integer\_list&gt; depends on whether integer\_list contains more than one integer:

- If integer\_list contains more than one integer, x&lt;i, j, k, . . . , n&gt; is defined to be the concatenation: x&lt;i&gt; : x&lt;j&gt; : x&lt;k&gt; : . . . : x&lt;n&gt; .
- If integer\_list consists of just one integer i , x&lt;i&gt; is defined to be:
- -If x is a bitstring, '0' if bit i of x is a zero and '1' if bit i of x is a one.
- -If x is an integer, and y is the unique integer in the range 0 to 2^(i+1)-1 that is congruent to x modulo 2^(i+1) . Then x&lt;i&gt; is '0' if y &lt; 2^i and '1' if y &gt;= 2^i . Loosely, this definition treats an integer as equivalent to a sufficiently long two's complement representation of it as a bitstring.

The notation for a range expression is i:j with i &gt;= j is shorthand for the integers in order from i down to j , with both end values included. For example, instr&lt;31:28&gt; represents instr&lt;31, 30, 29, 28&gt; .

x&lt;integer\_list&gt; is assignable provided x is an assignable bitstring and no integer appears more than once in &lt;integer\_list&gt; . In particular, x&lt;i&gt; is assignable if x is an assignable bitstring and 0 &lt;= i &lt; Len(x) .

Encoding diagrams for registers frequently show named bits or multi-bit fields. For example, the encoding diagram for the APSR shows its bit&lt;31&gt; as N . In such cases, the syntax APSR.N is used as a more readable synonym for APSR&lt;31&gt; as named bits can be referred to with the same syntax as referring to members of a struct. A comma-separated list of named bits enclosed in angle brackets following the register name allows multiple bits to be addressed simultaneously. For example, APSR.&lt;N, C, Q&gt; is synonymous with APSR &lt;31, 29, 27&gt; .

## K13.4.4 Arithmetic operators

Most pseudocode arithmetic is performed on integer or real values, with operands obtained by conversions from bitstrings and results converted back to bitstrings. As these data types are the unbounded mathematical types, no issues arise about overflow or similar errors.

## K13.4.4.1 Unary plus and minus

If x is an integer or real, then +x is x unchanged, -x is x with its sign reversed. Both are of the same type as x .

## K13.4.4.2 Addition and subtraction

If x and y are integers or reals, x+y and x-y are their sum and difference. Both are of type integer if x and y are both of type integer , and real otherwise.

There are two cases where the types of x and y can be different. A bitstring and an integer can be added together to allow the operation PC + 4 . An integer can be subtracted from a bitstring to allow the operation PC -2 .

If x and y are bitstrings of the same length N , so that N = Len(x) = Len(y) , then x+y and x-y are the least significant N bits of the results of converting x and y to integers and adding or subtracting them. Signed and unsigned conversions produce the same result:

```
x+y = (SInt(x) + SInt(y))<N-1:0> = (UInt(x) + UInt(y))<N-1:0> x-y = (SInt(x) SInt(y))<N-1:0> = (UInt(x) UInt(y))<N-1:0>
```

If x is a bitstring of length N and y is an integer, x+y and x-y are the bitstrings of length N defined by x+y = x + y&lt;N-1:0&gt; and x-y = x -y&lt;N-1:0&gt; . Similarly, if x is an integer and y is a bitstring of length M , x+y and x-y are the bitstrings of length M defined by x+y = x&lt;M-1:0&gt; + y and x-y = x&lt;M-1:0&gt; -y .

## K13.4.4.3 Multiplication

If x and y are integers or reals, then x * y is the product of x and y . It is of type integer if x and y are both of type integer , and real otherwise.

## K13.4.4.4 Division and modulo

If x and y are reals, then x/y is the result of dividing x by y , and is always of type real .

If x and y are integers, then x DIV y and x MOD y are defined by:

```
x DIV y = RoundDown(x/y) x MOD y = x - y * (x DIV
```

```
y)
```

It is a pseudocode error to use any of x/y , x MOD y , or x DIV y in any context where y can be zero.

## K13.4.4.5 Scaling

If x and n are of type integer , then:

```
· x << n = RoundDown(x * 2^n) . · x >> n = RoundDown(x * 2^(-n))
```

## K13.4.4.6 Raising to a power

If x is an integer or a real and n is an integer, then x^n is the result of raising x to the power of n , and:

- If x is of type integer , then x^n is of type integer .
- If x is of type real , then x^n is of type real .

## K13.4.5 The assignment operator

The assignment operator is the = character, which assigns the value of the right-hand side to the left-hand side. An assignment statement takes the form:

```
<assignable_expression> = <expression>;
```

This following subsection defines valid expression syntax.

- .

## K13.4.5.1 General expression syntax

An expression is one of the following:

- Aliteral.
- Avariable, optionally preceded by a data type name to declare its type.
- The word UNKNOWN preceded by a data type name to declare its type.
- The result of applying a language-defined operator to other expressions.
- The result of applying a function to other expressions.

Variable names normally consist of alphanumeric and underscore characters, starting with an alphabetic or underscore character.

Each register defined in an Arm architecture specification defines a correspondingly named pseudocode bitstring variable, and that variable has the stated behavior of the register. For example, if a bit of a register is defined as RAZ/WI, then the corresponding bit of its variable reads as '0' and ignore writes.

An expression like bits(32) UNKNOWN indicates that the result of the expression is a value of the given type, but the architecture does not specify what value it is and software must not rely on such values. The value produced must not:

- Return information that cannot be accessed at the current or a lower level of privilege using instructions that are not UNPREDICTABLE or CONSTRAINED UNPREDICTABLE and do not return UNKNOWN values,
- Be promoted as providing any useful information to software.

Note

UNKNOWN values are similar to the definition of UNPREDICTABLE, but do not indicate that the entire architectural state becomes unspecified.

Only the following expressions are assignable. This means that these are the only expressions that can be placed on the left-hand side of an assignment.

- Variables.
- The results of applying some operators to other expressions.
- The description of each language-defined operator that can generate an assignable expression specifies the circumstances under which it does so. For example, those circumstances might require that one or more of the expressions the operator operates on is an assignable expression.
- The results of applying array-like functions to other expressions. The description of an array-like function specifies the circumstances under which it can generate an assignable expression.

Note

If the right-hand side in an assignment is a function returning a tuple, an item in the assignment destination can be written as - to indicate that the corresponding item of the assigned tuple value is discarded. For example:

```
(shifted, -) = LSL_C(operand, amount);
```

The expression on the right-hand side itself can be a tuple. For example:

```
(x, y) = (function_1(), function_2());
```

Every expression has a data type.

- For a literal, this data type is determined by the syntax of the literal.
- For a variable, there are the following possible sources for the data type
- -An optional preceding data type name.
- -Adata type the variable was given earlier in the pseudocode by recursive application of this rule.
- -Adata type the variable is being given by assignment, either by direct assignment to the variable, or by assignment to a list of which the variable is a member.

It is a pseudocode error if none of these data type sources exists for a variable, or if more than one of them exists and they do not agree about the type.

- For a language-defined operator, the definition of the operator determines the data type.
- For a function, the definition of the function determines the data type.

## K13.4.6 Precedence rules

The precedence rules for expressions are:

1. Literals, variables and function invocations are evaluated with higher priority than any operators using their results, but see Boolean operators.
2. Operators on integers follow the normal operator precedence rules of exponentiation before multiply/divide before add/subtract , with sequences of multiply/divides or add/subtracts evaluated left-to-right.
3. Other expressions must be parenthesized to indicate operator precedence if ambiguity is possible, but need not be if all permitted precedence orders under the type rules necessarily lead to the same result. For example, if i , j and k are integer variables, i &gt; 0 &amp;&amp; j &gt; 0 &amp;&amp; k &gt; 0 is acceptable, but i &gt; 0 &amp;&amp; j &gt; 0 || k &gt; 0 is not.

## K13.4.7 Conditional expressions

If x and y are two values of the same type and t is a value of type boolean , then if t then x else y is an expression of the same type as x and y that produces x if t is TRUE and y if t is FALSE .

## K13.4.8 Operator polymorphism

Operators in pseudocode can be polymorphic, with different functionality when applied to different data types. Each resulting form of an operator has a different prototype definition. For example, the operator + has forms that act on various combinations of integers, reals and bitstrings.

Table K13-1 summarizes the operand types valid for each unary operator and the result type. Table K13-2 summarizes the operand types valid for each binary operator and the result type.

Table K13-1 Result and operand types permitted for unary operators

| Operator   | Operand Type   | Result Type   |
|------------|----------------|---------------|
| -          | integer        | integer       |
| NOT        | bits(N)        | bits(N)       |
| !          | boolean        | boolean       |

Table K13-2 Result and operand types permitted for binary operators

| Operator   | First operand type   | Second operand type   | Result type   |
|------------|----------------------|-----------------------|---------------|
| ==         | bits(N)              | integer               | boolean       |
|            |                      | bits(N)               |               |
|            | integer              | integer               |               |
|            | real                 | real                  |               |

| Operator          | First operand type   | Second operand type   | Result type   |
|-------------------|----------------------|-----------------------|---------------|
|                   | enumeration          | enumeration           |               |
|                   | boolean              | boolean               |               |
| !=                | bits(N)              | bits(N)               | boolean       |
|                   | integer              | integer               |               |
|                   | real                 | real                  |               |
| < , >             | integer              | integer               | boolean       |
| <= , >=           | real                 | real                  |               |
| + , -             | integer              | integer               | integer       |
|                   | real                 | real                  | real          |
|                   | bits(N)              | bits(N)               | bits(N)       |
|                   |                      | integer               |               |
| << , >>           | integer              | integer               | integer       |
| *                 | integer              | integer               | integer       |
|                   | real                 | real                  | real          |
|                   | bits(N)              | bits(N)               | bits(N)       |
| /                 | real                 | real                  | real          |
| DIV               | integer              | integer               | integer       |
| MOD               | integer              | integer               | integer       |
|                   | bits(N)              | integer               |               |
| && , &#124;&#124; | boolean              | boolean               | boolean       |
| AND , OR , EOR    | bits(N)              | bits(N)               | bits(N)       |
| ^                 | integer              | integer               | integer       |
|                   | real                 | integer               | real          |