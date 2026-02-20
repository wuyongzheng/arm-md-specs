## F5.1.114 MOV, MOVS (register-shifted register)

Move (register-shifted register) copies a register-shifted register value to the destination register. It can optionally update the condition flags based on the value.

This instruction is used by the aliases ASRS (register), ASR (register), LSLS (register), LSL (register), LSRS (register), LSR (register), RORS (register), and ROR (register).

It has encodings from the following instruction sets: A32 (A1) and T32 (T1 and T2).

A1

<!-- image -->

## Encoding for the Flag setting variant

```
Applies when (S == 1) MOVS{<c>}{<q>} <Rd>, <Rm>, <shift> <Rs>
```

## Encoding for the Not flag setting variant

```
Applies when (S == 0) MOV{<c>}{<q>} <Rd>, <Rm>, <shift>
```

```
<Rs>
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant integer m = UInt(Rm); constant integer s = UInt(Rs); constant boolean setflags = (S == '1'); constant SRType shift_t = DecodeRegShift(stype); if d == 15 || m == 15 || s == 15 then
```

T1

```
UNPREDICTABLE;
```

<!-- image -->

## Encoding for the Arithmetic shift right variant

```
Applies when (op == 0100) MOV<c>{<q>} <Rdm>, <Rdm>, ASR <Rs> // (InITBlock()) MOVS{<q>} <Rdm>, <Rdm>, ASR <Rs> // (Outside IT block)
```

## Encoding for the Logical shift left variant

Applies when

(op

==

0010)

```
MOV<c>{<q>} <Rdm>, <Rdm>, LSL <Rs> // (InITBlock()) MOVS{<q>} <Rdm>, <Rdm>, LSL <Rs> // (Outside IT block)
```

## Encoding for the Logical shift right variant

```
Applies when (op == 0011) MOV<c>{<q>} <Rdm>, <Rdm>, LSR <Rs> // (InITBlock()) MOVS{<q>} <Rdm>, <Rdm>, LSR <Rs> // (Outside IT block)
```

## Encoding for the Rotate right variant

```
Applies when (op == 0111) MOV<c>{<q>} <Rdm>, <Rdm>, ROR <Rs> // (InITBlock()) MOVS{<q>} <Rdm>, <Rdm>, ROR <Rs> // (Outside IT block)
```

## Decode for all variants of this encoding

```
if ! op IN {'0010', '0011', '0100', '0111'} then SEE "Related encodings"; constant integer d = UInt(Rdm); constant integer m = UInt(Rdm); constant integer s = UInt(Rs); constant boolean setflags = !InITBlock(); constant SRType shift_t = DecodeRegShift(op<2>:op<0>);
```

T2

<!-- image -->

## Encoding for the Flag setting variant

```
Applies when (S == 1) MOVS{<c>}{<q>} <Rd>, <Rm>, <shift> <Rs> MOVS.W <Rd>, <Rm>, <shift> <Rs> // (Outside IT block, and <Rd>, <Rm>, <shift>, <Rs> can be represented ↪ → in T1)
```

## Encoding for the Not flag setting variant

```
Applies when (S == 0) MOV{<c>}{<q>} <Rd>, <Rm>, <shift> <Rs> MOV<c>.W <Rd>, <Rm>, <shift> <Rs> // (Inside IT block, and <Rd>, <Rm>, <shift>, <Rs> can be represented ↪ → in T1)
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant integer m = UInt(Rm); constant integer s = UInt(Rs); constant boolean setflags = (S == '1'); constant SRType shift_t = DecodeRegShift(stype); // Armv8-A removes UNPREDICTABLE for R13 if d == 15 || m == 15 || s == 15 then
```

```
UNPREDICTABLE;
```

Related encodings: In encoding T1, for an op field value that is not described above, see Data-processing (two low registers).

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

&lt;q&gt;

&lt;Rd&gt;

Is the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Rm&gt;

Is the general-purpose source register, encoded in the 'Rm' field.

