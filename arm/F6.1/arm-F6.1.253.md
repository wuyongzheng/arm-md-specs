## F6.1.253 VTBL, VTBX

Vector Table Lookup and Extension

Vector Table Lookup uses byte indexes in a control vector to look up byte values in a table and generate a new vector. Indexes out of range return 0.

Vector Table Extension works in the same way, except that indexes out of range leave the destination element unchanged.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the VTBL variant

```
Applies when (op == 0) VTBL{<c>}{<q>}.8 <Dd>,
```

```
<list>, <Dm>
```

## Encoding for the VTBX variant

```
Applies when (op == 1) VTBX{<c>}{<q>}.8 <Dd>, <list>, <Dm>
```

## Decode for all variants of this encoding

```
constant boolean is_vtbl = (op == '0'); constant integer length = UInt(len)+1; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); if n+length > 32 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If n + length &gt; 32 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- One or more of the SIMD and floating-point registers are UNKNOWN. This behavior does not affect any general-purpose registers.

T1

<!-- image -->

## Encoding for the VTBL variant

```
Applies when (op == 0) VTBL{<c>}{<q>}.8 <Dd>, <list>, <Dm>
```

## Encoding for the VTBX variant

Applies when (op ==

```
1)
```

```
VTBX{<c>}{<q>}.8 <Dd>,
```

```
<list>, <Dm>
```

## Decode for all variants of this encoding

```
constant boolean is_vtbl = (op == '0'); constant integer length = UInt(len)+1; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); if n+length > 32 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If n + length &gt; 32 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- One or more of the SIMD and floating-point registers are UNKNOWN. This behavior does not affect any general-purpose registers.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

For the 'A1 VTBL' and 'A1 VTBX' variants: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1 VTBL' and 'T1 VTBX' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

The vectors containing the table. It must be one of:

&lt;q&gt;

## &lt;Dd&gt;

&lt;list&gt;

```
{<Dn>} Encoded as len = 0b00 . {<Dn>, <Dn+1>} Encoded as len = 0b01 . {<Dn>, <Dn+1>, <Dn+2>} Encoded as len = 0b10 . {<Dn>, <Dn+1>, <Dn+2>, <Dn+3>} Encoded as len = 0b11 .
```

## &lt;Dm&gt;

Is the 64-bit name of the SIMD&amp;FP source register holding the indices, encoded in the 'M:Vm' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); // Create 256-bit = 32-byte table variable, with zeros in entries that will not be used. constant bits(64) table3 = if length == 4 then D[n+3] else Zeros(64); constant bits(64) table2 = if length >= 3 then D[n+2] else Zeros(64); constant bits(64) table1 = if length >= 2 then D[n+1] else Zeros(64); constant bits(256) table = table3 : table2 : table1 : D[n]; for i = 0 to 7 constant integer index = UInt(Elem[D[m],i,8]); if index < 8*length then Elem[D[d],i,8] = Elem[table,index,8]; else if is_vtbl then Elem[D[d],i,8] = Zeros(8); // else Elem[D[d],i,8] unchanged
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.