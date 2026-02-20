## F5.1.183 SETEND

Set Endianness writes a new value to PSTATE.E.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
SETEND{<q>} <endian_specifier> // (Cannot be conditional)
```

## Decode for this encoding

```
constant boolean set_bigend = (E == '1');
```

T1

## Encoding

```
SETEND{<q>} <endian_specifier> // (Not permitted in IT block)
```

## Decode for this encoding

```
constant boolean set_bigend = (E == '1'); if InITBlock() then UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

<!-- image -->

See Standard assembler syntax fields.

## &lt;endian\_specifier&gt;

Is the endianness to be selected, and the value to be set in PSTATE.E, encoded in 'E':

<!-- image -->

## Operation

```
EncodingSpecificOperations(); AArch32.CheckSETENDEnabled(); PSTATE.E = if set_bigend then '1' else
```

'0';

|   E | <endian_specifier>   |
|-----|----------------------|
|   0 | LE                   |
|   1 | BE                   |