## F5.1.140 POP (multiple registers)

Pop Multiple Registers from Stack loads multiple general-purpose registers from the stack, loading from consecutive memory locations starting at the address in SP, and updates SP to point just above the loaded data.

This is an alias of LDM, LDMIA, LDMFD. This means:

- The encodings in this description are named to match the encodings of LDM, LDMIA, LDMFD.
- The description of LDM, LDMIA, LDMFD gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

It has encodings from the following instruction sets: A32 (A1) and T32 (T2).

A1

<!-- image -->

## Encoding for the A1 variant

```
POP{<c>}{<q>} <registers>
```

## is equivalent to

```
LDM{IA}{<c>}{<q>} SP!, <registers>
```

and is the preferred disassembly when BitCount(register\_list) &gt; 1 .

T2

<!-- image -->

## Encoding for the T2 variant

```
POP{<c>}{<q>} <registers>
```

```
POP{<c>}.W <registers> // (M == 0 && register_list[13:8] == '000000')
```

## is equivalent to

```
LDM{IA}{<c>}.W SP!, <registers>
```

and is the preferred disassembly when BitCount(P :: M :: register\_list) &gt; 1 .

## Assembler Symbols

<!-- image -->

See Standard assembler syntax fields.

<!-- image -->

See Standard assembler syntax fields.

## &lt;registers&gt;

For the 'A1' variant: is a list of two or more registers to be loaded, separated by commas and surrounded by { and }. The lowest-numbered register is loaded from the lowest memory address, through to the highest-numbered register from the highest memory address. See also Encoding of lists of general-purpose registers and the PC.

If the SP is in the list, the value of the SP after such an instruction is UNKNOWN.

The PC can be in the list. If it is, the instruction branches to the address loaded to the PC. This is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.

Arm deprecates the use of this instruction with both the LR and the PC in the list.

For the 'T2' variant: is a list of two or more registers to be loaded, separated by commas and surrounded by { and }. The lowest-numbered register is loaded from the lowest memory address, through to the highest-numbered register from the highest memory address. See also Encoding of lists of general-purpose registers and the PC.

The registers in the list must be in the range R0-R12, encoded in the 'register\_list' field, and can optionally contain one of the LR or the PC. If the LR is in the list, the 'M' field is set to 1, otherwise it defaults to 0. If the PC is in the list, the 'P' field is set to 1, otherwise it defaults to 0.

The PC can be in the list. If it is, the instruction branches to the address loaded to the PC. This is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC. If the PC is in the list:

- The LR must not be in the list.
- The instruction must be either outside any IT block, or the last instruction in an IT block.

## Operation

The description of LDM, LDMIA, LDMFD gives the operational pseudocode for this instruction.

## Operational Information

The description of LDM, LDMIA, LDMFD gives the operational information for this instruction.