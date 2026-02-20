## F5.1.184 SETPAN

Set Privileged Access Never writes a new value to PSTATE.PAN.

This instruction is available only in privileged mode and it is a NOP when executed in User mode.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

## A1

(FEAT\_PAN)

<!-- image -->

## Encoding

```
SETPAN{<q>} #<imm> // (Cannot be conditional)
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_PAN) then UNDEFINED; constant bit value = imm1;
```

T1

## (FEAT\_PAN)

## Encoding

```
SETPAN{<q>} #<imm> // (Not permitted in IT block)
```

## Decode for this encoding

```
if InITBlock() then UNPREDICTABLE; if !IsFeatureImplemented(FEAT_PAN) then constant bit value = imm1;
```

## Assembler Symbols

<!-- image -->

See Standard assembler syntax fields.

## &lt;imm&gt;

Is the unsigned immediate 0 or 1, encoded in the 'imm1' field.

## Operation

```
EncodingSpecificOperations(); if PSTATE.EL != EL0 then PSTATE.PAN = value;
```

<!-- image -->

```
UNDEFINED;
```