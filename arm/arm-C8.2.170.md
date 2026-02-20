## C8.2.170 FCMLT (vectors)

Floating-point compare less than vector

This instruction compares active floating-point elements in the first source vector being less than the corresponding elements in the second source vector, and places the boolean results of the comparison in the corresponding elements of the destination predicate. Inactive elements in the destination predicate register are set to zero. This instruction does not set the condition flags.

This is a pseudo-instruction of FCM&lt;cc&gt; (vectors). This means:

- The encodings in this description are named to match the encodings of FCM&lt;cc&gt; (vectors).
- The assembler syntax is used only for assembly, and is not used on disassembly.
- The description of FCM&lt;cc&gt; (vectors) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## Greater than

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
FCMLT <Pd>.<T>, <Pg>/Z, <Zm>.<T>, <Zn>.<T>
```

## is equivalent to

```
FCMGT <Pd>.<T>, <Pg>/Z, <Zn>.<T>, <Zm>.<T>
```

## Assembler Symbols

## &lt;Pd&gt;

Is the name of the destination scalable predicate register, encoded in the 'Pd' field.

Is the size specifier, encoded in 'size':

## &lt;T&gt;

## &lt;Pg&gt;

|   size | <T>      |
|--------|----------|
|     00 | RESERVED |
|     01 | H        |
|     10 | S        |
|     11 | D        |

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## &lt;Zn&gt;

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## Operation

The description of FCM&lt;cc&gt; (vectors) gives the operational pseudocode for this instruction.

## Operational Information

The description of FCM&lt;cc&gt; (vectors) gives the operational information for this instruction.