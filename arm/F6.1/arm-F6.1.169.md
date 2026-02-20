## F6.1.169 VPOP

Pop SIMD&amp;FP registers from stack loads multiple consecutive Advanced SIMD and floating-point register file registers from the stack.

This is an alias of VLDM, VLDMDB, VLDMIA. This means:

- The encodings in this description are named to match the encodings of VLDM, VLDMDB, VLDMIA.
- The description of VLDM, VLDMDB, VLDMIA gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

It has encodings from the following instruction sets: A32 (A1 and A2) and T32 (T1 and T2).

A1

<!-- image -->

W

## Encoding for the Increment After variant

<!-- image -->

and is always the preferred disassembly.

A2

<!-- image -->

## Encoding for the Increment After variant

<!-- image -->

and is always the preferred disassembly.

T1

<!-- image -->

W

## Encoding for the Increment After variant

```
VPOP{<c>}{<q>}{.<size>} <dreglist>
```

## is equivalent to

```
VLDM{<c>}{<q>}{.<size>} SP!, <dreglist>
```

and is always the preferred disassembly.

T2

<!-- image -->

W

## Encoding for the Increment After variant

```
VPOP{<c>}{<q>}{.<size>} <sreglist>
```

## is equivalent to

```
VLDM{<c>}{<q>}{.<size>} SP!, <sreglist>
```

and is always the preferred disassembly.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

&lt;q&gt;

See Standard assembler syntax fields.

## &lt;size&gt;

An optional data size specifier. If present, it must be equal to the size in bits, 32 or 64, of the registers being transferred.

## &lt;dreglist&gt;

Is the list of consecutively numbered 64-bit SIMD&amp;FP registers to be transferred. The first register in the list is encoded in 'D:Vd', and 'imm8' is set to twice the number of registers in the list. The list must contain at least one register, and must not contain more than 16 registers.

## &lt;sreglist&gt;

Is the list of consecutively numbered 32-bit SIMD&amp;FP registers to be transferred. The first register in the list is encoded in 'Vd:D', and 'imm8' is set to the number of registers in the list. The list must contain at least one register.

## Operation

The description of VLDM, VLDMDB, VLDMIA gives the operational pseudocode for this instruction.

## Operational Information

The description of VLDM, VLDMDB, VLDMIA gives the operational information for this instruction.