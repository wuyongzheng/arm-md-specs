## K13.1 About the Arm pseudocode

The Arm pseudocode provides precise descriptions of some areas of the Arm architecture. This includes description of the decoding and operation of all valid instructions. Pseudocode for instruction descriptions gives general information about this instruction pseudocode, including its limitations.

The following sections describe the Arm pseudocode in detail:

- Data types.
- Operators.
- Statements and control structures.

Built-in functions and Miscellaneous helper procedures and functions describe some built-in functions and pseudocode helper functions that are used by the pseudocode functions that are described elsewhere in this manual. Arm pseudocode definition index contains the indexes to the pseudocode.

## K13.1.1 General limitations of Arm pseudocode

The pseudocode statements IMPLEMENTATION\_DEFINED , SEE , UNDEFINED , and UNPREDICTABLE indicate behavior that differs from that indicated by the pseudocode being executed. If one of them is encountered:

- Earlier behavior indicated by the pseudocode is only specified as occurring to the extent required to determine that the statement is executed.
- No subsequent behavior indicated by the pseudocode occurs.

For more information, see Special statements.