## &lt;shift&gt;

Is the type of shift to be applied to the second source register, encoded in 'stype':

|   stype | <shift>   |
|---------|-----------|
|      00 | LSL       |
|      01 | LSR       |
|      10 | ASR       |
|      11 | ROR       |

## &lt;Rs&gt;

Is the general-purpose source register holding a shift amount in its bottom 8 bits, encoded in the 'Rs' field.

## &lt;Rdm&gt;

Is the general-purpose source register and the destination register, encoded in the 'Rdm' field.

## Alias Conditions

| Alias   |            | Of variant Is preferred when   |                              |
|---------|------------|--------------------------------|------------------------------|
| ASRS    | (register) | A1 Flag setting                | S == '1' && stype == '10'    |
| ASRS    | (register) | T1 Arithmetic shift right      | op == '0100' && !InITBlock() |
| ASRS    | (register) | T2 Flag setting                | stype == '10' && S == '1'    |
| ASRS    | (register) | T2 Flag setting                | Unconditionally              |
| ASR     | (register) | A1 Not flag setting            | S == '0' && stype == '10'    |
| ASR     | (register) | T1 Arithmetic shift right      | op == '0100' && InITBlock()  |
| ASR     | (register) | T2 Not flag setting            | stype == '10' && S == '0'    |
| ASR     | (register) | T2 Not flag setting            | Unconditionally              |
| LSLS    | (register) | A1 Flag setting                | S == '1' && stype == '00'    |
| LSLS    | (register) | T1 Logical shift left          | op == '0010' && !InITBlock() |
| LSLS    | (register) | T2 Flag setting                | stype == '00' && S == '1'    |
| LSLS    | (register) | T2 Flag setting                | Unconditionally              |
| LSL     | (register) | A1 Not flag setting            | S == '0' && stype == '00'    |
| LSL     | (register) | T1 Logical shift left          | op == '0010' && InITBlock()  |
| LSL     | (register) | T2 Not flag setting            | stype == '00' && S == '0'    |
| LSL     | (register) | T2 Not flag setting            | Unconditionally              |
| LSRS    | (register) | A1 Flag setting                | S == '1' && stype == '01'    |
| LSRS    | (register) | T1 Logical shift right         | op == '0011' && !InITBlock() |
| LSRS    | (register) | T2 Flag setting                | stype == '01' && S == '1'    |
| LSRS    | (register) | T2 Flag setting                | Unconditionally              |
| LSR     | (register) | A1 Not flag setting            | S == '0' && stype == '01'    |
| LSR     | (register) | T1 Logical shift right         | op == '0011' && InITBlock()  |
| LSR     | (register) | T2 Not flag setting            | stype == '01' && S == '0'    |
| LSR     | (register) | T2 Not flag setting            | Unconditionally              |
| RORS    | (register) | A1 Flag setting                | S == '1' && stype == '11'    |
| RORS    | (register) | T1 Rotate right                | op == '0111' && !InITBlock() |
| RORS    | (register) | T2 Flag setting                | stype == '11' && S == '1'    |
| RORS    | (register) | T2 Flag setting                | Unconditionally              |
| ROR     | (register) | A1 Not flag setting            | S == '0' && stype == '11'    |
| ROR     | (register) | T1 Rotate right                | op == '0111' && InITBlock()  |
| ROR     | (register) | T2 Not flag setting            | stype == '11' && S == '0'    |
| ROR     | (register) | T2 Not flag setting            | Unconditionally              |

## Operation

if

```
ConditionPassed() then EncodingSpecificOperations(); constant integer shift_n = UInt(R[s]<7:0>); bits(32) result; bit carry; (result, carry) = Shift_C(R[m], shift_t, shift_n, PSTATE.C); R[d] = result; if setflags then
```

```
PSTATE.N = result<31>; PSTATE.Z = IsZeroBit(result); PSTATE.C = carry; // PSTATE.V unchanged
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.