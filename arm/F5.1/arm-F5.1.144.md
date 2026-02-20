## F5.1.144 PUSH (multiple registers)

Push multiple registers to Stack stores multiple general-purpose registers to the stack, storing to consecutive memory locations ending just below the address in SP, and updates SP to point to the start of the stored data.

This is an alias of STMDB, STMFD. This means:

- The encodings in this description are named to match the encodings of STMDB, STMFD.
- The description of STMDB, STMFD gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the A1 variant

PUSH{&lt;c&gt;}{&lt;q&gt;} &lt;registers&gt;

## is equivalent to

```
STMDB{<c>}{<q>} SP!, <registers>
```

and is the preferred disassembly when BitCount(register\_list) &gt; 1 .

T1

<!-- image -->

## Encoding for the T1 variant

```
PUSH{<c>}{<q>} <registers>
```

```
PUSH{<c>}.W <registers> // (register_list[13:8] == '000000')
```

## is equivalent to

```
STMDB{<c>}{<q>} SP!, <registers>
```

and is the preferred disassembly when BitCount(M :: register\_list) &gt; 1 .

## Assembler Symbols

<!-- image -->

See Standard assembler syntax fields.

<!-- image -->

See Standard assembler syntax fields.

## &lt;registers&gt;

For the 'A1' variant: is a list of two or more registers to be stored, separated by commas and surrounded by { and }. The lowest-numbered register is stored to the lowest memory address, through to the highest-numbered register to the highest memory address. See also Encoding of lists of general-purpose registers and the PC.

The SP and PC can be in the list. However:

- Arm deprecates the use of instructions that include the PC in the list.
- If the SP is in the list, and it is not the lowest-numbered register in the list, the instruction stores an UNKNOWN value for the SP.

For the 'T1' variant: is a list of one or more registers to be stored, separated by commas and surrounded by { and }. The lowest-numbered register is stored to the lowest memory address, through to the highest-numbered register to the highest memory address. See also Encoding of lists of general-purpose registers and the PC.

The registers in the list must be in the range R0-R12, encoded in the 'register\_list' field, and can optionally contain the LR. If the LR is in the list, the 'M' field is set to 1, otherwise it defaults to 0.

## Operation

The description of STMDB, STMFD gives the operational pseudocode for this instruction.

## Operational Information

The description of STMDB, STMFD gives the operational information for this instruction.