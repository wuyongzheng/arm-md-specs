## F5.1.171 RSC, RSCS (register)

Reverse Subtract with Carry (register) subtracts a register value and the value of NOT (Carry flag) from an optionally-shifted register value, and writes the result to the destination register.

If the destination register is not the PC, the RSCS variant of the instruction updates the condition flags based on the result.

The field descriptions for &lt;Rd&gt; identify the encodings where the PC is permitted as the destination register. ARM deprecates any use of these encodings. However, when the destination register is the PC:

- The RSC variant of the instruction is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.
- The RSCS variant of the instruction performs an exception return without the use of the stack. In this case:
- The PE branches to the address written to the PC, and restores PSTATE from SPSR\_&lt;current\_mode&gt;.
- The PE checks SPSR\_&lt;current\_mode&gt; for an illegal return event. See Illegal return events from AArch32 state.
- The instruction is UNDEFINED in Hyp mode.
- The instruction is CONSTRAINED UNPREDICTABLE in User mode and System mode.

<!-- image -->

## Encoding for the RSC, rotate right with extend variant

```
Applies when (S == 0 && imm5 == 00000 && stype ==
```

```
RSC{<c>}{<q>}
```

```
11) {<Rd>, }<Rn>, <Rm>, RRX
```

## Encoding for the RSC, shift or rotate by value variant

```
Applies when
```

```
RSC{<c>}{<q>} {<Rd>, }<Rn>, <Rm> {, <shift>
```

```
(S == 0 && !(imm5 == 00000 && stype == 11)) #<amount>}
```

## Encoding for the RSCS, rotate right with extend variant

```
Applies when (S == 1 && imm5 == 00000 && stype ==
```

```
RSCS{<c>}{<q>}
```

```
11) {<Rd>, }<Rn>, <Rm>, RRX
```

## Encoding for the RSCS, shift or rotate by value variant

```
Applies when (S == 1 && !(imm5 == 00000 && stype ==
```

```
RSCS{<c>}{<q>} {<Rd>, }<Rn>, <Rm> {, <shift>
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean setflags = (S == '1'); SRType shift_t; integer shift_n; (shift_t, shift_n) = DecodeImmShift(stype,
```

```
imm5);
```

```
11)) #<amount>}
```

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the general-purpose destination register, encoded in the 'Rd' field. If omitted, this register is the same as &lt;Rn&gt; . Arm deprecates using the PC as the destination register, but if the PC is used:

- For the RSC variant, the instruction is a branch to the address calculated by the operation. This is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.
- For the RSCS variant, the instruction performs an exception return, that restores PSTATE from SPSR\_&lt;current\_mode&gt;.

## &lt;q&gt;

## &lt;Rd&gt;

## &lt;Rn&gt;

Is the first general-purpose source register, encoded in the 'Rn' field. The PC can be used, but this is deprecated.

## &lt;Rm&gt;

Is the second general-purpose source register, encoded in the 'Rm' field. The PC can be used, but this is deprecated.

## &lt;shift&gt;

Is the type of shift to be applied to the second source register, encoded in 'stype':

|   stype | <shift>   |
|---------|-----------|
|      00 | LSL       |
|      01 | LSR       |
|      10 | ASR       |
|      11 | ROR       |

## &lt;amount&gt;

Is the shift amount, in the range 1 to 31 (when &lt;shift&gt; = LSL or ROR) or 1 to 32 (when &lt;shift&gt; = LSR or ASR) encoded in the 'imm5' field as &lt;amount&gt; modulo 32.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) shifted = Shift(R[m], shift_t, shift_n, PSTATE.C); bits(32) result; bits(4) nzcv; (result, nzcv) = AddWithCarry(NOT(R[n]), shifted, PSTATE.C); if d == 15 then if setflags then ALUExceptionReturn(result); else ALUWritePC(result); else R[d] = result;
```

```
if setflags then PSTATE.<N,Z,C,V> = nzcv;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.