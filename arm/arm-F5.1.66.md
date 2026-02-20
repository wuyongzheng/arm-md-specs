## F5.1.66 LDC (literal)

Load data to System register (literal) calculates an address from the PC value and an immediate offset, loads a word from memory, and writes it to the DBGDTRTXint System register. For information about memory accesses, see Memory accesses.

In an implementation that includes EL2, the permitted LDC access to DBGDTRTXint can be trapped to Hyp mode, meaning that an attempt to execute an LDC instruction in a Non-secure mode other than Hyp mode, that would be permitted in the absence of the Hyp trap controls, generates a Hyp Trap exception. For more information, see HDCR.TDA.

For simplicity, the LDC pseudocode does not show this possible trap to Hyp mode.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
Applies when (!(P == '0' && U == '0' && W == '0')) LDC{<c>}{<q>} p14, c5, <label> // (Preferred syntax) LDC{<c>}{<q>} p14, c5, [PC, #{+/-}<imm>] LDC{<c>}{<q>} p14, c5, [PC], <option>
```

## Decode for this encoding

```
if P == '0' && U == '0' && W == '0' then UNDEFINED; constant boolean index = (P == '1'); constant boolean add = (U == '1'); constant integer cp = 14; constant bits(32) imm32 = ZeroExtend(imm8:'00', 32); if W == '1' || (P == '0' && CurrentInstrSet() !=
```

```
InstrSet_A32) then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If W == '1' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes without writeback of the base address.
- The instruction uses the addressing mode described in the equivalent immediate offset instruction.

T1

<!-- image -->

## Encoding

Applies when (!(P == '0' &amp;&amp; U == '0' &amp;&amp; W ==

LDC{&lt;c&gt;}{&lt;q&gt;} p14, c5, &lt;label&gt; // (Preferred

```
LDC{<c>}{<q>}
```

```
'0')) syntax) p14, c5, [PC, #{+/-}<imm>]
```

## Decode for this encoding

```
if P == '0' && U == '0' && W == '0' then UNDEFINED; constant boolean index = (P == '1'); constant boolean add = (U == '1'); constant integer cp = 14; constant bits(32) imm32 = ZeroExtend(imm8:'00', 32); if W == '1' || (P == '0' && CurrentInstrSet() !=
```

```
InstrSet_A32) then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If W == '1' || P == '0' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes without writeback of the base address.
- The instruction executes as LDC (immediate) with writeback to the PC. The instruction is handled as described in Using R15.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

&lt;q&gt;

See Standard assembler syntax fields.

## &lt;label&gt;

The label of the literal data item that is to be loaded into &lt;Rt&gt; . The assembler calculates the required value of the offset from the Align(PC, 4) value of the instruction to this label. Permitted values of the offset are multiples of 4 in the range -1020 to 1020.

If the offset is zero or positive, imm32 is equal to the offset and add == TRUE (encoded as U == 1).

If the offset is negative, imm32 is equal to minus the offset and add == FALSE (encoded as U == 0) .

Specifies the offset is added to or subtracted from the base register, defaulting to + if omitted and encoded in 'U':

+/-

L

## &lt;imm&gt;

Is the immediate offset used for forming the address, a multiple of 4 in the range 0-1020, defaulting to 0 and encoded in the 'imm8' field, as &lt;imm&gt;/4.

## &lt;option&gt;

Is an 8-bit immediate, in the range 0 to 255 enclosed in { }, encoded in the 'imm8' field. The value of this field is ignored when executing this instruction.

The alternative syntax permits the addition or subtraction of the offset and the immediate offset to be specified separately, including permitting a subtraction of 0 that cannot be specified using the normal syntax. For more information, see Use of labels in UAL instruction syntax.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) offset_addr = (if add then (Align(PC32,4) + imm32) else (Align(PC32,4) imm32)); constant bits(32) address = if index then offset_addr else Align(PC32,4); // System register write to DBGDTRTXint. AArch32.SysRegWriteM(cp, ThisInstr(), address);
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

|   U | +/-   |
|-----|-------|
|   0 | -     |
|   1 | +     |