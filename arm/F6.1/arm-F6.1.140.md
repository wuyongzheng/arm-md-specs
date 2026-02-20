## F6.1.140 VMOV (register, SIMD)

Copy between SIMD registers copies the contents of one SIMD register to another.

This is an alias of VORR (register). This means:

- The encodings in this description are named to match the encodings of VORR (register).
- The description of VORR (register) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

Applies when

```
(Q == 0)
```

```
VMOV{<c>}{<q>}{.<dt>} <Dd>, <Dm>
```

## is equivalent to

```
VORR{<c>}{<q>}{.<dt>} {<Dd>, }<Dm>, <Dm>
```

and is the preferred disassembly when N :: Vn == M :: Vm .

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VMOV{<c>}{<q>}{.<dt>}
```

```
<Qd>, <Qm>
```

## is equivalent to

```
VORR{<c>}{<q>}{.<dt>} {<Qd>, }<Qm>, <Qm>
```

and is the preferred disassembly when N :: Vn == M :: Vm .

T1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

Applies when

```
(Q == 0)
```

```
VMOV{<c>}{<q>}{.<dt>} <Dd>, <Dm>
```

is equivalent to

```
VORR{<c>}{<q>}{.<dt>} {<Dd>, }<Dm>, <Dm>
```

and is the preferred disassembly when N :: Vn == M :: Vm .

## Encoding for the 128-bit SIMD vector variant

Applies when

```
(Q == 1)
```

```
VMOV{<c>}{<q>}{.<dt>} <Qd>, <Qm>
```

## is equivalent to

```
VORR{<c>}{<q>}{.<dt>} {<Qd>, }<Qm>, <Qm>
```

and is the preferred disassembly when N :: Vn == M :: Vm .

## Assembler Symbols

&lt;c&gt;

For the 'A1 128-bit SIMD vector' and 'A1 64-bit SIMD vector' variants: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1 128-bit SIMD vector' and 'T1 64-bit SIMD vector' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

An optional data type. &lt;dt&gt; must not be F64 , but it is otherwise ignored.

&lt;q&gt;

&lt;dt&gt;

## &lt;Dd&gt;

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

## &lt;Dm&gt;

Is the 64-bit name of the SIMD&amp;FP source register, encoded in the 'N:Vn' and 'M:Vm' field.

&lt;Qd&gt;

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

## &lt;Qm&gt;

Is the 128-bit name of the SIMD&amp;FP source register, encoded in the 'N:Vn' and 'M:Vm' field as &lt;Qm&gt;*2.

## Operation

The description of VORR (register) gives the operational pseudocode for this instruction.

## Operational Information

The description of VORR (register) gives the operational information for this instruction.