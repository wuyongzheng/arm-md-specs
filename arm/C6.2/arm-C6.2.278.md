## C6.2.278 MOV (inverted wide immediate)

Move inverted wide immediate value

This instruction moves an inverted 16-bit immediate value to a register.

This is an alias of MOVN. This means:

- The encodings in this description are named to match the encodings of MOVN.
- The description of MOVN gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

<!-- image -->

## Encoding for the 32-bit variant

Applies when

(sf

== 0 &amp;&amp; hw == 0x)

MOV

&lt;Wd&gt;, #&lt;imm&gt;

## is equivalent to

```
MOVN <Wd>, #<imm16>, LSL #<shift>
```

and is the preferred disassembly when !(IsZero(imm16) &amp;&amp; hw != '00') &amp;&amp; !IsOnes(imm16) .

## Encoding for the 64-bit variant

Applies when (sf ==

```
1) MOV <Xd>, #<imm>
```

## is equivalent to

```
MOVN <Xd>, #<imm16>, LSL #<shift>
```

and is the preferred disassembly when !(IsZero(imm16) &amp;&amp; hw != '00') .

## Assembler Symbols

## &lt;Wd&gt;

Is the 32-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;imm&gt;

For the '32-bit' variant: is a 32-bit immediate, the bitwise inverse of which can be encoded in 'imm16:hw', but excluding 0xffff0000 and 0x0000 ffff

For the '64-bit' variant: is a 64-bit immediate, the bitwise inverse of which can be encoded in 'imm16:hw'.

<!-- image -->

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## Operation

The description of MOVN gives the operational pseudocode for this instruction.
