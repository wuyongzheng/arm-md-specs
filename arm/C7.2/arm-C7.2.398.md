## C7.2.398 TBX

Table vector lookup extension

This instruction reads each value from the vector elements in the index source SIMD&amp;FP register, uses each result as an index to perform a lookup in a table of bytes that is described by one to four source table SIMD&amp;FP registers, places the lookup result in a vector, and writes the vector to the destination SIMD&amp;FP register. If an index is out of range for the table, the existing value in the vector element of the destination register is left unchanged. If more than one source register is used to describe the table, the first source register describes the lowest bytes of the table.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

## Advanced SIMD

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding for the Single register table variant

```
Applies when (len == 00)
```

```
TBX <Vd>.<Ta>, { <Vn>.16B
```

```
}, <Vm>.<Ta>
```

## Encoding for the Two register table variant

```
Applies when (len == 01) TBX <Vd>.<Ta>, { <Vn>.16B, <Vn+1>.16B }, <Vm>.<Ta>
```

## Encoding for the Three register table variant

```
Applies when (len == 10) TBX <Vd>.<Ta>, { <Vn>.16B, <Vn+1>.16B, <Vn+2>.16B }, <Vm>.<Ta>
```

## Encoding for the Four register table variant

```
Applies when (len == 11)
```

```
TBX <Vd>.<Ta>, { <Vn>.16B, <Vn+1>.16B, <Vn+2>.16B, <Vn+3>.16B
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF);
```

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV 8; constant integer regs = UInt(len) + 1; constant boolean is_tbl = (op == '0');
```

```
}, <Vm>.<Ta>
```

## Assembler Symbols

## &lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is an arrangement specifier, encoded in 'Q':

## &lt;Ta&gt;

## &lt;Vn&gt;

|   Q | <Ta>   |
|-----|--------|
|   0 | 8B     |
|   1 | 16B    |

For the 'Single register table' variant: is the name of the SIMD&amp;FP table register, encoded in the 'Rn' field.

For the 'Four register table', 'Three register table', and 'Two register table' variants: is the name of the first SIMD&amp;FP table register, encoded in the 'Rn' field.

## &lt;Vm&gt;

Is the name of the SIMD&amp;FP index register, encoded in the 'Rm' field.

## &lt;Vn+1&gt;

Is the name of the second SIMD&amp;FP table register, encoded as 'Rn' plus 1 modulo 32.

## &lt;Vn+2&gt;

Is the name of the third SIMD&amp;FP table register, encoded as 'Rn' plus 2 modulo 32.

## &lt;Vn+3&gt;

Is the name of the fourth SIMD&amp;FP table register, encoded as 'Rn' plus 3 modulo 32.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) indices = V[m, datasize]; bits(128*regs) table = Zeros(128*regs); bits(datasize) result; integer index; // Create table from registers for i = 0 to regs - 1 Elem[table, i, 128] = V[(n+i) MOD 32, 128]; result = if is_tbl then Zeros(datasize) else V[d, for i = 0 to elements - 1 index = UInt(Elem[indices, i, 8]); if index < 16 * regs then Elem[result, i, 8] = Elem[table, index, 8]; V[d, datasize] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
datasize];
```
