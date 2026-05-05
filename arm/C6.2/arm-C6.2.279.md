## C6.2.279 MOV (wide immediate)

Move wide immediate value

This instruction moves a 16-bit immediate value to a register.

This is an alias of MOVZ. This means:

- The encodings in this description are named to match the encodings of MOVZ.
- The description of MOVZ gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

<!-- image -->

## Encoding for the 32-bit variant

Applies when

(sf

== 0 &amp;&amp; hw == 0x)

MOV

&lt;Wd&gt;, #&lt;imm&gt;

## is equivalent to

```
MOVZ <Wd>, #<imm16>, LSL #<shift>
```

and is the preferred disassembly when !(IsZero(imm16) &amp;&amp; hw != '00') .

## Encoding for the 64-bit variant

Applies when (sf ==

```
1) MOV <Xd>, #<imm>
```

## is equivalent to

```
MOVZ <Xd>, #<imm16>, LSL #<shift>
```

and is the preferred disassembly when !(IsZero(imm16) &amp;&amp; hw != '00') .

## Assembler Symbols

## &lt;Wd&gt;

Is the 32-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;imm&gt;

For the '32-bit' variant: is a 32-bit immediate which can be encoded in 'imm16:hw'.

For the '64-bit' variant: is a 64-bit immediate which can be encoded in 'imm16:hw'.

## &lt;Xd&gt;

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## Operation

The description of MOVZ gives the operational pseudocode for this instruction.
