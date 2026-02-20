## F5.1.26 BLX (register)

Branch with Link and Exchange (register) calls a subroutine at an address specified in the register, and if necessary changes to the instruction set indicated by bit[0] of the register value. If the value in bit[0] is 0, the instruction set after the branch will be A32. If the value in bit[0] is 1, the instruction set after the branch will be T32.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
BLX{<c>}{<q>} <Rm>
```

## Decode for this encoding

```
constant integer m = UInt(Rm); if m == 15 then UNPREDICTABLE;
```

T1

## Encoding

```
BLX{<c>}{<q>} <Rm>
```

## Decode for this encoding

```
constant integer m = UInt(Rm); if m == 15 then UNPREDICTABLE; if InITBlock() && !LastInITBlock() then UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

<!-- image -->

See Standard assembler syntax fields.

<!-- image -->

See Standard assembler syntax fields.

&lt;Rm&gt;

Is the general-purpose register holding the address to be branched to, encoded in the 'Rm' field.

<!-- image -->

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) target = R[m]; bits(32) next_instr_addr; if CurrentInstrSet() == InstrSet_A32 then next_instr_addr = PC32 - 4; LR = next_instr_addr; else next_instr_addr = PC32 - 2; LR = next_instr_addr<31:1> : '1'; BXWritePC(target, BranchType_INDCALL);
```