## F1.4 Shifts applied to a register

A32 register offset load/store word and unsigned byte instructions can apply a wide range of different constant shifts to the offset register. Both T32 and A32 data-processing instructions can apply the same range of different constant shifts to the second operand register. For details, see Constant shifts.

A32 data-processing instructions can apply a register-controlled shift to the second operand register.

## F1.4.1 Constant shifts

These are the same in T32 and A32 instructions, except that the input bits come from different positions.

&lt;shift&gt; is an optional shift to be applied to &lt;Rm&gt; . It can be any one of:

## (omitted) No shift.

LSL #&lt;n&gt; Logical shift left &lt;n&gt; bits. 1 &lt;= &lt;n&gt; &lt;= 31.

LSR #&lt;n&gt; Logical shift right &lt;n&gt; bits. 1 &lt;= &lt;n&gt; &lt;= 32.

ASR #&lt;n&gt; Arithmetic shift right &lt;n&gt; bits. 1 &lt;= &lt;n&gt; &lt;= 32.

- ROR #&lt;n&gt;

Rotate right &lt;n&gt; bits. 1 &lt;= &lt;n&gt; &lt;= 31.

RRX

Rotate right one bit, with extend. Bit[0] is written to shifter\_carry\_out , bits[31:1] are shifted right one bit, and the Carry flag is shifted into bit[31].

Note

Assemblers can permit the use of some or all of ASR #0 , LSL #0 , LSR #0 , and ROR #0 to specify that no shift is to be performed. This is not standard UAL, and the encoding selected for T32 instructions might vary between UAL assemblers if it is used. To ensure disassembled code assembles to the original instructions, disassemblers must omit the shift specifier when the instruction specifies no shift.

Similarly, assemblers can permit the use of #0 in the immediate forms of ASR , LSL , LSR , and ROR instructions to specify that no shift is to be performed, that is, that a MOV (register) instruction is wanted. Again, this is not standard UAL, and the encoding selected for T32 instructions might vary between UAL assemblers if it is used. To ensure disassembled code assembles to the original instructions, disassemblers must use the MOV (register) syntax when the instruction specifies no shift.

## F1.4.1.1 Encoding

The assembler encodes &lt;shift&gt; into two type bits and five immediate bits, as follows:

| (omitted)   | (omitted)   | type = 0b00 , immediate = 0.    |
|-------------|-------------|---------------------------------|
| LSL         | #<n>        | type = 0b00 , immediate = <n> . |
| LSR         | #<n>        | type = 0b01 .                   |
|             |             | If <n> < 32, immediate = <n> .  |
|             |             | If <n> == 32, immediate = 0.    |
| ASR         | #<n>        | type = 0b10 .                   |
|             |             | If <n> < 32, immediate = <n> .  |
|             |             | If <n> == 32, immediate = 0.    |
| ROR         | #<n>        | type = 0b11 , immediate = <n> . |
| RRX         |             | type = 0b11 , immediate = 0.    |

## F1.4.2 Register controlled shifts

These are available only in A32 instructions.

&lt;type&gt; is the type of shift to apply to the value read from &lt;Rm&gt; . It must be one of:

| ASR   | Arithmetic shift right, encoded as type = 0b10   |
|-------|--------------------------------------------------|
| LSL   | Logical shift left, encoded as type = 0b00 .     |
| LSR   | Logical shift right, encoded as type = 0b01 .    |
| ROR   | Rotate right, encoded as type = 0b11 .           |

The bottom byte of &lt;Rs&gt; contains the shift amount.

## F1.4.3 Pseudocode description of instruction-specified shifts and rotates

The pseudocode enumeration SRType {} defines the shift types. Shift and rotate instruction decode is described by the pseudocode function:

- DecodeImmShift() for a constant shift.
- DecodeRegShift() for a register controlled shift.

Shift and rotate operations are made by the pseudocode function Shift() .