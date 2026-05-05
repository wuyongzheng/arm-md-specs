## C6.2.342 REV16

Reverse bytes in 16-bit halfwords

This instruction reverses the byte order in each 16-bit halfword of a register.

<!-- image -->

## Encoding for the 32-bit variant

```
Applies when (sf == 0) REV16 <Wd>, <Wn>
```

## Encoding for the 64-bit variant

```
Applies when (sf == 1) REV16 <Xd>, <Xn>
```

## Decode for all variants of this encoding

```
'0' then EndOfDecode(Decode_UNDEF);
```

```
if opc == '11' && sf == constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer datasize = 32 << UInt(sf); constant integer container_size = 8 << UInt(opc);
```

## Assembler Symbols

&lt;Wd&gt;

Is the 32-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Wn&gt;

Is the 32-bit name of the general-purpose source register, encoded in the 'Rn' field.

## &lt;Xd&gt;

## &lt;Xn&gt;

Is the 64-bit name of the general-purpose source register, encoded in the 'Rn' field.

## Operation

```
constant bits(datasize) operand = X[n, datasize]; bits(datasize) result; constant integer containers = datasize DIV container_size; for c = 0 to containers-1 constant bits(container_size) container = Elem[operand, c, container_size]; Elem[result, c, container_size] = Reverse(container, 8); X[d, datasize] = result;
```

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
