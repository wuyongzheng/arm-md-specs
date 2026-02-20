## K13.8 Arm pseudocode definition index

This section contains the following tables:

- Table K13-3 which contains the pseudocode data types.
- Table K13-4 which contains the pseudocode operators.
- Table K13-5 which contains the pseudocode keywords and control structures.
- Table K13-6 which contains the statements with special behaviors.

## Table K13-3 Index of pseudocode data types

| Keyword     | Meaning                                           |
|-------------|---------------------------------------------------|
| array       | Type name for the array type                      |
| bit         | Keyword equivalent to bits(1)                     |
| bits(N)     | Type name for the bitstring of length N data type |
| boolean     | Type name for the Boolean data type               |
| enumeration | Keyword to define a new enumeration type          |
| integer     | Type name for the integer data type               |
| real        | Type name for the real data type                  |
| type        | Keyword to define a new structure                 |

## Table K13-4 Index of pseudocode operators

| Operator   | Meaning                                                                      |
|------------|------------------------------------------------------------------------------|
| -          | Unary minus on integers or reals                                             |
| -          | Subtraction of integers, reals, and bitstrings                               |
| -          | Used in the left-hand side of an assignment or a tuple to discard the result |
| +          | Unary plus on integers or reals                                              |
| +          | Addition of integers, reals, and bitstrings                                  |
| .          | Extract named member from a list                                             |
| .          | Extract named bit or field from a register                                   |
| :          | Bitstring concatenation                                                      |
| :          | Integer range in bitstring extraction operator                               |
| !          | BooleanNOT                                                                   |
| !=         | Comparison for inequality                                                    |
| ( . . . )  | Around arguments of procedure or function                                    |
| [ . . . ]  | Around array index                                                           |
| [ . . . ]  | Around arguments of array-like function                                      |
| *          | Multiplication of integers, reals, and bitstrings                            |
| /          | Division of reals                                                            |

| Operator                     | Meaning                                                     |
|------------------------------|-------------------------------------------------------------|
| &&                           | BooleanAND                                                  |
| <                            | Less than comparison of integers and reals                  |
| < . . . >                    | Slicing of specified bits of bitstring or integer           |
| <<                           | Multiply integer by power of 2                              |
| <=                           | Less than or equal comparison of integers and reals         |
| =                            | Assignment operator                                         |
| ==                           | Comparison for equality                                     |
| >                            | Greater than comparison of integers and reals               |
| >=                           | Greater than or equal comparison of integers and reals      |
| >>                           | Divide integer by power of 2                                |
| &#124;&#124;                 | BooleanOR                                                   |
| ^                            | Exponential operator                                        |
| AND                          | Bitwise ANDof bitstrings                                    |
| DIV                          | Quotient from integer division                              |
| EOR                          | Bitwise EORof bitstrings                                    |
| IN                           | Tests membership of a certain expression in a set of values |
| MOD                          | Remainder from integer division                             |
| NOT                          | Bitwise inversion of bitstrings                             |
| OR                           | Bitwise ORof bitstrings                                     |
| case . . . of . . .          | Control structure for the                                   |
| if . . . then . . . else . . | Condition expression selecting between two values           |

## Table K13-5 Index of pseudocode keywords and control structures

| Operator                       | Meaning                                                                                     |
|--------------------------------|---------------------------------------------------------------------------------------------|
| /* . . . */                    | Comment delimiters                                                                          |
| //                             | Introduces comment terminated by end of line                                                |
| FALSE                          | One of two values a Boolean can take (other than TRUE )                                     |
| for . . . = . . . to . . .     | Loop control structure, counting up from the initial value to the upper limit               |
| for . . . = . . . downto . . . | Loop control structure, counting down from the initial value to the lower limit             |
| if . . . then . . . else . . . | Conditional control structure                                                               |
| otherwise                      | Introduces default case in case . . . of . . . control structure                            |
| repeat . . . until . . .       | Loop control structure that runs at least once until the termination condition is satisfied |
| return                         | Procedure or function return                                                                |
| TRUE                           | One of two values a Boolean can take (other than FALSE )                                    |
| when                           | Introduces specific case in case . . . of . . . control structure                           |
| while . . . do . . .           | Loop control structure that runs until the termination condition is satisfied               |

## Table K13-6 Index of special statements

| Keyword                | Meaning                                   |
|------------------------|-------------------------------------------|
| IMPLEMENTATION_DEFINED | Describes IMPLEMENTATION DEFINED behavior |
| SEE                    | Points to other pseudocode to use instead |
| UNDEFINED              | Cause Undefined Instruction exception     |
| UNKNOWN                | Unspecified value                         |
| UNPREDICTABLE          | Unspecified behavior                      |

## Appendix K14 Registers Index

This appendix provides indexes to the register descriptions in this manual. It contains the following sections:

- Introduction and register disambiguation.
- Alphabetical index of AArch64 registers and System instructions.
- Functional index of AArch64 registers and System instructions.
- Alphabetical index of AArch32 registers and System instructions.
- Functional index of AArch32 registers and System instructions.
- Alphabetical index of memory-mapped registers.
- Functional index of memory-mapped registers.