## F5.1.270 UDF

Permanently Undefined generates an Undefined Instruction exception.

The encodings for UDF used in this section are defined as permanently UNDEFINED. However:

- With the T32 instruction set, Arm deprecates using the UDF instruction in an IT block.
- In the A32 instruction set, UDF is not conditional.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1 and T2).

A1

<!-- image -->

## Encoding

```
UDF{<c>}{<q>} {#}<imm>
```

## Decode for this encoding

```
constant bits(32) imm32 = ZeroExtend(imm12:imm4, 32); // imm32 is for assembly and disassembly only, and is ignored by hardware.
```

T1

## Encoding

```
UDF{<c>}{<q>} {#}<imm>
```

## Decode for this encoding

```
constant bits(32) imm32 = ZeroExtend(imm8, 32); // imm32 is for assembly and disassembly only, and is ignored
```

T2

<!-- image -->

## Encoding

<!-- image -->

```
by hardware.
```

```
UDF{<c>}{<q>} {#}<imm> UDF{<c>}.W {#}<imm> // (<imm> can be represented in T1)
```

## Decode for this encoding

```
constant bits(32) imm32 = ZeroExtend(imm4:imm12, 32); // imm32 is for assembly and disassembly only, and is ignored
```

## Assembler Symbols

&lt;c&gt;

For the 'A1' variant: see Standard assembler syntax fields. &lt;c&gt; must be AL or omitted.

For the 'T1' and 'T2' variants: see Standard assembler syntax fields. Arm deprecates using any &lt;c&gt; value other than AL .

See Standard assembler syntax fields.

## &lt;imm&gt;

For the 'A1' variant: is a 16-bit unsigned immediate, in the range 0 to 65535, encoded in the 'imm12:imm4' field. The PE ignores the value of this constant.

For the 'T1' variant: is a 8-bit unsigned immediate, in the range 0 to 255, encoded in the 'imm8' field. The PE ignores the value of this constant.

For the 'T2' variant: is a 16-bit unsigned immediate, in the range 0 to 65535, encoded in the 'imm4:imm12' field. The PE ignores the value of this constant.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); UNDEFINED;
```

## &lt;q&gt;

```
by hardware.
```