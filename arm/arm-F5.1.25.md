## F5.1.25 BL, BLX (immediate)

Branch with Link and optional Exchange (immediate)

Branch with Link calls a subroutine at a PC-relative address, and setting LR to the return address.

Branch with Link and Exchange Instruction Sets (immediate) calls a subroutine at a PC-relative address, setting LR to the return address, and changes the instruction set from A32 to T32, or from T32 to A32.

It has encodings from the following instruction sets: A32 (A1 and A2) and T32 (T1 and T2).

A1

<!-- image -->

## Encoding

```
BL{<c>}{<q>} <label>
```

## Decode for this encoding

```
constant bits(32) imm32 = SignExtend(imm24:'00', 32); constant InstrSet targetInstrSet = InstrSet_A32;
```

A2

<!-- image -->

## Encoding

```
BLX{<c>}{<q>} <label>
```

## Decode for this encoding

```
constant bits(32) imm32 = constant InstrSet targetInstrSet = InstrSet_T32;
```

T1

<!-- image -->

## Encoding

<!-- image -->

```
SignExtend(imm24:H:'0', 32);
```

## Decode for this encoding

```
constant bit I1 = NOT(J1 EOR S); constant bit I2 = NOT(J2 EOR S); constant bits(32) imm32 = SignExtend(S:I1:I2:imm10:imm11:'0', 32); constant InstrSet targetInstrSet = InstrSet_T32; if InITBlock() && !LastInITBlock() then UNPREDICTABLE;
```

T2

<!-- image -->

| 15   | 13 12 11 10 9   | 0 15 14 13 12 11 10 1 0   |
|------|-----------------|---------------------------|
| 1 1  | 1 1 0 S         | 1 1 J1 0 J2 imm10L H      |

## Encoding

```
BLX{<c>}{<q>} <label>
```

## Decode for this encoding

```
if H == '1' then UNDEFINED; constant bit I1 = NOT(J1 EOR S); constant bit I2 = NOT(J2 EOR S); constant bits(32) imm32 = constant InstrSet targetInstrSet = InstrSet_A32; if InITBlock() && !LastInITBlock() then UNPREDICTABLE;
```

```
SignExtend(S:I1:I2:imm10H:imm10L:'00', 32);
```

For more information about the CONSTRAINED UNPREDICTABLE behavior, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

For the 'A1', 'T1', and 'T2' variants: see Standard assembler syntax fields.

For the 'A2' variant: see Standard assembler syntax fields. &lt;c&gt; must be AL or omitted.

See Standard assembler syntax fields.

## &lt;label&gt;

For the 'A1' variant: the label of the instruction that is to be branched to. The assembler calculates the required value of the offset from the PC value of the BL instruction to this label, then selects an encoding that sets imm32 to that offset.

Permitted offsets are multiples of 4 in the range -33554432 to 33554428.

For the 'A2' variant: the label of the instruction that is to be branched to. The assembler calculates the required value of the offset from the PC value of the BLX instruction to this label, then selects an encoding with imm32 set to that offset.

Permitted offsets are even numbers in the range -33554432 to 33554430.

For the 'T1' variant: the label of the instruction that is to be branched to.

The assembler calculates the required value of the offset from the PC value of the BL instruction to this label, then selects an encoding with imm32 set to that offset.

Permitted offsets are even numbers in the range -16777216 to 16777214.

&lt;q&gt;

For the 'T2' variant: the label of the instruction that is to be branched to.

The assembler calculates the required value of the offset from the Align(PC, 4) value of the BLX instruction to this label, then selects an encoding with imm32 set to that offset.

Permitted offsets are multiples of 4 in the range -16777216 to 16777212.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); if CurrentInstrSet() == InstrSet_A32 then LR = PC32 - 4; else LR = PC32<31:1> : '1'; bits(32) targetAddress; if targetInstrSet == InstrSet_A32 then targetAddress = Align(PC32,4) + imm32; else targetAddress = PC32 + imm32; SelectInstrSet(targetInstrSet); BranchWritePC(targetAddress, BranchType_DIRCALL);
```